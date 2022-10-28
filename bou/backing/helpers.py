""" bou.backing.helpers
    ~~~
    Utility methods and behaviors to assist backing operations.
"""

from contextlib import contextmanager

import pathlib
import sqlite3


@contextmanager
def fetch(database: pathlib.Path) -> sqlite3.Connection:
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
