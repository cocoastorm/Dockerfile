#!/usr/bin/env bash
set -e

echo 'building webdevops/toolbox'
docker build -t webdevops/toolbox:latest -f ./docker/toolbox/latest/Dockerfile .

echo 'building webdevops/php:8.2-alpine'
docker build -t webdevops/php:8.2-alpine -f ./docker/php/8.2-alpine/Dockerfile ./docker/php/8.2-alpine
docker tag webdevops/php:8.2-alpine ghcr.io/cocoastorm/webdevops/php:8.2-alpine

echo 'building webdevops/php-nginx:8.2-alpine'
docker build -t webdevops/php-nginx:8.2-alpine -f ./docker/php-nginx/8.2-alpine/Dockerfile ./docker/php-nginx/8.2-alpine
docker tag webdevops/php-nginx:8.2-alpine ghcr.io/cocoastorm/webdevops/php-nginx:8.2-alpine

# echo 'building webdevops/php-nginx-dev:8.2-alpine'
# docker build -t webdevops/php-nginx-dev:8.2-alpine -f ./docker/php-nginx-dev/8.2-alpine/Dockerfile ./docker/php-nginx-dev/8.2-alpine
# docker tag webdevops/php-nginx-dev:8.2-alpine ghcr.io/cocoastorm/webdevops/php-nginx-dev:8.2-alpine
