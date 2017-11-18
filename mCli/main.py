from __future__ import unicode_literals
import os
import sys
from six import text_type
from libs.shell import Shell

def main():
    argv = sys.argv[1:]
    cpath = "mCli/commands"
    cprefix = "commands."
    cli = Shell(appname="suresh-cli",symbol="#",cmdpath=cpath,cmdprefix=cprefix)
    cli()
    print "exiting"

if __name__ == "__main__":
    main()        