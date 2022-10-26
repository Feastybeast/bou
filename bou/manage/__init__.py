""" bou.actions.manage
    ~~~
    Manage the given database.
"""

import bou.backing.operations as operations


def manage(database):
    """ [Creates and] adds bou management tables to :database:

    :param database: location to store the database at.
    :type database: str
    """
    operations.create(database)
