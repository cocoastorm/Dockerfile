#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/bootstrap:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

<<<<<<< HEAD
=======

>>>>>>> upstream/php-ci
FROM alpine:3.11

ARG BUILDARCH
ARG TARGETARCH

LABEL maintainer=info@webdevops.io \
      vendor=WebDevOps.io \
      io.webdevops.layout=8 \
      io.webdevops.version=1.5.0

ENV TERM="xterm" \
    LANG="C.UTF-8" \
    LC_ALL="C.UTF-8"


# Baselayout copy (from staged image)
COPY --from=ghcr.io/cocoastorm/webdevops/toolbox:buster /baselayout/sbin/* /sbin/
COPY --from=ghcr.io/cocoastorm/webdevops/toolbox:buster /baselayout/usr/local/bin/* /usr/local/bin/

RUN set -x \
    # Init bootstrap
    # Add community
    && echo https://dl-4.alpinelinux.org/alpine/v3.11/community/ >> /etc/apk/repositories \
    # System update
    && /usr/local/bin/apk-upgrade \
    # Install base stuff
    && apk-install \
        bash \
        ca-certificates \
        openssl \
    && update-ca-certificates \
    && /usr/local/bin/generate-dockerimage-info \
    ## Fix su execution (eg for tests)
    && mkdir -p /etc/pam.d/ \
    && echo 'auth sufficient pam_rootok.so' >> /etc/pam.d/su \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
