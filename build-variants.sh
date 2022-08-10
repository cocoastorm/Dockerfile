#!/usr/bin/env bash
set -e

# echo 'setting up buildx'
# docker run --rm --privileged tonistiigi/binfmt:latest --install all
# docker buildx create --driver docker-container --use

echo 'building webdevops/php-nginx'
docker buildx build \
    --progress plain \
    --platform="linux/amd64,linux/arm64" \
    -t ghcr.io/cocoastorm/webdevops/php-nginx:8.0 \
    ./docker/php-nginx/8.0/
