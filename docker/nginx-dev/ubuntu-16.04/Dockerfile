#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/nginx-dev:ubuntu-16.04
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/nginx:ubuntu-16.04

ARG TARGETARCH

ENV WEB_NO_CACHE_PATTERN="\.(css|js|gif|png|jpg|svg|json|xml)$"

COPY conf/ /opt/docker/

EXPOSE 80 443
