#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/sphinx:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM ghcr.io/cocoastorm/webdevops/bootstrap:alpine

ARG BUILDARCH
ARG TARGETARCH

RUN set -x \
    && apk-install \
    # General python
    python \
    py-crypto \
    py2-pip \
    # General sphinx
    py-pillow \
    py-yaml \
    py-sphinx \
    py-sphinx_rtd_theme \
    # GRAPHVIZ
    graphviz \
    ttf-dejavu \
    && pip install --upgrade pip \
    && hash -r \
    && pip install --upgrade sphinxcontrib-googlechart \
    && pip install --upgrade sphinxcontrib-googlemaps \
    && pip install --upgrade sphinxcontrib-httpdomain \
    && pip install --upgrade sphinxcontrib-slide \
    && pip install --upgrade sphinx-autobuild \
    && pip install --upgrade recommonmark \
    # TYPO3 stuff
    && pip install t3SphinxThemeRtd \
    && pip install t3fieldlisttable \
    && pip install t3tablerows \
    && pip install t3targets \
    && docker-arch-info $BUILDARCH $TARGETARCH \
&& docker-run-bootstrap \
    && docker-arch-info $TARGETARCH \
    && docker-image-cleanup
