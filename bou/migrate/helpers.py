""" bou.migrate.helpers
    ~~~
    Support behaviors for iterating migrations.
"""

import logging

from bou.constants import BOUFILE
from bou.errors import MigrationsSourceError
import bou.modules
from bou.types import Migration, PathOrPackage


def location(migrations: PathOrPackage) -> Migration:
    """ Locates the filesystem location of :migrations:

    :param migrations: path to consider.
    :returns: Location of the migrations.
    """
    try:
        fspath = migrations.absolute()

        if fspath.isdir() and fspath.relpath(BOUFILE).exists():
            logging.debug(f'Filesystem path located: {fspath}')
            return fspath.iterdir()

        m = bou.modules.load(migrations)
        logging.debug(f'Python package located: {migrations}')
        return bou.modules.resources(m)

    except (ImportError, TypeError, ModuleNotFoundError):
        raise MigrationsSourceError(
            f'Fully qualify or verify the existence of package "{migrations}".'
        )

    raise MigrationsSourceError(f'No Migrations at "{migrations}".')
