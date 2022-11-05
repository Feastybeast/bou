""" bou.modules
    ~~~
    Abstracts importlib behaviors for reusability.
"""
import importlib
import importlib.resources
import types

import pathlib

from bou.constants import BLANK, DOT, DOT_PY, FORWARD_SLASH


def matching(glob: str):
    """ Locate packages matching :spec:

    e.g. bou.*.cli yields (bou.add.cli, .., bou.version.cli)

    :param glob: to search against.
    """
    pkg_root = glob.split(DOT)[0]
    pkg_origin = importlib.util.find_spec(pkg_root).origin
    pkg_parent = pathlib.Path(pkg_origin).parent

    children = f'{FORWARD_SLASH.join(glob.split(DOT)[1:])}{DOT_PY}'

    for each in pkg_parent.glob(children):
        rel_pkg = str(each.relative_to(pkg_parent))
        rel_pkg = rel_pkg.replace(DOT_PY, BLANK)
        rel_pkg = rel_pkg.replace(FORWARD_SLASH, DOT)

        yield f'{pkg_root}{DOT}{rel_pkg}'


def load(module: str):
    """ Sugarcoats dynamically importing the :module:

    :param module: to import.
    """
    return importlib.import_module(module)


def resources(module: types.ModuleType):
    """ Sugarcoats importlib.resources.files(:module:)

    :param module: to index.
    """
    return importlib.resources.files(module)
