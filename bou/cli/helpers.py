""" bou.cli.helpers
    ~~~
    Support code for the cli module.
"""

import functools
import sys
import traceback

import click

import bou.errors


def error():
    """ Print """
    click.echo('-- bou had a major failure --')
    traceback.print_exc(file=sys.stdout)
    click.echo('-- bou had a major failure --')


def exit(msg, exit_code):
    """ sys.exit(:exit_code:) following a :msg:

    :param msg: to print to the end user.
    :type msg: str
    :param exit_code: to report to the caller.
    :type exit_code: int
    """
    click.echo('')
    click.echo(msg)
    sys.exit(exit_code)


def unhappy_case_handler(click_func: callable):
    """ Provides return management for :click_func:

    :param click_func: to be wrapped.
    """
    @functools.wraps(click_func)
    def wrapper(*args, **kwargs):
        """ """
        try:
            click_func(*args, **kwargs)

        except bou.errors.BackingError:
            raise click.BadParameter(
                f'Fully qualify or verify the package "{args[0]}".'
            )

        except bou.errors.MigrationsError:
            raise click.BadParameter(f'Migrations not located at "{args[0]}".')

        except Exception as e:
            exit(e, 1)

        else:
            exit('Done.', 0)

    return wrapper
