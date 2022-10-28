""" bou.backing.operations
    ~~~
    A bit of support code to locate where migrations are.

    # Make Bou migrate itself into existence.
"""


import pathlib

from bou.backing.helpers import fetch


def track(database: pathlib.Path):
    """ Create a migration-ready *database*.

    :param database: location to store the database at.
    """
    # See the template work. It's gonna dogfood itself into existence.


def version(database: pathlib.Path):
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
