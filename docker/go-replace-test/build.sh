#!/bin/sh
set -ex

docker buildx build -t tux:5000/cocoastorm/webdevops/base-layout:latest ./docker/base-layout/latest --push

docker buildx build --platform=linux/arm64,linux/amd64 -t tux:5000/cocoastorm/webdevops/toolbox:alpine ./docker/toolbox/alpine --push

docker buildx build --progress plain --platform=linux/arm64,linux/amd64 -t tux:5000/cocoastorm/webdevops/go-replace-test ./docker/go-replace-test --push
