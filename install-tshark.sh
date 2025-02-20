#!/bin/sh
set -eu

dir_debs="$(mktemp -d)"
(
  cd "$dir_debs"

  # picked from latest Ubuntu APT Package: https://gitlab.com/wireshark/wireshark/-/pipelines?page=1&scope=tags&status=success
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/libwireshark-data_4.4.4_all.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/libwsutil16_4.4.4_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/libwiretap15_4.4.4_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/libwireshark18_4.4.4_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/wireshark-common_4.4.4_amd64.deb
  wget https://gitlab.com/wireshark/wireshark/-/jobs/9187374022/artifacts/raw/ubuntu-packages/tshark_4.4.4_amd64.deb
  echo "wireshark-common wireshark-common/install-setuid boolean true" | debconf-set-selections
  if ! (DEBIAN_FRONTEND=noninteractive dpkg -i -R . && :); then
    apt-get update
    apt-get install -y --fix-broken --no-install-recommends
    DEBIAN_FRONTEND=noninteractive dpkg -i -R .
  fi
)

rm -rf "$dir_debs"
