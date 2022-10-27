""" bou.backing.helpers
    ~~~
    Utility methods and behaviors to assist backing operations.
"""

from contextlib import contextmanager

import pathlib
import sqlite3


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
