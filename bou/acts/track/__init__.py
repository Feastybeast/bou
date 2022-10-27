""" bou.acts.track
    ~~~
    Introduce _bou behaviors into the :database:.
"""

import pathlib

import bou.backing.operations as operations


def action(database: pathlib.Path):
    """ [Creates and] adds bou management to :database:

    :param database: path on the filesystem.
    """
    operations.track(database)
