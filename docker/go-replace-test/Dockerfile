FROM --platform=$BUILDPLATFORM tux:5000/cocoastorm/webdevops/toolbox:alpine AS base

FROM alpine
ARG TARGETARCH
COPY --from=base /baselayout /
RUN apk add --no-cache dpkg; \
    go-replace --version && echo "$TARGETARCH"
