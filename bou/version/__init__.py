""" bou.actions.version
    ~~~
    List the bou migration value of the given database.
"""

import pathlib

import bou.backing.operations as operations
import bou.backing.errors as errors


def version(database: pathlib.Path) -> int:
    """ Get the current migration version from :database:

    :param database: to query.
    """
    try:
        return operations.version(database)
    except ():
        raise errors.UnversionedError()
