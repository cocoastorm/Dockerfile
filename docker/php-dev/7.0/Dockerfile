#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/php-dev:7.0
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/php:7.0

ARG BUILDARCH
ARG TARGETARCH

COPY conf/ /opt/docker/

RUN set -x \
    # Install development environment
    && wget -q -O - https://packages.blackfire.io/gpg.key | apt-key add - \
    && echo "deb https://packages.blackfire.io/debian any main" | tee /etc/apt/sources.list.d/blackfire.list \
    && apt-install \
        blackfire-php \
        blackfire-agent \
    && pecl install xdebug-2.8.1 \
    && docker-php-ext-enable xdebug \
    # Enable php development services
    && docker-service enable syslog \
    && docker-service enable postfix \
    && docker-service enable ssh \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && symlink-go-replace \
    && docker-image-cleanup
