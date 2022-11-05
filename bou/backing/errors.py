""" bou.backing.errors """

from bou.errors import BouError


# Backing related errors
class BackingError(BouError):
    """ Raised when backing can't be found """
    pass


class BackingMissingError(BackingError):
    """ the .sqlite file is just missing. """
    pass


class BackingUnversionedError(BackingError):
    """ thrown when a database isn't managed by bou """
    pass
