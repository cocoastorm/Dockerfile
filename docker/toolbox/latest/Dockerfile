#+++++++++++++++++++++++++++++++++++++++
# Dockerfile for webdevops/toolbox:latest
#    -- automatically generated  --
#+++++++++++++++++++++++++++++++++++++++

FROM alpine:latest

RUN apk add --no-cache \
        ca-certificates \
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
    && mkdir -p \
            /baselayout/sbin \
            /baselayout/usr/local/bin \
        # Baselayout scripts
        && wget -O /tmp/baselayout-install.sh https://raw.githubusercontent.com/webdevops/Docker-Image-Baselayout/master/install.sh \
        && sh /tmp/baselayout-install.sh /baselayout \
        ## install go-replace
    && export dpkgArch=$(dpkg --print-architecture | awk -F- '{ print $NF }') \
    && export grArch="$(echo $dpkgArch | sed s/amd64/64/g)" \
    && wget -O "/baselayout/usr/local/bin/go-replace-$dpkgArch" "https://github.com/webdevops/goreplace/releases/download/1.1.2/gr-$grArch-linux" \
    && chmod +x "/baselayout/usr/local/bin/go-replace-$dpkgArch" \
        && ln -s /baselayout/usr/local/bin/go-replace /usr/local/bin/ \
        ## install gosu
    && export dpkgArch=$(dpkg --print-architecture | awk -F- '{ print $NF }'); \
        wget -O "/baselayout/sbin/gosu" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch"; \
        wget -O "/baselayout/sbin/gosu.asc" "https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch.asc"; \
    GNUPGHOME="$(mktemp -d)"; \
        gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
        gpg --batch --verify /baselayout/sbin/gosu.asc "/baselayout/sbin/gosu"; \
        rm -rf "$GNUPGHOME"; \
        chmod +x "/baselayout/sbin/gosu";
