FROM ubuntu:22.04

RUN mkdir -p /root/debs
WORKDIR /root/debs

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates wget \
  libbcg729-0 libc-ares2 liblua5.2-0 libnghttp2-14 libopus0 libsbc1 libsmi2ldbl libsnappy1v5 libspandsp2 libcap2-bin libmaxminddb0 libnl-3-200 libnl-genl-3-200 libpam-cap libpcap0.8 libssh-gcrypt-4 libglib2.0-0 libbrotli1 libxml2 \
# picked from latest Ubuntu APT Package: https://gitlab.com/wireshark/wireshark/-/pipelines?page=1&scope=tags&status=success
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/libwireshark-data_4.0.4_all.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/libwsutil14_4.0.4_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/libwiretap13_4.0.4_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/libwireshark16_4.0.4_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/wireshark-common_4.0.4_amd64.deb \
  && wget --no-hsts https://gitlab.com/wireshark/wireshark/-/jobs/3866543367/artifacts/raw/ubuntu-packages/tshark_4.0.4_amd64.deb \
  && apt-get purge --auto-remove -y ca-certificates wget \
  && dpkg -i libwireshark-data_4.0.4_all.deb \
  && dpkg -i libwsutil14_4.0.4_amd64.deb \
  && dpkg -i libwiretap13_4.0.4_amd64.deb \
  && dpkg -i libwireshark16_4.0.4_amd64.deb \
  && DEBIAN_FRONTEND=noninteractive dpkg -i wireshark-common_4.0.4_amd64.deb \
  && dpkg -i tshark_4.0.4_amd64.deb \
  && rm -rf /root/debs \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /
