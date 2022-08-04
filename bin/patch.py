#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def find_append_to_file(filename, find, insert):
    """find and append text in a file."""
    with open(filename, 'r') as in_file:
        buf = in_file.readlines()

    with open(filename, 'w') as out_file:
        for line in buf:
            out_file.write(line)

            if find in line:
                out_file.write("\n")
                out_file.write(insert + "\n")

if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.dirname(script_path)
    dockerfiles_path = os.path.join(root_path, 'docker')

    dockerfiles = []

    for root, dirs, files in os.walk(dockerfiles_path):
        for file in files:
            if file.endswith(".jinja2"):
                dockerfiles.append(os.path.join(root, file))

    for dockerfile in dockerfiles:
        find_pattern = "docker.from"
        insert_line = "{{ docker.platformArgs() }}"

        find_append_to_file(dockerfile, find_pattern, insert_line)
