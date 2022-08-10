#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/ansible:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/bootstrap:centos-7

ARG BUILDARCH
ARG TARGETARCH

RUN set -x \
    # Install ansible
    && yum-install \
        epel-release \
        PyYAML \
        python-jinja2 \
        python-httplib2 \
        python-keyczar \
        python-paramiko \
        python-setuptools \
        python-setuptools-devel \
        libffi \
        python-devel \
        libffi-devel \
        openssh-clients \
    && easy_install pip \
    && pip install --upgrade pip \
    && hash -r \
    && pip install --no-cache-dir ansible \
    && chmod 750 /usr/bin/ansible* \
    # Cleanup
    && yum erase -y python-devel \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
