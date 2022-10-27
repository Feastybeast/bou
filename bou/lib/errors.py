""" bou.lib.errors """


class BouError(Exception):
    """ Root exception for the application """
    pass


class BackingError(BouError):
    """ Raised when backing can't be found """
    pass


class MigrationError(BouError):
    """ thrown when a module's method failed. """
    pass


class UnversionedError(BackingError):
    """ thrown when a database isn't managed by bou """
    pass
