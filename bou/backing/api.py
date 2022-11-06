""" bou.backing.helpers
    ~~~
    A bit of support code to locate where migrations are.

    # Make Bou migrate itself into existence.
"""


import uuid

import bou.backing.errors
from bou.backing.helpers import fetch
from bou.types import Database


def exists(database: Database):
    """ Because sqlite will implicitly operate on anything, bou needs
        to halt some operations on non-existant databases for user clarity.

    :param database: to check the existence of.
    """
    if not database.exists():
        raise bou.backing.errors.BackingMissingError()


def migrations_for(database: Database) -> (str, uuid.uuid4):
    """ Locate :database:'s migration directory as an absolute path and uuid.

    :param database: to open.

    :returns: a pathlike object to the Migrations, and
    """
    with fetch(database) as conn:
        curr = conn.cursor()

        smt = curr.execute("""
            SELECT location, uuid
            FROM _boufile
            LIMIT 1
        """)

        location, uuid = smt.fetchone()

        return (location, uuid)


def track(database: Database, migrations: MigrationDir):
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
