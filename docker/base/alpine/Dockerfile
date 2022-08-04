#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/base:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/bootstrap:alpine

ARG TARGETARCH

ENV DOCKER_CONF_HOME=/opt/docker/ \
    LOG_STDOUT="" \
    LOG_STDERR=""

COPY conf/ /opt/docker/

RUN set -x \
    # Install services
    && chmod +x /opt/docker/bin/* \
    && apk-install \
        supervisor \
        wget \
        curl \
        vim \
        sed \
        tzdata \
        busybox-suid \
    && chmod +s /sbin/gosu \
    && docker-run-bootstrap \
    && docker-image-cleanup

ENTRYPOINT ["/entrypoint"]
CMD ["supervisord"]
