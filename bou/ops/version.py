""" bou.acts.version
    ~~~
    List the bou migration value of the given database.
"""

import bou.lib.backing
import bou.lib.errors as errors
from bou.lib.types import Database


def version(database: Database) -> int:
    """ Get the current migration version from :database:

    :param database: to query.
    """
    try:
        return bou.lib.backing.version(database)
    except ():
        raise errors.UnversionedError()
