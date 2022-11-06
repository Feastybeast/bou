""" bou.migration.errors """

from bou.errors import BouError


class MigrationError(BouError):
    """ thrown from a bad upgrade() or downgrade() call. """
    pass
