#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/bootstrap:centos-7
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++


# Staged baselayout builder
FROM --platform=$BUILDPLATFORM ghcr.io/cocoastorm/webdevops/toolbox:latest AS baselayout
RUN mkdir -p \
        /baselayout/sbin \
        /baselayout/usr/local/bin \
    # Baselayout scripts
    && wget -O /tmp/baselayout-install.sh https://raw.githubusercontent.com/webdevops/Docker-Image-Baselayout/master/install.sh \
    && sh /tmp/baselayout-install.sh /baselayout \
    ## Install go-replace
    && export grArch="$(echo $TARGETARCH | sed s/amd64/64/g)" \
    && wget -O "/baselayout/usr/local/bin/go-replace" "https://github.com/webdevops/goreplace/releases/download/1.1.2/gr-$grArch-linux" \
    && chmod +x "/baselayout/usr/local/bin/go-replace" \
    && go-replace version \
    # Install gosu
    && wget -O "/baselayout/sbin/gosu" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$TARGETARCH" \
    && wget -O "/baselayout/sbin/gosu.asc" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$TARGETARCH.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /baselayout/sbin/gosu.asc "/baselayout/sbin/gosu" \
    && rm -rf "$GNUPGHOME" \
    && chmod +x "/baselayout/sbin/gosu"


FROM --platform=$BUILDPLATFORM centos:7

ARG TARGETARCH

LABEL maintainer=info@webdevops.io \
      vendor=WebDevOps.io \
      io.webdevops.layout=8 \
      io.webdevops.version=1.5.0

ENV TERM="xterm" \
    LANG="en_US.utf8" \
    LC_ALL="en_US.utf8"


# Baselayout copy (from staged image)
COPY --from=baselayout /baselayout /


RUN set -x \
    # Init bootstrap
    # System update
    && /usr/local/bin/yum-upgrade \
    && yum-install \
        epel-release \
    && /usr/local/bin/generate-dockerimage-info \
    && docker-run-bootstrap \
    && docker-image-cleanup
