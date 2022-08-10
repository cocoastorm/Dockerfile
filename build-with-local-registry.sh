#!/usr/bin/env bash

set -e

# start up a local registry via docker run
docker run --rm -d -p 5000:5000 --restart=always --name registry registry:2

# create and use a buildkit builder/runner for linux/amd64 and linux/arm64
{
    echo '# https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md'
    echo 'debug = true'
    echo ''
    echo '[registry."localhost:5000"]'
    echo '    http=true'
    echo '    insecure=true'
    echo ''
} | tee /tmp/buildkitd.toml

docker buildx create --name multiarch-builder --config /tmp/buildkitd.toml --use

# replace prefix in configuration file
sed -i 's/[[:space:]]imagePrefix:.*/ imagePrefix: localhost:5000/' ./conf/console.yml

# use python virtualenv to run 'console' and generate and provision dockerfiles
(
    source venv/bin/activate
    bin/console generate:dockerfile -o /tmp/webdevops
    bin/console generate:provision
)

build() {
    arg="$1"

    IFS=':' read -ra IMAGE <<< "$arg"

    name="${IMAGE[0]}"
    tag="${IMAGE[1]}"

    context_path="docker/${name}/${tag}"
    docker buildx build --platform="linux/amd64,linux/arm64" -t "$arg" "$context_path"
}

# build
builds=( "toolbox" "php:8.0" "php:8.0-alpine" "php-nginx:8.0" "php-nginx:8.0-alpine" )

for image in "${builds[@]}"; do
    build "$image"
done
