""" bou.acts.migrate.commands
    ~~~
    Migrates a database. Hooray.
"""

import pathlib

from bou.backing.helpers import fetch
from bou.lib.errors import MigrationError
from bou.lib.types import Migration, Direction


def dry_run(database: pathlib.Path, migrations: Migration, dir: Direction):
    """ Normalized migration behaviors for bou.

    :param database: to act upon.
    :param migrations: steps to process.
    :param direction: of the migration.
    """
    # Create a trial database.
    # migrate() that.
    # Throw it away if it succeeded.


def migrate(database: pathlib.Path, migrations: Migration, dir: Direction):
    """ Normalized migration behaviors for bou.

    :param database: to act upon.
    :param migrations: steps to process.
    :param direction: of the migration.
    """
    with fetch(database) as conn:
        try:
            for each in migrations:
                each[dir](database)

        except Exception:
            conn.rollback()
            raise MigrationError(each.VERSION)
