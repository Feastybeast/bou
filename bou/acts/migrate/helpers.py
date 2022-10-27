""" bou.acts.migrate.helpers
    ~~~

"""

import importlib
import logging
import os
import sys
import types

from bou.lib.errors import BackingError
from bou.lib.types import Location, LocationType, Migration


def location(migrations: Migration) -> Location:
    """ Locates the filesystem location of :migrations:

    :param migrations: path to consider.
    :returns: Location of the migrations.
    """
    fspath = os.path.abspath(migrations)

    if os.path.exists(fspath):
        logging.debug(f'Migrations path located at "{fspath}"')
        return Location(migrations, fspath, LocationType.FILESYSTEM)

    try:
        m = _module(migrations)
        logging.debug(f'Migrations package located at "{migrations}"')
        return Location(migrations, m.__path__.pop(), LocationType.PACKAGE)

    except (ImportError, TypeError, ModuleNotFoundError):
        raise BackingError(
            f'Fully qualify or verify the existence of package "{migrations}".'
        )

    raise BackingError(f'No Migrations at "{migrations}".')


def _module(spec: str) -> types.ModuleType:
    """ Returns the module at :spec:

    @see Issue #2

    :param spec: to load.
    """
    cwd = os.getcwd()

    if cwd not in sys.path:
        sys.path.append(cwd)

    return importlib.import_module(spec)
