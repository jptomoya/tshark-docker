# tshark-docker
A minimal Dockerfile to run the tshark on Ubuntu 24.04.

## docker build example

```bash
$ docker build -t tshark-docker .
[+] Building 24.0s (8/8) FINISHED                                                                docker:default
 => [internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 321B                                                                       0.0s
 => [internal] load metadata for docker.io/library/ubuntu:24.04                                            0.0s
 => [internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                            0.0s
 => [internal] load build context                                                                          0.0s
 => => transferring context: 1.29kB                                                                        0.0s
 => [1/3] FROM docker.io/library/ubuntu:24.04                                                              0.0s
 => [2/3] COPY install-tshark.sh /                                                                         0.0s
 => [3/3] RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget   && /in  23.4s
 => exporting to image                                                                                     0.4s
 => => exporting layers                                                                                    0.4s
 => => writing image sha256:1e3a8bc1924f80f4d856485b0ef0500924f6b9475ebf73e160fb7f313a0c4f8b               0.0s
 => => naming to docker.io/library/tshark-docker                                                           0.0s
$ docker images | grep tshark-docker
tshark-docker                latest                1e3a8bc1924f   3 seconds ago   274MB
$ docker run -it --rm tshark-docker tshark -v
Running as user "root" and group "root". This could be dangerous.
TShark (Wireshark) 4.4.0 (v4.4.0-0-g009a163470b5).

Copyright 1998-2024 Gerald Combs <gerald@wireshark.org> and contributors.
Licensed under the terms of the GNU General Public License (version 2 or later).
This is free software; see the file named COPYING in the distribution. There is
NO WARRANTY; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) using GCC 13.2.0, with GLib 2.80.0, with libpcap, with POSIX
capabilities (Linux), with libnl 3, with zlib 1.3, without zlib-ng, with PCRE2,
with Lua 5.4.6, with GnuTLS 3.8.3 and PKCS #11 support, with Gcrypt 1.10.3, with
Kerberos (MIT), with MaxMind, with nghttp2 1.59.0, with nghttp3 0.8.0, with
brotli, with LZ4, with Zstandard, with Snappy, with libxml2 2.9.14, with libsmi
0.4.8, with binary plugins.

Running on Linux 5.15.153.1-microsoft-standard-WSL2, with AMD Ryzen 7 PRO 6850U
with Radeon Graphics (with SSE4.2), with 15370 MB of physical memory, with GLib
2.80.0, with libpcap 1.10.4 (with TPACKET_V3), with zlib 1.3, with PCRE2 10.42
2022-12-11, with c-ares 1.27.0, with GnuTLS 3.8.3, with Gcrypt 1.10.3, with
nghttp2 1.59.0, with nghttp3 0.8.0, with brotli 1.1.0, with LZ4 1.9.4, with
Zstandard 1.5.5, with libsmi 0.4.8, with LC_TYPE=C, binary plugins supported.
```
