# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
#import inspect
import argparse
import abc
#from fnmatch import fnmatch
#from collections import OrderedDict
from six import add_metaclass, text_type
import argparse

from utils import get_resource_classes

@add_metaclass(abc.ABCMeta)
class CommandManager(object):
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

    def list(self):
        # return the commands name
        return self.commands

    def execute(self, cmdname):
        # get the command object and execute call function
        if cmdname == "help" or cmdname == "?":
            return self.list()
        for c in self.cmdcls:
            if cmdname == c.__name__:
                return c()()
        return "Error : Command Not Found"



if __name__ == "__main__":
    cm = CommandManager()
    cm.list()
    print cm.execute("Help")
    #print get_resource_classes()
