""" bou.version.cli
    ~~~
    module specific CLI behaviors.
"""

import click

from bou.cli.main import main
from bou.constants import KWARG_DATABASE
from bou.types import Database


@main.command(short_help='Returns the migration state of the :database:')
@click.argument(KWARG_DATABASE, required=True, type=Database)
def version(database):
    """ Returns the current version of :database:

    :param database: file to interrogate.
    :type database: click.Path
    """
    import bou.version.api

    ver = bou.version.api.version(database)
    click.echo(f'"{database}" is at migration {ver}')
