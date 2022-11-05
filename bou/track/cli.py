""" bou.track.cli
    ~~~
    module specific CLI behaviors.
"""

import click

import bou.cli.helpers as helpers

from bou.cli.main import main
from bou.constants import DEFAULT_MIGRATIONS_DIRECTORY, KWARG_DATABASE
from bou.types import Database, MigrationDir


@main.command(short_help='Have bou manage migrations for :database:')
@click.argument(KWARG_DATABASE, required=True, type=Database)
@helpers.unhappy_case_handler
def track(database: Database):
    """ Instruct bou to manage migrations for :database:

    :param database: file to track. Probably shouldn't exist, but you know.
    """
    import bou.track.api

    migrations_path = _suggested(database) or _user()

    while True:
        try:
            bou.track.api.filesystem(migrations_path)

        except bou.boufile.errors.BoufileCreationError:
            click.echo(f'Could not create Boufile at "{migrations_path}".')
            click.echo()
            migrations_path = _user()

        else:
            break

    click.echo()
    bou.boufile.api.create(migrations_path)
    bou.track.api.database(database, migrations_path)


def _suggested(database: Database):
    """ Suggest :database:/migrations for Boufiles.

    :param database: to interrogate.
    """
    suggested_path = (
        database.parent / DEFAULT_MIGRATIONS_DIRECTORY
    ).absolute()

    if click.confirm(f'Store migrations at {suggested_path}', default=True):
        return suggested_path


def _user():
    """ Get information from the user about where they want it. """
    input_path = click.prompt('New migration directory')
    return MigrationDir(input_path).absolute()
