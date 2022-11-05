""" bou.list.cli
    ~~~
    module specific CLI behaviors
"""

import click

import bou.cli.helpers as helpers
from bou.cli.main import main
from bou.constants import KWARG_DATABASE
from bou.types import Database


@main.command(short_help='Lists migrations known by :database:')
@click.argument(KWARG_DATABASE, type=Database)
@helpers.unhappy_case_handler
def list(database: Database):
    """ Lists all of :database:'s migrations

    :param database: to interrogate.
    """
    import bou.list.api

    versions = bou.list.api.list(database)

    # Interrogate the database for where it's stuff is

    # THEN click.echo(f'Listing migrations at "{migrations.input}":')
    click.echo()

    # THEN click.echo(f'Listing migrations at "{migrations.input}":')
    # bou.list.api.list(migrations.output)
    for file in enumerate(versions):
        m_vars = bou.migration.from_filename(file)
        msg = f'{m_vars.localtime}) {m_vars.localtime}: {file}'
        click.echo(msg)
