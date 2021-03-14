""" bou.actions.manage
    ~~~
    Manage the given database.
"""

import bou.backing


def manage(database):
    """ [Creates and] adds bou management tables to :database:

    :param database: location to store the database at.
    :type database: str
    """
    bou.backing.create(database)
