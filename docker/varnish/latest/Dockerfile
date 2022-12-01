#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/varnish:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/base:alpine

ARG BUILDARCH
ARG TARGETARCH

ENV VARNISH_PORT    80

ENV VARNISH_CONFIG  ""
ENV VARNISH_STORAGE "malloc,128m"
ENV VARNISH_OPTS    ""

ENV VARNISH_BACKEND_HOST ""
ENV VARNISH_BACKEND_PORT "80"

COPY conf/ /opt/docker/

RUN set -x \
    && apk-install \
        varnish \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

CMD ["varnishd"]

EXPOSE 80
