from __future__ import annotations
import os
import sys
import json
import urllib.request
from packaging import version

PIPELINES_URL = 'https://gitlab.com/wireshark/wireshark/-/pipelines.json?scope=tags&page=1&status=success'
DOCKERFILE_TEMPLATE = """FROM ubuntu:22.04

RUN mkdir -p /root/debs
WORKDIR /root/debs

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget \\
# picked from latest Ubuntu APT Package: https://gitlab.com/wireshark/wireshark/-/pipelines?page=1&scope=tags&status=success
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwireshark-data_{version_str}_all.deb \\
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwsutil14_{version_str}_amd64.deb \\
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwiretap13_{version_str}_amd64.deb \\
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwireshark16_{version_str}_amd64.deb \\
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/wireshark-common_{version_str}_amd64.deb \\
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/tshark_{version_str}_amd64.deb \\
  && apt-get purge --auto-remove -y ca-certificates wget \\
  && (DEBIAN_FRONTEND=noninteractive dpkg -i -R /root/debs || :) \\
  && apt-get install -y --fix-broken --no-install-recommends \\
  && DEBIAN_FRONTEND=noninteractive dpkg -i -R /root/debs \\
  && rm -rf /root/debs \\
  && rm -rf /var/lib/apt/lists/*

WORKDIR /
"""

def generate_dockerfile(job_id: int, version_str: str, dockerfile_path: str) -> None:
    dockerfile_content = DOCKERFILE_TEMPLATE.format(
        job_id=job_id,
        version_str=version_str,
    )
    
    with open(dockerfile_path, 'w') as f:
        f.write(dockerfile_content)

def retrieve_jobid() -> tuple[int, str]:
    req = urllib.request.Request(PIPELINES_URL)
    with urllib.request.urlopen(req) as res:
        pipelines = json.loads(res.read())
    vers = [(x['id'], version.parse(x['ref']['name'])) for x in pipelines['pipelines'] if x['ref']['tag']]
    vers = [x for x in vers if not x[1].is_prerelease]
    pipeline_id, version_str = max(vers, key=lambda x: x[1])

    artifacts_url = f'https://gitlab.com/wireshark/wireshark/-/pipelines/{pipeline_id}/downloadable_artifacts.json'
    req = urllib.request.Request(artifacts_url)
    with urllib.request.urlopen(req) as res:
        artifacts = json.loads(res.read())
    for x in artifacts['artifacts']:
        if x['name'].startswith("Ubuntu APT Package:"):
            job_id = x['path'].split('jobs/')[1].split('/')[0]
            assert(job_id.isnumeric())
            break

    return (int(job_id), str(version_str))

if __name__ == '__main__':
    job_id, version_str = retrieve_jobid()
    if filename := os.environ.get("GITHUB_STEP_SUMMARY"):
        f = open(filename, 'a')
    else:
        f = sys.stdout

    f.write(f"Latest version of tshark: {version_str}\n")
    generate_dockerfile(job_id, version_str, 'Dockerfile')

    if not f is sys.stdout:
        f.close()

