""" bou.boufile.errors """

from bou.errors import BouError


class BoufileError(BouError):
    """ raised for Boufile problems """
    pass


class BoufileCreationError(BoufileError):
    """ bou.boufile.api.create() failed. """
    pass


class BoufileInvalidError(BoufileError):
    """ Whatever it is, it's not a Boufile """
    pass


class MigrationError(BoufileError):
    """ thrown when a module's method failed. """
    pass


class MigrationsSourceError(BouError):
    """ thrown when a migrations source can't be located """
    pass
