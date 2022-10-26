""" bou.migration
    ~~~
    Non-mutating operations against migration files.
"""

from collections import namedtuple
import time
import types

import bou.chrono
import bou.constants as c

MigrationVars = namedtuple('MigrationVars', [
    c.LOCALTIME,
    c.NAME,
    c.VERSION
])


def from_args(name: str, unixtime: time.st_time) -> MigrationVars:
    """ Generate MigrationVars for the given :name: and :unixtime:

    :param name: to include in the filename.
    :param unixtime: to utilize.
    """
    localtime = bou.chrono.as_readable(unixtime)

    version = bou.chrono.as_int(unixtime)

    scrubbed_name = name.translate(
        str.maketrans({
            c.ASTERISK: c.BLANK,
            c.BACK_SLASH: c.BLANK,
            c.GT: c.BLANK,
            c.LT: c.BLANK,
            c.PIPE: c.BLANK,
            c.QUESTION_MARK: c.BLANK,
            c.QUOTE: c.BLANK,
        })
    )

    return MigrationVars(localtime, scrubbed_name, version)


def from_filename(basename: str) -> MigrationVars:
    """ Generates MigrationVars from :basename:

    :param basename: of the file to reverse.

    @consider if basename should be a Path?
    """
    ts, fs = basename.split(c.UNDERSCORE, 1)
    ts = bou.chrono.at(int(ts))
    fs = fs.replace(c.UNDERSCORE, c.SPACE)

    return from_args(fs, ts)


def is_valid(module: types.ModuleType) -> bool:
    """ Does this look like it's a real module?

    :param module: to inspect.
    """
    return all([
        hasattr(module, c.DOWNGRADE),
        callable(module[c.DOWNGRADE]),

        hasattr(module, c.UPGRADE),
        callable(module[c.UPGRADE]),

        hasattr(module, c.VERSION_CONST)
    ])


def to_filename(migration_vars: MigrationVars) -> str:
    """ Generate the filename of the given :migration_vars:

    :param migration_vars: to parse.
    """
    prefix = c.UNDERSCORE.join([
        str(migration_vars.version),
        migration_vars.name.replace(
            c.SPACE, c.UNDERSCORE
        ).lower()
    ])

    return f'{prefix}{c.DOT_PY}'
