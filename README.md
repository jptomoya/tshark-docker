# tshark-docker
A minimal Dockerfile to run the tshark on Ubuntu 22.04.

## docker build example

```bash
$ docker build -t tshark-docker .
[+] Building 72.2s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                                                   0.0s
 => => transferring dockerfile: 38B                                                                    0.0s
 => [internal] load .dockerignore                                                                      0.0s
 => => transferring context: 2B                                                                        0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04                                        0.0s
 => [1/5] FROM docker.io/library/ubuntu:22.04                                                          0.0s
 => CACHED [2/5] RUN mkdir -p /root/debs                                                               0.0s
 => CACHED [3/5] WORKDIR /root/debs                                                                    0.0s
 => [4/5] RUN apt-get update && apt-get install -y --no-install-recommends   ca-certificates wget     70.2s
 => exporting to image                                                                                 1.8s
 => => exporting layers                                                                                1.8s
 => => writing image sha256:ab2399d741a7275f8bb24d752043a99c592a1bfe39d6e83f653f2e68fd533922           0.0s
 => => naming to docker.io/library/tshark-docker                                                       0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
$ docker images | grep tshark-docker
tshark-docker   latest        ab2399d741a7   About a minute ago   252MB
$ docker run -it --rm tshark-docker tshark -v
Running as user "root" and group "root". This could be dangerous.
TShark (Wireshark) 4.0.3 (v4.0.3-0-gc552f74cdc23).

Copyright 1998-2023 Gerald Combs <gerald@wireshark.org> and contributors.
Licensed under the terms of the GNU General Public License (version 2 or later).
This is free software; see the file named COPYING in the distribution. There is
NO WARRANTY; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) using GCC 11.3.0, with GLib 2.72.4, with PCRE2, with zlib
1.2.11, with libpcap, with POSIX capabilities (Linux), with libnl 3, with Lua
5.2.4, with GnuTLS 3.7.3 and PKCS #11 support, with Gcrypt 1.9.4, with Kerberos
(MIT), with MaxMind, with nghttp2 1.43.0, with brotli, with LZ4, with Zstandard,
with Snappy, with libxml2 2.9.13, with libsmi 0.4.8, with binary plugins.

Running on Linux 5.15.79.1-microsoft-standard-WSL2, with Intel(R) Core(TM)
i7-3520M CPU @ 2.90GHz (with SSE4.2), with 7854 MB of physical memory, with GLib
2.72.4, with PCRE2 10.39 2021-10-29, with zlib 1.2.11, with libpcap 1.10.1 (with
TPACKET_V3), with c-ares 1.18.1, with GnuTLS 3.7.3, with Gcrypt 1.9.4, with
nghttp2 1.43.0, with brotli 1.0.9, with LZ4 1.9.3, with Zstandard 1.4.8, with
libsmi 0.4.8, with LC_TYPE=C, binary plugins supported.
```
