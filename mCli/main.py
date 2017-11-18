from __future__ import unicode_literals
import os
import sys
#import argparse
#import logging
#import logging.config
from six import text_type
from libs.shell import Shell

def main():
    argv = sys.argv[1:]
    cli = Shell()
    cli()
    print "exiting"

if __name__ == "__main__":
    main()        