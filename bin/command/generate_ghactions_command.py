#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pprint
from pathlib import Path
from cleo import Output
from jinja2 import Environment, FileSystemLoader
from webdevops import DockerfileUtility
from webdevops.command import BaseCommand

class GenerateGHActionsCommand(BaseCommand):
    """
    Generate Github Actions template

    generate:ghactions
        {docker images?*         : Docker images (whitelist)}
        {--whitelist=?*          : image/tag whitelist }
        {--blacklist=?*          : image/tag blacklist }
    """

    image_prefix = ''

    def run_task(self, configuration):
        self.image_prefix = configuration.get('docker.imagePrefix')
        template_path = os.path.join(configuration.get('templatePath'), 'Github')
        dockerfile_path = configuration.get('dockerPath')
        github_actions_path = configuration.get('githubActionsPath')
        github_action_file = os.path.join(github_actions_path, 'docker.yml')

        whitelist = self.get_whitelist()
        blacklist = self.get_blacklist()

        if Output.VERBOSITY_VERBOSE <= self.output.get_verbosity():
            self.line('<info>-> </info><comment>image prefix</comment> : %s' % self.image_prefix)
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

        env = Environment(
            autoescape=False,
            loader=FileSystemLoader([template_path]),
            trim_blocks=False
        )

        dockerfiles = DockerfileUtility.find_file_in_path(
            dockerfile_path=dockerfile_path,
            filename="Dockerfile.jinja2",
            whitelist=whitelist, blacklist=blacklist,
        )

        dockerfile_blocks = [self.process_dockerfile(file) for file in dockerfiles]

        template = env.get_template('docker_action.jinja2')
        rendered_content = template.render(dockerfiles=dockerfile_blocks)

        Path(github_actions_path).mkdir(parents=True, exist_ok=True)

        with open(github_action_file, 'w') as file_output:
            file_output.write(rendered_content)

        self.line('written to %s' % github_action_file)

    def process_dockerfile(self, input_file):
        """
        :param input_file: Input File
        :type input_file: str
        """

        output_file = os.path.splitext(input_file)
        output_file = os.path.join(os.path.dirname(output_file[0]), os.path.basename(output_file[0]))

        docker_image = os.path.basename(os.path.dirname(os.path.dirname(output_file)))
        docker_tag = os.path.basename(os.path.dirname(output_file))

        context_dir = os.path.split(output_file)[0]

        img = {
            'name': f"{docker_image}:{docker_tag}",
            'context': context_dir,
            'tags': f"{self.image_prefix}/{docker_image}:{docker_tag}"
        }

        if Output.VERBOSITY_NORMAL <= self.output.get_verbosity():
            self.line("<info>* </info><comment>Build block for </comment>%s" % img["name"])

        return img
