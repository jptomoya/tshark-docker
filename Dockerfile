FROM ubuntu:22.04

RUN mkdir -p /root/debs
WORKDIR /root/debs

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget \
# picked from latest Ubuntu APT Package: https://gitlab.com/wireshark/wireshark/-/pipelines?page=1&scope=tags&status=success
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/libwireshark-data_4.0.5_all.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/libwsutil14_4.0.5_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/libwiretap13_4.0.5_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/libwireshark16_4.0.5_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/wireshark-common_4.0.5_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/4102638734/artifacts/raw/ubuntu-packages/tshark_4.0.5_amd64.deb \
  && apt-get purge --auto-remove -y ca-certificates wget \
  && (DEBIAN_FRONTEND=noninteractive dpkg -i -R /root/debs || :) \
  && apt-get install -y --fix-broken --no-install-recommends \
  && DEBIAN_FRONTEND=noninteractive dpkg -i -R /root/debs \
  && rm -rf /root/debs \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /
