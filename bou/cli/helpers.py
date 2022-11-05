""" bou.cli.helpers
    ~~~
    Support code for the cli module.
"""

import functools
import pathlib
import sys
import traceback

import click

import bou.backing.errors
from bou.constants import KWARG_DATABASE


def cwd() -> pathlib.Path:
    """ Gets the current directory """
    return pathlib.Path.cwd()


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


def patch_sys_dot_path():
    """ Adds the current working directory to sys.path, if needed. """
    the_cwd = cwd()

    if the_cwd not in sys.path:
        sys.path.append(the_cwd)


def unhappy_case_handler(click_func: callable):
    """ Provides exception management for :click_func:

    :param click_func: to be wrapped.
    """
    @functools.wraps(click_func)
    def wrapper(*args, **kwargs):
        """ """
        try:
            click_func(*args, **kwargs)

        except bou.backing.errors.BackingMissingError:
            exit(
                f'"{kwargs[KWARG_DATABASE]}" is missing. Aborting.',
                1
            )

        except bou.backing.errors.BackingUnversionedError:
            exit(
                f'"{kwargs[KWARG_DATABASE]}" not managed by bou. Aborting.',
                1
            )

        except Exception:
            error()
            exit('', 1)

        else:
            exit('Done.', 0)

    return wrapper
