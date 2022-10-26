""" bou.backing.errors
    ~~~
    Errors directly relating to database operations.
"""

from bou import BouError


class BackingError(BouError):
    """ Raised when backing can't be found """
    pass


class UnversionedError(BackingError):
    """ Not managed by bou """
    pass
