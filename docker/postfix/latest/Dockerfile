#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/postfix:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM webdevops/base-app:latest

ARG BUILDARCH
ARG TARGETARCH

COPY conf/ /opt/docker/

RUN set -x \
    && docker-service enable syslog \
    && docker-service enable postfix \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup

EXPOSE 25 465 587
