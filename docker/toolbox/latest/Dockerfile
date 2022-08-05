#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/toolbox:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM --platform=$BUILDPLATFORM alpine:latest

ARG TARGETARCH

RUN apk add --no-cache \
        ca-certificates \
        dpkg \
        openssl \
        curl \
        bash \
        sed \
        wget \
        zip \
        unzip \
        bzip2 \
        p7zip \
        drill \
        ldns \
        openssh-client \
        rsync \
        git \
        gnupg \
    ## Install go-replace
    && export grArch="$(echo $TARGETARCH | sed s/amd64/64/g)" \
    && wget -O "/usr/local/bin/go-replace" "https://github.com/webdevops/goreplace/releases/download/1.1.2/gr-$grArch-linux" \
    && chmod +x "/usr/local/bin/go-replace"
