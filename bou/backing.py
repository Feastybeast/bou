""" bou.backing
    ~~~
    A bit of support code to locate where migrations are.
"""

import importlib
import logging
import os
import sqlite3

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

        conn.commit()
        conn.close()

    except sqlite3.Error:
        raise BackingError()


def location(migrations):
    """ Does :resource: exist as a package or filesystem location?

    :param migrations: of the given parameter.
    :type migrations: any
    """
    fspath = os.path.abspath(migrations)

    if os.path.exists(fspath):
        logging.debug(f'Migrations path located at "{fspath}"')
        return fspath

    try:
        importlib.import_module(migrations)
        logging.debug(f'Migrations package located at "{migrations}"')
        return migrations

    except (TypeError, ModuleNotFoundError):
        raise BackingError(
            f'Fully qualify or verify the existence of package "{migrations}".'
        )

    raise BackingError(f'Migrations not located at "{migrations}".')


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
