""" bou.track.api
    ~~~
    Insert bou behaviors into the :database:.
"""

import bou.backing.api

from bou.types import Database, MigrationDir


def filesystem(database: MigrationDir):
    """ [Creates and] adds bou management to :database:

    :param database: path on the filesystem.
    """
    bou.boufile.api.create(database)


def database(database: Database, migrations: MigrationDir):
    """ [Creates, if needed] :database: and informs bou about :migrations:

    :param database: location on the filesystem.
    :param migrations: directory on the filesystem.
    """
    bou.backing.api.track(database, migrations)


def validate(database: Database, migrations: MigrationDir):
    """ """
    bou.backing.api.migrations_for(database)
