#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/bootstrap:ubuntu-17.04
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ubuntu:17.04

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
    # Add multiverse
    && sed -i 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list \
    && apt-update \
    # System update
    && /usr/local/bin/apt-upgrade \
    # Install base stuff
    && apt-install \
        apt-transport-https \
        python-software-properties \
        ca-certificates \
        apt-transport-https \
    && apt-add-repository multiverse \
    && sed -i 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list \
    && apt-update \
    && /usr/local/bin/generate-dockerimage-info \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
