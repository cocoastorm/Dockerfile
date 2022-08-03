#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
from cleo import Output
from webdevops import DockerfileUtility
from webdevops.command import BaseCommand

class GenerateGHActionMatrixCommand(BaseCommand):
    """
    Generate Github Actions template

    generate:gh-action-matrix
        {docker images?*         : Docker images (whitelist)}
        {--whitelist=?*          : image/tag whitelist }
        {--blacklist=?*          : image/tag blacklist }
    """

    image_user = ''
    image_prefix = ''
    dockerfile_path = ''

    def run_task(self, configuration):
        image_user = configuration.get('docker.imageUser')
        image_prefix = configuration.get('docker.imagePrefix')
        template_path = os.path.join(configuration.get('templatePath'), 'Github')
        dockerfile_path = configuration.get('dockerPath')

        whitelist = self.get_whitelist()
        blacklist = self.get_blacklist()

        self.image_user = image_user
        self.image_prefix = image_prefix
        self.dockerfile_path = dockerfile_path

        if Output.VERBOSITY_VERBOSE <= self.output.get_verbosity():
            self.line('<info>-> </info><comment>image prefix</comment> : %s' % image_prefix)
            self.line('<info>-> </info><comment>docker path</comment> : %s' % dockerfile_path)
            self.line('<info>-> </info><comment>template path </comment> : %s' % template_path)

            if whitelist:
                self.line('<info>-> </info><comment>whitelist </comment> :')
                for crit in whitelist:
                    self.line("\t * %s" % crit)

            if blacklist:
                self.line('<info>-> </info><comment>blacklist </comment> :')
                for crit in blacklist:
                    self.line("\t * %s" % crit)

        # dockerfiles = DockerfileUtility.find_file_in_path(
        #     dockerfile_path=dockerfile_path,
        #     filename="Dockerfile.jinja2",
        #     whitelist=whitelist, blacklist=blacklist,
        # )

        user_image_prefix = f"{image_user}/{image_prefix}" if image_user else image_prefix

        dockerfiles = DockerfileUtility.find_dockerfiles_in_path(
            base_path=self.configuration.get('dockerPath'),
            path_regex=self.configuration.get('docker.pathRegex'),
            image_prefix=user_image_prefix,
            whitelist=whitelist, blacklist=blacklist,
        )

        dockerfile_blocks = [self.process_dockerfile(file) for file in dockerfiles]

        base_img_blocks = []
        needs_dep_img_blocks = []

        for block in dockerfile_blocks:
            block_input = block['input']
            dockerfile_input = os.path.splitext(block_input)[0]

            from_img = DockerfileUtility.parse_dockerfile_from_statement(dockerfile_input)

            if image_prefix in from_img:
                needs_dep_img_blocks.append(block)
            else:
                base_img_blocks.append(block)

        # base images
        base_images = []
        for base_img in base_img_blocks:
            base_images.append(base_img)

            # toolbox should be first :tm:
            if "toolbox" in base_img["name"]:
                base_images.insert(0, base_images.pop(base_images.index(base_img)))

        # images with parent image from "webdevops"
        # /shrug

        output_path = os.path.split(dockerfile_path)[0]
        output_base_file = os.path.join(output_path, 'gh_matrix-base-images.json')
        output_multi_file = os.path.join(output_path, 'gh_matrix-multi-images.json')

        # matrix: base images
        self.line("\n\n")
        base_matrix = self.fmt_github_output("matrix-base", json.dumps(base_images))
        print(base_matrix)

        self.line("\n\n")
        multi_matrix = self.fmt_github_output("matrix-multi", json.dumps(needs_dep_img_blocks))
        print(multi_matrix)

        with open(output_base_file, 'w') as f:
            json.dump(base_images, f, indent=2)

        with open(output_multi_file, 'w') as fm:
            json.dump(needs_dep_img_blocks, fm, indent=2)

    def fmt_github_output(self, name, output):
        text = output
        
        text = text.replace("%", "%25")
        text = text.replace("\n", "%0A")
        text = text.replace("\r", "%0D")
        
        return "::set-output name=%s::%s" % (name, text)

    def fmt_tags(self, image, tag):
        if self.image_user:
            return f"{self.image_user}/{self.image_prefix}/{image}:{tag}"
        else:
            return f"{self.image_prefix}/{image}:{tag}"

    def process_dockerfile(self, dockerfile):
        input_file = dockerfile['abspath']
        output_file = os.path.split(input_file)[0]

        docker_image = os.path.basename(os.path.dirname(output_file))
        docker_tag = os.path.basename(output_file)

        context_dir = os.path.relpath(output_file, os.path.dirname(self.dockerfile_path))

        img = {
            'input': input_file,
            'name': f"{docker_image}:{docker_tag}",
            'context': context_dir,
            'tags': dockerfile['image']['fullname'],
        }

        if Output.VERBOSITY_NORMAL <= self.output.get_verbosity():
            self.line("<info>* </info><comment>Build block for </comment>%s" % img["name"])
            self.line("<info>  context_path: </info>%s" % context_dir)

        return img
