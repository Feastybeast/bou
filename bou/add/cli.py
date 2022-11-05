""" bou.add.cli
    ~~~
    module specific CLI behaviors.
"""

import click

import bou.cli.helpers as helpers
from bou.cli.main import main
from bou.constants import KWARG_BRIEF, KWARG_DATABASE
from bou.types import Brief, Database


@main.command(short_help='Create a new migration for :database:')
@click.argument(KWARG_DATABASE, type=Database)
@click.argument(KWARG_BRIEF, nargs=-1, required=True, type=str)
@helpers.unhappy_case_handler
def add(database: Database, brief: Brief):
    """ Add a new migration for :database: with a :brief: description.

    Writing to a python module is asking for trouble.
    Please use this only during development against filesystem paths.

    :param database: to add the migration to.
    :param brief: description of the migration goals.
    """
    from bou.add.api import add

    add(database, brief)
