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

    image_prefix = ''
    dockerfile_path = ''

    def run_task(self, configuration):
        image_prefix = configuration.get('docker.imageUser') or configuration.get('docker.imagePrefix')
        template_path = os.path.join(configuration.get('templatePath'), 'Github')
        dockerfile_path = configuration.get('dockerPath')
        github_actions_path = configuration.get('githubActionsPath')
        github_action_file = os.path.join(github_actions_path, 'docker.yml')

        whitelist = self.get_whitelist()
        blacklist = self.get_blacklist()

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

        dockerfiles = DockerfileUtility.find_file_in_path(
            dockerfile_path=dockerfile_path,
            filename="Dockerfile.jinja2",
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
                block['needs_parent'] = True
                needs_dep_img_blocks.append(block)
            else:
                base_img_blocks.append(block)

        # base images
        base_images = []
        for base_img in base_img_blocks:
            base_img['needs_parent'] = False

            base_images.append(base_img)

            # toolbox should be first :tm:
            if "toolbox" in base_img["name"]:
                base_images.insert(0, base_images.pop(base_images.index(base_img)))

        # images with parent image from "webdevops"
        # /shrug

        output_path = os.path.split(dockerfile_path)[0]
        output_base_file = os.path.join(output_path, 'gh_matrix-base-images.json')
        output_multi_file = os.path.join(output_path, 'gh_matrix-multi-images.json')

        self.line("\n\n")
        print("::set-output name=matrix-base::%s" % json.dumps(base_images, indent=2))
        self.line("\n\n")
        print("::set-output name=matrix-multi::%s" % json.dumps(needs_dep_img_blocks, indent=2))

        with open(output_base_file, 'w') as f:
            json.dump(base_images, f, indent=2)

        with open(output_multi_file, 'w') as fm:
            json.dump(needs_dep_img_blocks, fm, indent=2)

    def process_dockerfile(self, input_file):
        """
        :param input_file: Input File
        :type input_file: str
        """

        output_file = os.path.split(input_file)[0]

        docker_image = os.path.basename(os.path.dirname(output_file))
        docker_tag = os.path.basename(output_file)

        context_dir = os.path.relpath(output_file, os.path.dirname(self.dockerfile_path))

        img = {
            'input': input_file,
            'name': f"{docker_image}:{docker_tag}",
            'context': context_dir,
            'tags': f"{self.image_prefix}/{docker_image}:{docker_tag}"
        }

        if Output.VERBOSITY_NORMAL <= self.output.get_verbosity():
            self.line("<info>* </info><comment>Build block for </comment>%s" % img["name"])
            self.line("<info>  context_path: </info>%s" % context_dir)

        return img
