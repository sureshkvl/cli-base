from commands.base import Command


class exit(Command):
    description = "Exit from the CLI"
    details = '''
    Exit from the CLI
    Arguments: None
    '''

    def __call__(self, args):
        raise EOFError


class add(Command):
    description = "Adds two integer numbers"
    details = '''
    Adds two integer numbers and return the result.
    Args: a  b
    type: interger
    return: result
    Example:  add 10 20
    '''

    def __call__(self, args):
        return "Hello Command Returned"


class test(Command):
    description = "Test command"
    details = '''
    Add two numbers
    Args: a  b
    type: interger
    return: result
    Example:   add 10 20
    '''
    def __call__(self, args):
        return "Test Command Executed"
