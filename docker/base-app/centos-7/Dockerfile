#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/base-app:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/base:centos-7

ARG BUILDARCH
ARG TARGETARCH

ENV APPLICATION_USER=application \
    APPLICATION_GROUP=application \
    APPLICATION_PATH=/app \
    APPLICATION_UID=1000 \
    APPLICATION_GID=1000

COPY conf/ /opt/docker/

RUN set -x \
    # Install services
    && yum-install \
        dpkg \
        # Install tools
        zip \
        unzip \
        bzip2 \
        moreutils \
        dnsutils \
        bind-utils \
        rsync \
        git \
        patch \
    && /usr/local/bin/generate-locales \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-image-cleanup
