#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/apache-dev:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/apache:alpine

ARG BUILDARCH
ARG TARGETARCH

ENV WEB_NO_CACHE_PATTERN="\.(css|js|gif|png|jpg|svg|json|xml)$"

COPY conf/ /opt/docker/

RUN set -x \
     \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 80 443
