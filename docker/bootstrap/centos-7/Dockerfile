#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/bootstrap:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++


# staged baselayout builder
FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/toolbox:alpine AS base

ARG BUILDARCH
ARG TARGETARCH

RUN set -eux \
    mkdir -p \
        /baselayout/sbin \
        /baselayout/usr/local/bin \
    ## install go-replace
    && export dpkgArch=$(dpkg --print-architecture | awk -F- '{ print $NF }') \
    && export grArch="$(echo $dpkgArch | sed s/amd64/64/g)" \
    && wget -O "/baselayout/usr/local/bin/go-replace-$dpkgArch" "https://github.com/webdevops/goreplace/releases/download/1.1.2/gr-$grArch-linux" \
    && chmod +x "/baselayout/usr/local/bin/go-replace-$dpkgArch" \
    ## install gosu
    && export dpkgArch=$(dpkg --print-architecture | awk -F- '{ print $NF }'); \
        wget -O "/baselayout/sbin/gosu" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch"; \
        wget -O "/baselayout/sbin/gosu.asc" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch.asc"; \
    GNUPGHOME="$(mktemp -d)"; \
        gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
        gpg --batch --verify /baselayout/sbin/gosu.asc "/baselayout/sbin/gosu"; \
        rm -rf "$GNUPGHOME"; \
        chmod +x "/baselayout/sbin/gosu";

FROM --platform=$BUILDPLATFORM centos:7

ARG BUILDARCH
ARG TARGETARCH

LABEL maintainer=info@webdevops.io \
      vendor=WebDevOps.io \
      io.webdevops.layout=8 \
      io.webdevops.version=1.5.0

ENV TERM="xterm" \
    LANG="en_US.utf8" \
    LC_ALL="en_US.utf8"


# base copy (from staged image)
COPY --from=base /baselayout /

RUN set -x \
    # Init bootstrap
    # System update
    && /usr/local/bin/yum-upgrade \
    && yum-install \
        epel-release \
    && /usr/local/bin/generate-dockerimage-info \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-image-cleanup
