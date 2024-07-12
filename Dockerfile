FROM ubuntu:24.04

COPY install-tshark.sh /

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget \
  && /install-tshark.sh \
  && apt-get purge --auto-remove -y ca-certificates wget \
  && rm -rf /var/lib/apt/lists/* \
  && rm -f /root/.wget-hsts

