""" bou.lib.types
    ~~~
    Custom types used throughout the application.
"""

import collections
import enum
import typing
import pathlib

import bou.constants as const


class Direction(enum.Enum):
    """ Direction should be self explanatory, with ...
            .UPGRADE
            .DOWNGRADE
    """
    UPGRADE = const.UPGRADE
    DOWNGRADE = const.DOWNGRADE


"""
bou.migrate.helpers(Migration) => Location(.input, .output, LocationType)
   .input = what was passed in. filepath, python.package.path, etc.
   .output = what the resulting filesystem location is.
   .type = indicates what the input was.
"""
Location = collections.namedtuple('Location', [
    const.INPUT, const.OUTPUT, const.TYPE
])


class LocationType(enum.Enum):
    """
    LocationType is
        .FILESYSTEM = when determined to be a filesystem path.
        .PACKAGE  = when abstracted into a python package.
    """
    FILESYSTEM = 0
    PACKAGE = 1


"""
Migration = [ python.module.location || ../file/system/path ]
"""
Migration = typing.Union[Location.output, pathlib.Path]


"""
TemplateVars
    .localtime: when the template was generated.
    .name: provided by the end user.
    .version: issued to the migration.
"""
TemplateVars = collections.namedtuple('TemplateVars', [
    const.LOCALTIME,
    const.NAME,
    const.VERSION
])
