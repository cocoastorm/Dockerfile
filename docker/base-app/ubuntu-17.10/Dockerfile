#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/base-app:ubuntu-17.10
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/base:ubuntu-17.10

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
    && apt-install \
        # Install common tools
        zip \
        unzip \
        bzip2 \
        moreutils \
        dnsutils \
        openssh-client \
        rsync \
        git \
        patch \
    && mkdir -p /var/lib/syslog-ng/ \
    && /usr/local/bin/generate-locales \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
