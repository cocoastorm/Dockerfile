#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/php-apache:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/php:centos-7

ARG BUILDARCH
ARG TARGETARCH

ENV WEB_DOCUMENT_ROOT=/app \
    WEB_DOCUMENT_INDEX=index.php \
    WEB_ALIAS_DOMAIN=*.vm \
    WEB_PHP_TIMEOUT=600 \
    WEB_PHP_SOCKET=""
ENV WEB_PHP_SOCKET=127.0.0.1:9000

COPY conf/ /opt/docker/

RUN set -x \
    # Install apache
    && yum-install \
        httpd \
        mod_ssl \
    && sed -ri ' \
        s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
        s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
        ' /etc/httpd/conf/httpd.conf /etc/httpd/conf.d/ssl.conf \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 80 443
