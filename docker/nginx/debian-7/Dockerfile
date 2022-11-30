#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/nginx:debian-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/base:debian-7

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
    && printf "deb http://nginx.org/packages/debian/ wheezy  nginx\n deb-src http://nginx.org/packages/debian/ wheezy nginx" \
    >> /etc/apt/sources.list \
    && curl -L https://nginx.org/keys/nginx_signing.key | apt-key add - \
    && apt-get update \
    && apt-install \
    nginx \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 80 443
