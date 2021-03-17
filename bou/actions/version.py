""" bou.actions.version
    ~~~
    List the bou migration value of the given database.
"""

import sqlite3

import bou.backing


def version(database):
    """ """
    conn = bou.backing.open(database)

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

    except (sqlite3.OperationalError, TypeError):
        raise UnversionedError()

    finally:
        conn.close()


class UnversionedError(bou.backing.BackingError):
    """ Not managed by bou """
    pass
