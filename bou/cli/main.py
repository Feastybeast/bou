""" bou.cli.main
    ~~~
    The CLI to the bou library.
    @see bou.acts.<method>.<method>() for implementations.
"""

import math

import click

import bou.cli.helpers as helpers
from bou.lib.types import Brief, Database


@click.group()
def main():
    pass


@main.command(short_help='Create a new migration for :database:')
@click.argument('database', type=Database)
@click.argument('brief', nargs=-1, required=True, type=str)
@helpers.unhappy_case_handler
def add(database: Database, brief: Brief):
    """ Add a new migration for :database: with a :brief: description.

    Writing to a python module is asking for trouble.
    Please use this only during development against filesystem paths.

    :param database: to add the migration to.
    :param brief: description of the migration goals.
    """
    from bou.ops.add import add

    add(database, brief)


@main.command(short_help='Lists available :migrations:')
@click.argument('database', type=Database)
@helpers.unhappy_case_handler
def list(database: Database):
    """ Lists all of :database:'s migrations

    :param database: to interrogate.
    """
    import bou.ops.list

    versions = bou.ops.list.list(database)

    # Interrogate the database for where it's stuff is

    # THEN click.echo(f'Listing migrations at "{migrations.input}":')
    click.echo()

    # THEN click.echo(f'Listing migrations at "{migrations.input}":')
    # bou.ops.list.list(migrations.output)
    for file in enumerate(versions):
        m_vars = bou.migration.from_filename(file)
        msg = f'{m_vars.localtime}) {m_vars.localtime}: {file}'
        click.echo(msg)


@main.command(short_help='Instruct bou to manage migrations for :database:')
@click.argument('database', required=True, type=Database)
@helpers.unhappy_case_handler
def track(database: Database):
    """ Instruct bou to manage migrations for :database:

    :param database: file to track. Probably shouldn't exist, but you know.
    """
    import bou.ops.track

    migrations_path = helpers.suggest_default_path()

    if not click.confirm(f'Store migrations at "{migrations_path}" [Y/n]?'):
        click.echo('')
        migrations_path = click.input(f'New migrations directory: ')

    bou.ops.track.track(database, migrations_path)


@main.command(short_help='Migrate :database: to :migrations:/:version:')
@click.argument('database', required=True, type=Database)
@click.argument('to_version', required=False, type=int)
def migrate(database: Database, to_version: int):
    """ Migrate :database: to :version: stored at :migrations:

    :param database: to upgrade.
    :param version: to finish at.
    """
    import bou.ops.migrate

    helpers.patch_sys_dot_path()
    bou.ops.migrate.migrate(database, to_version or math.inf)


@main.command(short_help='Returns the migration state of the :database:')
@click.argument('database', required=True, type=Database)
def version(database):
    """ Returns the current version of :database:

    :param database: file to interrogate.
    :type database: click.Path
    """
    import bou.ops.version

    ver = bou.ops.version.version(database)
    click.echo(f'"{database}" is at migration {ver}')


if __name__ == "__main__":
    main()
