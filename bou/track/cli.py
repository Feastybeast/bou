""" bou.track.cli
    ~~~
    module specific CLI behaviors.
"""

import click

from bou.app.core import main, unhappy_case_handler
import bou.boufile.api
from bou.constants import DEFAULT_MIGRATIONS_DIRECTORY, KWARG_DATABASE
from bou.types import Database, BouDir


@main.command(short_help='Have bou manage migrations for :database:')
@click.argument(KWARG_DATABASE, required=True, type=Database)
@unhappy_case_handler
def track(database: Database):
    """ Instruct bou to manage migrations for :database:

    :param database: file to track. Probably shouldn't exist, but you know.
    """
    bou_dir = _prep_bou_dir(database)
    boufile_id = bou.boufile.api.identify(bou_dir)
    bou.backing.api.track(database, boufile_id, bou_dir)


def _prep_bou_dir(database: Database):
    """ Ensure :database: has a filesystem location before boostrapping.

    :param database: location to suggest default folder against.
    """
    bou_dir = _suggested(database) or _user()

    while True:
        try:
            bou.boufile.api.create(bou_dir)

        except bou.boufile.errors.BoufileCreationError:
            click.echo(f'Could not create Boufile at "{bou_dir}".')
            click.echo()
            bou_dir = _user()

        else:
            break

    return bou_dir


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
    return BouDir(input_path).absolute()
