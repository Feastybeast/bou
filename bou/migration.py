""" bou.migration
    ~~~
    Non-mutating operations against migration files.
"""

from collections import namedtuple

import bou.chrono
import bou.constants as c


def from_args(name, unixtime):
    """ Prep keyword args for the template

    :param name: to include in the filename.
    :type name: str
    :param unixtime: to utilize.
    :type unixtime: time.st_time
    """
    localtime = bou.chrono.as_readable(unixtime)

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
    version = bou.chrono.as_int(unixtime)

    return MigrationVars(localtime, scrubbed_name, version)


def from_filename(basename):
    """ Given :basename:, reverse back to migration_vars

    :param basename: of the file to reverse.
    :type basename: str
    """
    ts, fs = basename.split(c.UNDERSCORE, 1)
    ts = bou.chrono.at(int(ts))
    fs = fs.replace(c.UNDERSCORE, c.SPACE)

    return from_args(fs, ts)


def is_valid(module):
    """ Does this look like it's a real module?

    :param module: to inspect.
    :type module: module
    """
    return all([
        hasattr(module, c.DOWNGRADE),
        callable(module[c.DOWNGRADE]),

        hasattr(module, c.UPGRADE),
        callable(module[c.UPGRADE]),

        hasattr(module, c.VERSION_CONST)
    ])


def to_filename(migration_vars):
    """ Return the filename for the template

    :param ts: to parse.
    :type ts: time.st_time
    :param name: to include in the filename.
    :type name: str
    """
    prefix = c.UNDERSCORE.join([
        str(migration_vars.version),
        migration_vars.name.replace(
            c.SPACE, c.UNDERSCORE
        ).lower()
    ])

    return f'{prefix}{c.DOT_PY}'


MigrationVars = namedtuple('MigrationVars', [
    c.LOCALTIME,
    c.NAME,
    c.VERSION
])
