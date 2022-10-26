""" bou.backing
    ~~~
    A bit of support code to locate where migrations are.
"""


import pathlib

from bou.backing.helpers import fetch
from bou.backing.errors import UnversionedError


def create(database: pathlib.Path):
    """ Create a migration-ready *database*.

    :param database: location to store the database at.
    """
    with fetch(database) as conn:
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


def version(database: pathlib.Path):
    """ Returns the current :database: version.

    :param database: path to open.
    :type database: click.Path
    """
    try:
        with fetch(database) as conn:
            curr = conn.cursor()

            smt = curr.execute("""
                SELECT migration
                FROM _bou
                ORDER BY id
                LIMIT 1
            """)

            return smt.fetchone()[0]
    except ():
        raise UnversionedError()