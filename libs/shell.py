# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path
from six import text_type
from pygments.token import Token

from prompt_toolkit import prompt
# from prompt_toolkit.history import FileHistory
# from prompt_toolkit.key_binding.manager import KeyBindingManager
#from exceptions import CommandError, CommandNotFound, Exists
#from command import Command
from utils import eventloop
from style import default as default_style
# from ..manager import CommandManager
from cmdmanager import CommandManager
APP_NAME = "Mini-CLI"
MODE_NAME = "conf"


class Shell(object):
    description = "Run an interactive shell"

    def __call__(self):

        def get_default_prompt_tokens(cli):
            return [
                (Token.Name, APP_NAME or 'CLI'),
                (Token.Symbol, '>')
                ]

        def get_mode_promt_tokens(cli):
            return [
                (Token.Name, APP_NAME or 'CLI'),
                (Token.Symbol, '>'),
                (Token.Mode, MODE_NAME or 'Config'),
                (Token.ModeSymbol, '#')
                ]

        CMgr = CommandManager()

        while True:
            try:
                action = prompt(get_prompt_tokens=get_default_prompt_tokens,
                                style=default_style,
                                eventloop=eventloop()
                                )
            except (EOFError, KeyboardInterrupt):
                break
            print CMgr.execute(action)



if __name__ == "__main__":
    #cm = CommandManager()
    #print cm.list()
    #print cm.execute("Help")
    a = Shell()  
    a()