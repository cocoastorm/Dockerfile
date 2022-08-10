#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/ansible:alpine
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/bootstrap:alpine

ARG BUILDARCH
ARG TARGETARCH

RUN set -x \
    # Install ansible
    && apk-install \
        python \
        python-dev \
        py-setuptools \
        py-crypto \
        py2-pip \
        py-cparser \
        py-cryptography \
        py-markupsafe \
        py-cffi \
        py-yaml \
        py-jinja2 \
        py-paramiko \
        openssh-client \
    && pip install --upgrade pip \
    && hash -r \
    && pip install --no-cache-dir ansible \
    && chmod 750 /usr/bin/ansible* \
    # Cleanup
    && apk del python-dev \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
