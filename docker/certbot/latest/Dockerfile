#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/certbot:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/bootstrap:alpine

ARG BUILDARCH
ARG TARGETARCH

VOLUME /etc/letsencrypt
VOLUME /var/www

RUN set -x \
    && apk-install \
        gcc \
        python2-dev \
        musl-dev \
        libffi-dev \
        openssl-dev \
        py2-pip \
    && pip install --upgrade pip \
    && hash -r \
    && pip install certbot \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && symlink-go-replace \
    && docker-image-cleanup
