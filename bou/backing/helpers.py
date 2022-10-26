""" bou.backing.helpers
    ~~~
    Utility methods and behaviors to assist backing operations.
"""

from contextlib import contextmanager
import collections
import enum
import importlib
import logging
import os
import pathlib
import sqlite3
import sys
import types

from bou.constants import INPUT, OUTPUT, TYPE


@contextmanager
def fetch(database: pathlib.Path) -> sqlite3.Connection:
    """ Fetches :database:, and ensures a tidy closure.

    :param database: path to open.

    :returns: the database connection.
    """
    try:
        conn = open(database)
        yield conn
    finally:
        conn.close()


def location(migrations):
    ## IMPROVE THIS. Too many abstractions.
    """ Returns the filesystem location of :migrations:

    :param migrations: python package or directory to consider.
    :type migrations: str
    :returns: Location
    """
    fspath = os.path.abspath(migrations)

    if os.path.exists(fspath):
        logging.debug(f'Migrations path located at "{fspath}"')
        return Location(migrations, fspath, LocationType.FILESYSTEM)

    try:
        m = module(migrations)
        logging.debug(f'Migrations package located at "{migrations}"')
        return Location(migrations, m.__path__.pop(), LocationType.PACKAGE)

    except (ImportError, TypeError, ModuleNotFoundError):
        raise BackingError(
            f'Fully qualify or verify the existence of package "{migrations}".'
        )

    raise BackingError(f'Migrations not located at "{migrations}".')


def module(spec) -> types.ModuleType:
    """ Returns the module at :spec:

    @see Issue #2

    :param spec: to load.
    :type spec: str
    """
    cwd = os.getcwd()

    if cwd not in sys.path:
        sys.path.append(cwd)

    return importlib.import_module(spec)


class LocationType(enum.Enum):
    FILESYSTEM = 0
    PACKAGE = 1


Location = collections.namedtuple('Location', [INPUT, OUTPUT, TYPE])