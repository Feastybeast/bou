""" bou.types
    ~~~
    Custom types used throughout the application.

[1]: https://stackoverflow.com/questions/29850801/subclass-pathlib-path-fails
"""

import collections
from collections.abc import Iterable
import types
import typing
import pathlib

import bou.constants as const

"""
Brief describes a brief human readable string, typically from *args
"""
Brief = typing.NewType('Brief', list[str])


class _BouPath(type(pathlib.Path())):
    """ Thanks [1] """
    pass


class Database(_BouPath):
    """ Database()s are syntactically sugarcoated pathlib.ConcretePath()s. """
    pass


class MigrationDir(_BouPath):
    """ MigrationDir()s are pathlikes intended for write ops. """
    pass


class MigrationFile(types.ModuleType):
    """ MigrationFile()s are the specific files located in Migration()s. """
    pass


class MigrationPackage(_BouPath):
    """ MigrationPackage()s are READ ONLY pathlikes, via python paths. """
    pass


""" Migration()s coordinate MigrationFiles, and typically
    come from methods that accept PathOrPackage arguments. """
Migration = typing.NewType('Migration', Iterable[MigrationFile])


"""
Methods which read or process migrations can do so from either a PathOrPackage.
"""
PathOrPackage = typing.Union[MigrationDir | str]


"""
TemplateVars
    .localtime: when the template was generated.
    .name: provided by the end user.
    .uuid: that bundles all templates together.
    .version: issued to the migration.
"""
TemplateVars = collections.namedtuple('TemplateVars', [
    const.LOCALTIME,
    const.NAME,
    const.UUID,
    const.VERSION
])
