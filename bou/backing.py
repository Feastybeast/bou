""" bou.backing
    ~~~
    A bit of support code to locate where migrations are.
"""

import collections
import enum
import importlib
import logging
import os
import sqlite3
import sys

from bou.constants import INPUT, OUTPUT, TYPE
from bou import BouError


def create(database):
    """ Create an empty sqlite database, ready for migrations.

    :param database: location to store the database at.
    :type database: click.Path
    """
    try:
        conn = sqlite3.connect(database)

        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE "_bou" (
                "id"    INTEGER,
                "migration" INTEGER NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
        """)

        cur.execute("""
            INSERT INTO _bou (migration) VALUES (0);
        """)

        conn.commit()
        conn.close()

    except sqlite3.Error:
        raise BackingError()


def location(migrations):
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


def module(spec):
    """ Returns the module at :spec:

    @see Issue #2

    :param spec: to load.
    :type spec: str
    """
    cwd = os.getcwd()

    if cwd not in sys.path:
        sys.path.append(cwd)

    return importlib.import_module(spec)


def open(database):
    """ open a :database: to interact with.

    :param database: path to open.
    :type database: click.Path
    :raises BackingError: if the database doesn't exist.
    :returns: a sqlite3.Connection
    """
    if not os.path.isfile(database):
        raise BackingError()

    return sqlite3.connect(database)


def version(database):
    """ Returns the current :database: version.

    :param database: path to open.
    :type database: click.Path
    """
    conn = open(database)

    try:
        with conn:
            curr = conn.cursor()
            smt = curr.execute("""
                SELECT migration
                FROM _bou
                ORDER BY id
                LIMIT 1
            """)
            return smt.fetchone()[0]

    except (BackingError, sqlite3.OperationalError, TypeError):
        raise UnversionedError()

    finally:
        conn.close()


class BackingError(BouError):
    """ Raised when backing can't be found """
    pass


class UnversionedError(BackingError):
    """ Not managed by bou """
    pass


class LocationType(enum.Enum):
    FILESYSTEM = 0
    PACKAGE = 1


Location = collections.namedtuple('Location', [INPUT, OUTPUT, TYPE])
