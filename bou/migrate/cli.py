""" bou.migrate.cli
    ~~~
    module specific CLI behaviors.
"""

import math

import click

from bou.app.core import main
import bou.app.helpers as helpers
from bou.constants import KWARG_DATABASE
from bou.types import Database


@main.command(short_help='Migrate :database: to :version:')
@click.argument(KWARG_DATABASE, required=True, type=Database)
@click.argument('to_version', required=False, type=int)
def migrate(database: Database, to_version: int):
    """ Migrate :database: to :version: stored at :migrations:

    :param database: to migrate.
    :param version: to finish at.
    """
    import bou.migrate.api

    helpers.patch_sys_dot_path()
    bou.migrate.api.migrate(database, to_version or math.inf)
