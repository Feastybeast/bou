""" bou.version.api
    ~~~
    List the bou migration value of the given database.
"""

import bou.backing
import bou.errors as errors
from bou.types import Database


def version(database: Database) -> int:
    """ Get the current migration version from :database:

    :param database: to query.
    """
    try:
        return bou.backing.version(database)
    except ():
        raise errors.UnversionedError()
