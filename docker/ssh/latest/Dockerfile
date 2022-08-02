#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/ssh:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM webdevops/base-app:latest

RUN set -x \
    && docker-service enable ssh \
    && docker-run-bootstrap \
    && docker-image-cleanup

EXPOSE 22
