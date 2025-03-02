#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/bootstrap:debian-9
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++


FROM debian:stretch

ARG BUILDARCH
ARG TARGETARCH

LABEL maintainer=info@webdevops.io \
      vendor=WebDevOps.io \
      io.webdevops.layout=8 \
      io.webdevops.version=1.5.0

ENV TERM="xterm" \
    LANG="C.UTF-8" \
    LC_ALL="C.UTF-8"


# Baselayout copy (from staged image)
COPY --from=ghcr.io/cocoastorm/webdevops/toolbox:buster /baselayout/sbin/* /sbin/
COPY --from=ghcr.io/cocoastorm/webdevops/toolbox:buster /baselayout/usr/local/bin/* /usr/local/bin/

RUN set -x \
    # Init bootstrap
    && apt-update \
    && /usr/local/bin/generate-dockerimage-info \
    # Enable non-free
    && sed -ri "s/(deb.*\/debian $(docker-image-info dist-codename) main)/\1 contrib non-free /" -- /etc/apt/sources.list \
    && apt-update \
    # System update
    && /usr/local/bin/apt-upgrade \
    # Base stuff
    && apt-install \
        apt-transport-https \
        ca-certificates \
        locales \
        gnupg
