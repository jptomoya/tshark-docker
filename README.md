# tshark-docker
Run a newer `tshark` in Docker, based on Ubuntu 26.04.

This repository tracks the stable `.deb` artifacts published by Wireshark's official GitLab CI/CD, rather than the version typically available from Ubuntu `apt`. Updates are handled automatically so the image stays close to upstream releases while using packages built by the Wireshark project itself.


## docker build example

```bash
$ docker build -t tshark-docker .
[+] Building 152.6s (8/8) FINISHED                                                               docker:default
 => [internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 321B                                                                       0.0s
 => [internal] load metadata for docker.io/library/ubuntu:26.04                                            0.0s
 => [internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                            0.0s
 => [1/3] FROM docker.io/library/ubuntu:26.04                                                              0.0s
 => [internal] load build context                                                                          0.0s
 => => transferring context: 1.30kB                                                                        0.0s
 => [2/3] COPY install-tshark.sh /                                                                         0.0s
 => [3/3] RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget   && /i  151.9s
 => exporting to image                                                                                     0.5s
 => => exporting layers                                                                                    0.4s
 => => writing image sha256:123b1724aaf2cbe14d3a9061e2c2e6abf268b909874acb3a4d36417281e4b00a               0.0s
 => => naming to docker.io/library/tshark-docker                                                           0.0s
$ docker images | grep -i tshar
tshark-docker                                          latest                123b1724aaf2   10 seconds ago   272MB
$ docker run -it --rm tshark-docker tshark -v
Running as user "root" and group "root". This could be dangerous.
TShark (Wireshark) 4.6.7 (v4.6.7-0-gb439fb7b47a9).

Copyright 1998-2026 Gerald Combs <gerald@wireshark.org> and contributors.
Licensed under the terms of the GNU General Public License (version 2 or later).
This is free software; see the file named COPYING in the distribution. There is
NO WARRANTY; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compile-time info:
 Bit width: 64-bit
  Compiler: GCC 15.2.0
      GLib: 2.88.0
 With:
  +brotli                      +MaxMind
  +Gcrypt 1.12.0               +nghttp2 1.68.0
  +GnuTLS 3.8.12 and PKCS#11   +nghttp3 1.12.0
  +Kerberos (MIT)              +PCRE2 10.46 2025-08-27
  +libnl 3                     +POSIX capabilities (Linux)
  +libpcap                     +Snappy 1.2.2
  +libsmi 0.4.8                +xxhash 0.8.3
  +libxml2 2.15.2              +zlib 1.3.1
  +Lua 5.5.0                   +Zstandard 1.5.7
  +LZ4 1.10.0
 Without:
  -zlib-ng

Runtime info:
      OS: Linux 6.18.33.2-microsoft-standard-WSL2
     CPU: AMD Ryzen 7 PRO 6850U with Radeon Graphics (with SSE4.2)
  Memory: 15365 MB of physical memory
    GLib: 2.88.0
  Locale: LC_TYPE=C
 Plugins: supported, 0 loaded
 With:
  +brotli 1.2.0
  +c-ares 1.34.6
  +Gcrypt 1.12.0
  +GnuTLS 3.8.12
  +libpcap 1.10.6 (64-bit time_t, with TPACKET_V3)
  +libsmi 0.4.8
  +LZ4 1.10.0
  +nghttp2 1.68.0
  +nghttp3 1.12.0
  +PCRE2 10.46 2025-08-27
  +xxhash 803
  +zlib 1.3.1
  +Zstandard 1.5.7
```
