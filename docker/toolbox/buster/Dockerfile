#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/toolbox:buster
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM debian:buster-slim

ARG TARGETARCH

COPY --from=ghcr.io/cocoastorm/webdevops/base-layout:latest /baselayout /baselayout

RUN set -eux; \
        apt-get update; \
        apt-get install -y --no-install-recommends \
        ca-certificates \
        dpkg \
        openssl \
        curl \
        sed \
        wget \
        zip \
        unzip \
        bzip2 \
        p7zip \
        ldnsutils \
        libldns2 \
        openssh-client \
        rsync \
        git \
        gnupg \
    ; \
    rm -rf /var/lib/apt/lists/*
