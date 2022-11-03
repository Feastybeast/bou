""" bou.acts.migrate.commands
    ~~~
    Migrates a database. Hooray.
"""

from bou.backing.helpers import fetch
from bou.lib.errors import MigrationError
from bou.lib.types import Migration

from bou.lib.types import Database


def dry_run(migrations: Migration, database: Database, version):
    """ Normalized migration behaviors for bou.

    :param database: to act upon.
    :param migrations: steps to process.
    :param version: to stop at.
    """
    # Create a trial database.
    # migrate() that.
    # Throw it away if it succeeded.


def migrate(migrations: Migration, database: Database, version):
    """ Normalized migration behaviors for bou.

    :param database: to act upon.
    :param migrations: steps to process.
    :param version: to stop at.
    """
    with fetch(database) as conn:
        try:
            for each in migrations:
                each[dir](database)

        except Exception:
            conn.rollback()
            raise MigrationError(each.VERSION)
