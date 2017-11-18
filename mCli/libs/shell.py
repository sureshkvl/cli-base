# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path
from six import text_type
from pygments.token import Token

from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.contrib.completers import WordCompleter

from utils import eventloop
from libs.style import default as default_style
from libs.cmdmanager import CommandManager


class Shell(object):
    description = "Run an interactive shell"

    def __init__(self, appname="M-Cli", symbol=">", cmdpath=None, cmdprefix=None):
        self.appname = appname
        self.symbol = symbol
        self.cmdpath = cmdpath
        self.cmdprefix = cmdprefix
        self.CMgr = CommandManager(path=self.cmdpath, prefix=self.cmdprefix)

    def __call__(self):
        def get_default_prompt_tokens(cli):
            return [
                (Token.Name, self.appname),
                (Token.Symbol, self.symbol)
                ]

        my_completer = WordCompleter(self.CMgr.list("*"))

        while True:
            try:
                action = prompt(get_prompt_tokens=get_default_prompt_tokens,
                                style=default_style,
                                completer=my_completer,
                                eventloop=eventloop()
                                )
            except (EOFError, KeyboardInterrupt):
                break
            try:
                print self.CMgr.execute(action)
            except (EOFError, KeyboardInterrupt):
                break


if __name__ == "__main__":
    a = Shell()
    a()
