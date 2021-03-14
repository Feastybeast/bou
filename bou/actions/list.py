""" bou.actions.list """

import os

from bou.constants import DOT_PY


def list(migrations):
    """ Lists the steps located in :migrations:.

    :param migrations: location to use.
    :type migrations: a filesystem path or fully qualified python package
    """
    iterated = enumerate(
        sorted(
            filter(
                lambda basename: basename.endswith(DOT_PY),
                os.listdir(migrations)
            )
        )
    )

    for each in iterated:
        yield each
