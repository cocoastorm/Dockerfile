#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/php-dev:7.3-alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/php:7.3-alpine

ARG BUILDARCH
ARG TARGETARCH

COPY conf/ /opt/docker/

RUN set -x \
    # Install development environment
    && wget -q -O blackfire-agent https://packages.blackfire.io/binaries/blackfire-agent/1.34.0/blackfire-agent-linux_static_amd64 \
    && mv blackfire-agent /usr/local/bin/ \
    && chmod +x /usr/local/bin/blackfire-agent \
    && wget -q -O blackfire.so https://packages.blackfire.io/binaries/blackfire-php/1.33.0/blackfire-php-alpine_amd64-php-73.so \
    && mv blackfire.so "$(php -r "echo ini_get('extension_dir');")/blackfire.so" \
    && mkdir /var/run/blackfire/ \
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
