""" bou.actions.migrate """

import bou
import bou.constants
import enum


def migrate(database, migrations, direction):
    """ Normalized migration behaviors for bou.

    :param database: to act upon.
    :type database: sqlite.Connection
    :param migrations: package or folder to act against.
    :type migrations: os.Path
    :param direction: of the migration.
    :type direction: Direction
    :param stopping: at a given migration timestamp, or -1.
    :type stopping: int
    """
    try:
        for each in migrations:
            each[direction](database)

    except Exception:
        raise MigrationError(each.VERSION)


class Direction(enum.Enum):
    UPGRADE = bou.constants.UPGRADE
    DOWNGRADE = bou.constants.DOWNGRADE


class MigrationError(bou.BouError):
    """ thrown when a module's method failed. """
    pass
