#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/apache:debian-7
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

COPY conf/ /opt/docker/

RUN set -x \
    # Install apache
    && apt-install \
        apache2 \
        apache2-mpm-worker \
        libapache2-mod-fastcgi \
    && sed -ri ' \
        s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
        s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
        ' /etc/apache2/apache2.conf \
    && rm -f /etc/apache2/sites-enabled/* \
    && a2enmod actions fastcgi ssl rewrite headers expires \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 80 443
