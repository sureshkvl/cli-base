# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path
from six import text_type
#from pygments.token import Token
from prompt_toolkit.token import Token
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from mCli.utils import eventloop
from mCli.libs.style import default as default_style
from mCli.libs.cmdmanager import CommandManager


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

        def get_bottom_toolbar_tokens(cli):
            return [(Token.Toolbar, ' This is a toolbar. ')]


        my_completer = WordCompleter(self.CMgr.list("*"))
        history = InMemoryHistory()
        while True:
            try:
                action = prompt(get_prompt_tokens=get_default_prompt_tokens,
                                get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
                                style=default_style,
                                completer=my_completer,
                                history=history,
                                auto_suggest=AutoSuggestFromHistory(),
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
