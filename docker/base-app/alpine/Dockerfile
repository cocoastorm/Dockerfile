#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/base-app:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/base:alpine

ARG BUILDARCH
ARG TARGETARCH

ENV APPLICATION_USER=application \
    APPLICATION_GROUP=application \
    APPLICATION_PATH=/app \
    APPLICATION_UID=1000 \
    APPLICATION_GID=1000

COPY conf/ /opt/docker/

RUN set -x \
    && apk-install \
        dpkg \
        shadow \
    && apk-install \
        # Install common tools
        zip \
        unzip \
        bzip2 \
        drill \
        ldns \
        openssh-client \
        rsync \
        patch \
        git \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
