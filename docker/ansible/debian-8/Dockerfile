#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/ansible:debian-8
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/bootstrap:debian-8

ARG BUILDARCH
ARG TARGETARCH

RUN set -x \
    # Install ansible
    && apt-install \
        # Install ansible
        python-minimal \
        python-setuptools \
        python-pip \
        python-paramiko \
        python-jinja2 \
        python-dev \
        libffi-dev \
        libssl-dev \
        build-essential \
        openssh-client \
    && pip install --upgrade pip \
    && hash -r \
    && pip install --no-cache-dir ansible \
    && chmod 750 /usr/local/bin/ansible* \
    # Cleanup
    && apt-get purge -y -f --force-yes \
        python-dev \
        build-essential \
        libssl-dev \
        libffi-dev \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
