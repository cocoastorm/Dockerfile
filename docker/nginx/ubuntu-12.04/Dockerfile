#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/nginx:ubuntu-12.04
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/base:ubuntu-12.04

ARG BUILDARCH
ARG TARGETARCH

ENV WEB_DOCUMENT_ROOT=/app \
    WEB_DOCUMENT_INDEX=index.php \
    WEB_ALIAS_DOMAIN=*.vm \
    WEB_PHP_TIMEOUT=600 \
    WEB_PHP_SOCKET=""
ENV SERVICE_NGINX_CLIENT_MAX_BODY_SIZE="50m"

COPY conf/ /opt/docker/

RUN set -x \
    # Install nginx
    && apt-install \
        nginx \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 80 443
