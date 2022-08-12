#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def should_be_ignored(name, ignore_list):
    for ignore_term in ignore_list:
        if ignore_term in name:
            return True
    return False

class MatrixBuilder():
    cache = {}

    base_images = []
    graph = {}

    image_prefix = ''
    dockerfile_blocks = []

    # ignore these for now
    ignore = [
        'php-official',
        'toolbox',
    ]

    def __init__(self, dockerfile_blocks, my_image_prefix="webdevops"):
        self.image_prefix = my_image_prefix
        self.dockerfile_blocks = dockerfile_blocks

    def __add_to_cache(self, dockerfile_block):
        image_name = dockerfile_block['image']['fullname']
        self.cache[image_name] = dockerfile_block

    def __add_to_base_images_list(self, dockerfile_block):
        dockerfile_image = dockerfile_block['image']
        image_from = dockerfile_image['from']

        if self.image_prefix in image_from and should_be_ignored(image_from, self.ignore):
            self.base_images.append(dockerfile_block)

    def __add_to_dependency_graph(self, dockerfile_block):
        dockerfile_image = dockerfile_block['image']

        image_name = dockerfile_image['fullname']
        image_from = dockerfile_image['from']
        image_multistage = dockerfile_image['multiStageImages']

        if self.image_prefix not in image_from:
            return

        if should_be_ignored(image_from, self.ignore):
            return

        image_deps = [dockerfile_image['from']]

        if image_multistage:
            image_deps.extend(image_multistage)

        self.__add_to_cache(dockerfile_block)

        for image_dep in image_deps:
            if should_be_ignored(image_dep, self.ignore):
                continue

            graph_list = self.graph.get(image_dep)

            if graph_list:
                graph_list.extend([image_name])
                self.graph[image_dep] = graph_list
            else:
                self.graph[image_dep] = [image_name]

    def __build_dependency_graph(self):
        for dockerfile_block in self.dockerfile_blocks:
            self.__add_to_base_images_list(dockerfile_block)
            self.__add_to_dependency_graph(dockerfile_block)

    def __ignore_base_images(self):
        for base_dockerfile_block in self.base_images:
            # https://stackoverflow.com/a/11277439/5332177
            self.graph.pop(base_dockerfile_block['image']['fullname'], None)

    def build(self):
        self.__build_dependency_graph()
        self.__ignore_base_images()

    def get_base_images(self):
        return self.base_images

    def get_multiservice_images(self):
        multiservice_images_list = self.graph.keys()
        return [self.cache[name] for name in multiservice_images_list]

    def get_development_images(self):
        dependent_images_list = []

        for images in self.graph.values():
            dependent_images_list.extend(images)

        return [self.cache[name] for name in dependent_images_list]

    def printGraph(self, line):
        line("base images")
        line(json.dumps(self.base_images))

        line("")
        line("multiservice images:")
        line(json.dumps(self.get_multiservice_images()))

        line("")
        line("dev images:")
        line(json.dumps(self.get_development_images()))
