""" bou.backing.helpers """

from contextlib import contextmanager
import sqlite3

import bou.backing.errors
from bou.types import Database


@contextmanager
def fetch(database: Database) -> sqlite3.Connection:
    """ Fetches :database: and ensures a tidy closure.

    :param database: path to open.

    :returns: the database connection.
    """
    caught_exception = None

    try:
        conn = sqlite3.connect(database)
        yield conn

    except sqlite3.OperationalError:
        raise bou.backing.errors.BackingUnversionedError()

    except Exception as e:
        caught_exception = e
        conn.rollback()

    finally:
        try:
            conn.close()
        except UnboundLocalError:  # because it never existed! GASP.
            pass

    if caught_exception:
        raise caught_exception
