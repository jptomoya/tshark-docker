# tshark-docker
Run a newer `tshark` in Docker, based on Ubuntu 24.04.

This repository tracks the stable `.deb` artifacts published by Wireshark's official GitLab CI/CD, rather than the version typically available from Ubuntu `apt`. Updates are handled automatically so the image stays close to upstream releases while using packages built by the Wireshark project itself.


## docker build example

```bash
$ docker build -t tshark-docker .
[+] Building 29.5s (8/8) FINISHED                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 321B                                                                           0.0s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                                0.0s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 1.30kB                                                                            0.0s
 => CACHED [1/3] FROM docker.io/library/ubuntu:24.04                                                           0.0s
 => [2/3] COPY install-tshark.sh /                                                                             0.0s
 => [3/3] RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget   && /instal  28.7s
 => exporting to image                                                                                         0.6s
 => => exporting layers                                                                                        0.5s
 => => writing image sha256:ec11293c1de394253a24317d4f10867101fd76677645b630a8b23a92e68d67ee                   0.0s
 => => naming to docker.io/library/tshark-docker                                                               0.0s
$ docker images | grep tshark-docker
tshark-docker                                          latest                ec11293c1de3   2 seconds ago       280MB
$ docker run -it --rm tshark-docker tshark -v
Running as user "root" and group "root". This could be dangerous.
TShark (Wireshark) 4.6.4 (v4.6.4-0-g93282876538d).

Copyright 1998-2026 Gerald Combs <gerald@wireshark.org> and contributors.
Licensed under the terms of the GNU General Public License (version 2 or later).
This is free software; see the file named COPYING in the distribution. There is
NO WARRANTY; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compile-time info:
 Bit width: 64-bit
  Compiler: GCC 13.3.0
      GLib: 2.80.0
 With:
  +brotli                      +MaxMind
  +Gcrypt 1.10.3               +nghttp2 1.59.0
  +GnuTLS 3.8.3 and PKCS#11    +nghttp3 0.8.0
  +Kerberos (MIT)              +PCRE2 10.42 2022-12-11
  +libnl 3                     +POSIX capabilities (Linux)
  +libpcap                     +Snappy 1.1.10
  +libsmi 0.4.8                +xxhash 0.8.2
  +libxml2 2.9.14              +zlib 1.3
  +Lua 5.4.6                   +Zstandard 1.5.5
  +LZ4 1.9.4
 Without:
  -zlib-ng

Runtime info:
      OS: Linux 6.6.87.2-microsoft-standard-WSL2
     CPU: AMD Ryzen 7 PRO 6850U with Radeon Graphics (with SSE4.2)
  Memory: 15366 MB of physical memory
    GLib: 2.80.0
  Locale: LC_TYPE=C
 Plugins: supported, 0 loaded
 With:
  +brotli 1.1.0                      +nghttp2 1.59.0
  +c-ares 1.27.0                     +nghttp3 0.8.0
  +Gcrypt 1.10.3                     +PCRE2 10.42 2022-12-11
  +GnuTLS 3.8.3                      +xxhash 802
  +libpcap 1.10.4 (with TPACKET_V3)  +zlib 1.3
  +libsmi 0.4.8                      +Zstandard 1.5.5
  +LZ4 1.9.4
```
