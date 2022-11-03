""" bou.lib.migration_helpers
    ~~~
    Support behaviors for iterating migrations.
"""

import importlib
import logging

from bou.lib.constants import BOUFILE
from bou.lib.errors import MigrationsSourceError
from bou.lib.types import Migration, PathOrPackage


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

        m = importlib.import_module(migrations)
        logging.debug(f'Python package located: {migrations}')
        return importlib.resources.files(m)

    except (ImportError, TypeError, ModuleNotFoundError):
        raise MigrationsSourceError(
            f'Fully qualify or verify the existence of package "{migrations}".'
        )

    raise MigrationsSourceError(f'No Migrations at "{migrations}".')
