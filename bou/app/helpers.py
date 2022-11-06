""" bou.app.helpers
    ~~~
    Support code for the cli module.
"""

import pathlib
import sys

import bou.modules


def cwd() -> pathlib.Path:
    """ Gets the current directory """
    return pathlib.Path.cwd()


def load_modules(module_glob: str):
    """ Loads modules matching :module_glob:.

        Click should handle the rest.
    """
    for each in bou.modules.matching(module_glob):
        bou.modules.load(each)


def patch_sys_dot_path():
    """ Adds the current working directory to sys.path, if needed. """
    the_cwd = cwd()

    if the_cwd not in sys.path:
        sys.path.append(the_cwd)
