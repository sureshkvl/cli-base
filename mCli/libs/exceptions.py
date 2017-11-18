from __future__ import unicode_literals

from six import text_type

from gevent import GreenletExit


class CommandNotFound(Exception):
    pass


class CommandError(Exception):
    pass


class CommandInvalid(Exception):
    pass


class Exists(GreenletExit):

    def __init__(self, resources=None):
        self.resources = []
        if resources is not None:
            self.resources = resources

    @property
    def _paths(self):
        return ", ".join([text_type(c.path) for c in self.resources])

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__,
                           ", ".join([repr(r) for r in self.resources]))
