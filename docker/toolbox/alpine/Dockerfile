#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/toolbox:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM alpine:latest

ARG BUILDARCH
ARG TARGETARCH

RUN mkdir -p \
    /baselayout/sbin \
    /baselayout/usr/local/bin

COPY --from=ghcr.io/cocoastorm/webdevops/base-layout:latest /baselayout /baselayout

RUN set -eux; \
    apk add --no-cache \
        ca-certificates \
        dpkg \
        openssl \
        curl \
        bash \
        sed \
        wget \
        zip \
        unzip \
        bzip2 \
        p7zip \
        drill \
        ldns \
        openssh-client \
        rsync \
        git \
        gnupg \
    ; \
