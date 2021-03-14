""" bou.validators """

import click

import bou.backing


def migrations_loc(ctx, param, value):
    """ Does :value: exist as a package or filesystem location?

    :param ctx: of the validation check.
    :type ctx: click.Context
    :param param: that's being considered.
    :type param: click.Parameter
    :param value: of the given parameter.
    :type value: any
    """
    try:
        return bou.backing.location(value)

    except bou.backing.BackingError:
        raise click.BadParameter(
            f'Fully qualify or verify the existence of package "{value}".'
        )

    raise click.BadParameter(f'Migrations not located at "{value}".')
