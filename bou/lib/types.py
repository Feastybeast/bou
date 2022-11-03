""" bou.lib.types
    ~~~
    Custom types used throughout the application.
"""

import collections
from collections.abc import Iterable
import typing
import pathlib

import bou.lib.constants as const

"""
Brief describes a brief human readable string, typically from *args
"""
Brief = typing.NewType('Brief', list[str])


"""
Database()s are syntactically sugarcoated pathlib.ConcretePath()s.
"""
Database = typing.NewType('Database', pathlib.Path)


"""
MigrationDir()s are pathlib.Paths, and are intended for bou writes.
"""
MigrationDir = typing.NewType('WritableMigration', pathlib.Path)

"""
MigrationFile()s are sugarcoated pathlib.Paths, for abstraction.
"""
MigrationFile = typing.NewType('MigrationFile', pathlib.Path)


class Migration(Iterable):
    """
    Migration()s are iterables of Boufiles, usually coming from
    methods that accept PathOrPackage arguments.
    """
    pass


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
