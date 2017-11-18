# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prompt_toolkit.shortcuts import prompt, create_eventloop

import gevent


import copy
import functools
import importlib
import logging
import os
import pkgutil
import re

from commands.base import Command


def eventloop():
    # Allow to keep gevent greenlets running
    # while waiting for some input on the cli
    def inputhook(context):
        while not context.input_is_ready():
            gevent.sleep(0.1)

    return create_eventloop(inputhook=inputhook)


def get_resource_classes():

    iter_modules = pkgutil.iter_modules(
        [os.path.join(os.path.dirname(__file__), 'commands')],
        prefix='commands.'
    )
    for (_, name, ispkg) in iter_modules:
        if not ispkg:
            importlib.import_module(name)

    all_classes = Command.__subclasses__()
    return all_classes


#https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance



if __name__ == "__main__":
    print get_resource_classes()
