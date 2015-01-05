#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


class SystemCommands(object):

    def __init__(self, command):
        self.command = command

    def execute_command(self):
        if self.command == "get_hostname":
            s_out = subprocess.Popen(['hostname'], stdout=subprocess.PIPE)
            output = s_out.communicate()[0]
        elif self.command == "get_kernel_version":
            pass

        print output