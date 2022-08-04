#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/apache-dev:debian-10
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/apache:debian-10

ARG TARGETARCH

ENV WEB_NO_CACHE_PATTERN="\.(css|js|gif|png|jpg|svg|json|xml)$"

COPY conf/ /opt/docker/

RUN set -x \
     \
    && docker-run-bootstrap \
    && docker-image-cleanup

EXPOSE 80 443
