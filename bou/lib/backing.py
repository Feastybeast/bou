""" bou.lib.backing
    ~~~
    A bit of support code to locate where migrations are.

    # Make Bou migrate itself into existence.
"""

from contextlib import contextmanager

import sqlite3

from bou.lib.types import Database


@contextmanager
def fetch(database: Database) -> sqlite3.Connection:
    """ Fetches :database: and ensures a tidy closure.

    :param database: path to open.

    :returns: the database connection.
    """
    caught_exception = None

    try:
        conn = open(database)
        yield conn

    except sqlite3.Exception as e:
        caught_exception = e
        conn.rollback()

    finally:
        conn.close()

    if caught_exception:
        raise caught_exception


def migrations_for(database: Database):
    """ Locate :database:'s migration directory as an absolute path and uuid.

    :param database: to open.
    """
    with fetch(database) as conn:
        curr = conn.cursor()

        smt = curr.execute("""
            SELECT location, uuid
            FROM _boufile
            LIMIT 1
        """)

        return smt.fetchone()[0]


def track(database: Database):
    """ Create a migration-ready *database*.

    :param database: location to store the database at.
    """
    # See the template work. It's gonna dogfood itself into existence.


def version(database: Database):
    """ Returns the current :database: version.

    :param database: path to open.
    :type database: click.Path
    """
    with fetch(database) as conn:
        curr = conn.cursor()

        smt = curr.execute("""
            SELECT migration
            FROM _bou
            ORDER BY id
            LIMIT 1
        """)

        return smt.fetchone()[0]
