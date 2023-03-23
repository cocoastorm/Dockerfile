#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/php-dev:7.2-alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/php:7.2-alpine

ARG BUILDARCH
ARG TARGETARCH

COPY conf/ /opt/docker/

RUN set -x \
    # Install development environment
    && bash -c "$(curl -L https://installer.blackfire.io/installer.sh)" \
    && blackfire php:install \
    && apk-install \
        make \
        autoconf \
        g++ \
    && pecl install xdebug \
    && apk del -f --purge \
        autoconf \
        g++ \
        make \
    && docker-php-ext-enable xdebug \
    # Enable php development services
    && docker-service enable syslog \
    && docker-service enable postfix \
    && docker-service enable ssh \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
