from __future__ import annotations
import os
import json
import urllib.request
from packaging import version

PIPELINES_URL = 'https://gitlab.com/wireshark/wireshark/-/pipelines.json?scope=tags&page=1'
SH_TEMPLATE = """#!/bin/sh
set -eu

dir_debs="$(mktemp -d)"
(
  cd "$dir_debs"

  # picked from latest Ubuntu APT Package: https://gitlab.com/wireshark/wireshark/-/pipelines?page=1&scope=tags&status=success
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwireshark-data_{version_str}_all.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwsutil17_{version_str}_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwiretap16_{version_str}_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/libwireshark19_{version_str}_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/wireshark-common_{version_str}_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/{job_id}/artifacts/raw/ubuntu-packages/tshark_{version_str}_amd64.deb
  echo "wireshark-common wireshark-common/install-setuid boolean true" | debconf-set-selections
  if ! (DEBIAN_FRONTEND=noninteractive dpkg -i -R . && :); then
    apt-get update
    apt-get install -y --fix-broken --no-install-recommends
    DEBIAN_FRONTEND=noninteractive dpkg -i -R .
  fi
)

rm -rf "$dir_debs"
"""

def generate_shellscript(job_id: int, version_str: str, filepath: str) -> None:
    content = SH_TEMPLATE.format(
        job_id=job_id,
        version_str=version_str,
    )
    
    with open(filepath, 'w') as f:
        f.write(content)

def retrieve_jobid() -> tuple[int, str]:
    has_test_stage = lambda pipeline: any(x.get('name') == 'test' for x in pipeline['details']['stages'])

    req = urllib.request.Request(PIPELINES_URL)
    with urllib.request.urlopen(req) as res:
        pipelines = json.loads(res.read())
    vers = [(x['id'], version.parse(x['ref']['name'])) for x in pipelines['pipelines'] if x['ref']['tag'] and x['ref']['name'].startswith('v') and not x['active'] and has_test_stage(x)]
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
    print(f"Latest version of tshark: {version_str}")
    generate_shellscript(job_id, version_str, 'install-tshark.sh')

