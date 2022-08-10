#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/php-dev:centos-7-php56
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/php:centos-7-php56

ARG BUILDARCH
ARG TARGETARCH

COPY conf/ /opt/docker/

RUN set -x \
    && wget -O - "https://packages.blackfire.io/fedora/blackfire.repo" | tee /etc/yum.repos.d/blackfire.repo \
    && yum-install \
        # Install tools
        graphviz \
        # Install php development stuff
        php56w-pecl-xdebug \
        blackfire-php \
        blackfire-agent \
        # Tools
        nano \
        vim \
    # Enable php development services
    && docker-service enable syslog \
    && docker-service enable postfix \
    && docker-service enable ssh \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
