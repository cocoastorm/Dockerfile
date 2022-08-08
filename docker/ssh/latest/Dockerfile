#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/ssh:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM webdevops/base-app:latest

ARG BUILDARCH
ARG TARGETARCH

RUN set -x \
    && docker-service enable ssh \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && symlink-go-replace \
    && docker-image-cleanup

EXPOSE 22
