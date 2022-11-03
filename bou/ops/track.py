""" bou.ops.track
    ~~~
    Insert bou behaviors into the :database:.
"""

import bou.backing.operations as operations

from bou.lib.types import Database


def track(database: Database):
    """ [Creates and] adds bou management to :database:

    :param database: path on the filesystem.
    """
    operations.track(database)
