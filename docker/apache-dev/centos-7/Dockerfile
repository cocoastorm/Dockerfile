#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/apache-dev:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/apache:centos-7

ARG BUILDARCH
ARG TARGETARCH

ENV WEB_NO_CACHE_PATTERN="\.(css|js|gif|png|jpg|svg|json|xml)$"

COPY conf/ /opt/docker/

RUN set -x \
     \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && symlink-go-replace \
    && docker-image-cleanup

EXPOSE 80 443
