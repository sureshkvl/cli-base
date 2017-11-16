from base import Command


class Exit(Command):
    description = "Exit from shell"

    def __call__(self):
        raise EOFError


class Hello(Command):
    description = "Hello command"

    def __call__(self):
        return "Hello Command Returned"


class Test(Command):
    description = "Test command"

    def __call__(self):
        return "Test Command Executed"