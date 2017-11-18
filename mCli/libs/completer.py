"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from cmdmanager import CommandManager
from six import add_metaclass, text_type
import abc
from utils import Singleton


@add_metaclass(abc.ABCMeta)
class ShellCompleter(Singleton, Completer):

    def __init__(self):
        self.mgr = CommandManager()

    def get_completions(self, document, complete_event):
        result = self.mgr.list(document)
        for i in result:
            yield Completion(i)

"""