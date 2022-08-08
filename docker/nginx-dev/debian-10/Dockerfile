#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/nginx-dev:debian-10
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/nginx:debian-10

ARG BUILDARCH
ARG TARGETARCH

ENV WEB_NO_CACHE_PATTERN="\.(css|js|gif|png|jpg|svg|json|xml)$"

COPY conf/ /opt/docker/

EXPOSE 80 443
