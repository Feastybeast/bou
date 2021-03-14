""" bou.cli
    ~~~
    The CLI to the bou library.
    @see bou.actions.<method>.<method>() for implementations.
"""

import sys
import traceback

import click

import bou.actions
import bou.backing
from bou.constants import MIGRATIONS_DEFAULT, SPACE
from bou.validators import migrations_loc


@click.group()
def main():
    pass


@main.command(
    short_help='Store a new migration with :name: in :migrations:'
)
@click.argument('name', nargs=-1, required=True, type=str)
@click.argument(
    'migrations',
    default=MIGRATIONS_DEFAULT,
    type=click.Path(
        allow_dash=False, exists=True, file_okay=False, resolve_path=True
    )
)
def create(name, migrations):
    """ Store a new migration with :name: in :migrations:

    Writing to a python module or so forth is asking for trouble.
    Please use this only during development against filesystem paths.

    :param name: of the human readable segment of the migration.
    :type name: tuple<str>
    :param migrations: directory to write to.
    :type migrations: click.Path
    """
    bou.actions.create(
        SPACE.join(name),
        migrations
    )
    _done()


@main.command(
    short_help='Downgrade :database: to :version: stored at :migrations:'
)
@click.argument('database', required=True, type=click.Path())
@click.argument('version', default=-1, required=False, type=int)
@click.option(
    '--migrations', callback=migrations_loc, default=MIGRATIONS_DEFAULT
)
def downgrade(database, version, migrations):
    """ Downgrade :database: to :version: stored at :migrations:

    :param database: file to downgrade.
    :type database: click.Path
    :param version: to migrate to.
    :type version: int
    :param migrations: to consider for this action.
    :type migrations: str
    """
    bou.actions.downgrade(database, version, migrations)


@main.command(
    short_help='Lists all migrations at :migrations:'
)
@click.argument(
    'migrations', callback=migrations_loc, default=MIGRATIONS_DEFAULT
)
def list(migrations):
    """ Lists all migrations at :migrations:

    :param migrations: module or filesystem path to iterate.
    :type migrations: str
    """
    click.echo(f'Listing migrations at "{migrations}":')
    click.echo()

    for idx, file in bou.actions.list(migrations):
        click.echo(f'{idx+1}) {file}')

    _done()


@main.command(
    short_help='Instruct bou to manage migrations for :database:'
)
@click.argument('database', required=True, type=click.Path())
def manage(database):
    """ Instruct bou to manage migrations for :database:

    :param database: file to manage.
    :type database: click.Path
    """
    try:  # to find an existing database. Warn if it's there.
        bou.actions.version(database)

        msg = f'"{database}" exists or is already managed. Continue anyways?'

        if click.confirm(msg, default=False):
            raise bou.BouError()

    except bou.BouError:  # It didn't exist or was forced. Carry on.
        try:
            bou.actions.manage(database)
            _done()

        except bou.BouError:
            click.echo('-- bou management failed: --')
            traceback.print_exc(file=sys.stdout)
            click.echo('-- bou management failed  --')

            _exit(f'Unable to manage "{database}"', 1)


@main.command(
    short_help='Migrate :database: to :version: stored at :migrations:'
)
@click.argument('database', required=True, type=click.Path())
@click.argument('version', default=-1, required=False, type=int)
@click.option(
    '--migrations', callback=migrations_loc, default=MIGRATIONS_DEFAULT
)
def upgrade(database, version, migrations):
    """ Migrate :database: to :version: stored at :migrations:

    :param database: file to upgrade.
    :type database: click.Path
    :param version: to migrate to.
    :type version: int
    :param migrations: to consider for this action.
    :type migrations: str
    """
    bou.actions.upgrade(database, version, migrations)


@main.command(
    short_help='Returns the current version of :database:'
)
@click.argument('database', required=True, type=click.Path())
def version(database):
    """ Returns the current version of :database:

    :param database: file to interrogate.
    :type database: click.Path
    """
    try:
        ver = bou.actions.version(database)
        click.echo(f'"{database}" is at migration {ver}')

    except bou.BouError:
        click.echo(f'"{database}" isn\'t managed by bou.')


def _done():
    """ Happy exit conditions! """
    return _exit('Done.', 0)


def _exit(msg, exit_code):
    """ sys.exit(:exit_code:) following a :msg:

    :param msg: to print to the end user.
    :type msg: str
    :param exit_code: to report to the caller.
    :type exit_code: int
    """
    click.echo('')
    click.echo(msg)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
