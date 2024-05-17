#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/base:ubuntu-22.04
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/bootstrap:ubuntu-22.04

ARG BUILDARCH
ARG TARGETARCH

ENV DOCKER_CONF_HOME=/opt/docker/ \
    LOG_STDOUT="" \
    LOG_STDERR=""

COPY conf/ /opt/docker/

RUN set -x \
    # Install services
    && chmod +x /opt/docker/bin/* \
    && apt-install \
        supervisor \
        wget \
        curl \
        vim \
        net-tools \
        tzdata \
    && chmod +s /sbin/gosu \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

ENTRYPOINT ["/entrypoint"]
CMD ["supervisord"]
