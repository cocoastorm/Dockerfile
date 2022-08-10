#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# (c) 2016 WebDevOps.io
#
# This file is part of Dockerfile Repository.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
from cleo import Output
from jinja2 import Environment, FileSystemLoader
from webdevops import DockerfileUtility
from webdevops.command import BaseCommand

class GenerateDockerfileCommand(BaseCommand):
    """
    Build Dockerfile containers

    generate:dockerfile
        {docker images?*         : Docker images (whitelist)}
        {--o|output              : output directory}
        {--whitelist=?*          : image/tag whitelist }
        {--blacklist=?*          : image/tag blacklist }
    """

    template = ''
    template_header = '{% extends "Dockerfile/layout.jinja2" %}\n{% block content %}'
    template_footer = '{% endblock %}'

    dockerfile_path = ''

    def run_task(self, configuration):
        template_path = configuration.get('templatePath')

        dockerfile_path = configuration.get('dockerPath')
        self.dockerfile_path = dockerfile_path

        output_dirpath = self.option("o")

        whitelist = self.get_whitelist()
        blacklist = self.get_blacklist()

        if Output.VERBOSITY_VERBOSE <= self.output.get_verbosity():
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

        self.template = Environment(
            autoescape=False,
            loader=FileSystemLoader([template_path]),
            trim_blocks=False
        )

        image_user = self.configuration.get('docker.imageUser')
        image_prefix = self.configuration.get('docker.imagePrefix')

        user_image_prefix = f"{image_user}/{image_prefix}" if image_user else image_prefix
        self.template.globals = {"user": user_image_prefix or 'webdevops'}

        if output_dirpath:
            os.makedirs(output_dirpath, exist_ok=True)

        for file in DockerfileUtility.find_file_in_path(dockerfile_path=dockerfile_path, filename="Dockerfile.jinja2", whitelist=whitelist, blacklist=blacklist):
                self.process_dockerfile(file, output=output_dirpath)

    def process_dockerfile(self, input_file, output=""):
        """
        :param input_file: Input File
        :type input_file: str
        """
        dockerfile = os.path.splitext(input_file)
        dockerfile = os.path.join(os.path.dirname(dockerfile[0]), os.path.basename(dockerfile[0]))

        if not output: 
            output_file = dockerfile
        else:
            segment_name = os.path.relpath(dockerfile, self.dockerfile_path)
            output_file = os.path.join(output, segment_name)

        docker_image = os.path.basename(os.path.dirname(os.path.dirname(dockerfile)))
        docker_tag = os.path.basename(os.path.dirname(dockerfile))

        context = {
            'Dockerfile': {
                'image': docker_image,
                'tag': docker_tag
            }
        }

        if Output.VERBOSITY_NORMAL <= self.output.get_verbosity():
            self.line("<info>* </info><comment>Processing Dockerfile for </comment>%s:%s" % (docker_image,docker_tag))

        with open(input_file, 'r') as fileInput:
            template_content = fileInput.read()

            template_content = self.template_header + template_content + self.template_footer

            rendered_content = self.template.from_string(template_content).render(context)
            rendered_content = rendered_content.lstrip()

            with open(output_file, 'w') as file_output:
                file_output.write(rendered_content)
