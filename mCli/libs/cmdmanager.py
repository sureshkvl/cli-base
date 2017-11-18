# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import argparse
import abc
from six import add_metaclass, text_type
import argparse
import re

from utils import get_resource_classes
from utils import Singleton


@add_metaclass(abc.ABCMeta)
class CommandManager(Singleton, object):
    """Base class for commands
    """
    description = ""

    """Command aliases"""
    _options = None
    _args = None

    def __init__(self):
        # Load the Commands Subclasses, and Get the names.
        self.cmdcls = get_resource_classes()
        self.commands = [c.__name__ for c in self.cmdcls]

    def list(self, filter="*"):
        # return the commands name
        res = []
        if filter == "*":
            return self.commands
        else:
            for cmd in self.commands:
                match = re.match(r'(%s)' % filter, cmd,re.M|re.I)
                if match:
                    res.append(cmd)
            return res
    def isequal(self, a, b):
        return a.upper() == b.upper()

    def execute(self, cmdname):
        # get the command object and execute call function
        for c in self.cmdcls:
            if self.isequal(str(cmdname), str(c.__name__)):
                return c()()
        return "Error : Command Not Found"



if __name__ == "__main__":
    cm = CommandManager()
    print cm.list("*")
    print cm.list("H")
    print cm.list("He")
    print cm.list("Pi")
    #print cm.execute("Help")
    #print get_resource_classes()
