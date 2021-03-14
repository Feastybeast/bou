""" bou.migration
    ~~~
    Non-mutating operations against migration files.
"""

import bou.chrono
import bou.constants as c


def from_args(name, unixtime):
    """ Prep keyword args for the template

    :param name: to include in the filename.
    :type name: str
    :param unixtime: to utilize.
    :type unixtime: time.st_time
    """
    scrubbed_name = name

    migration_vars = {}
    migration_vars[c.LOCALTIME] = bou.chrono.as_readable(unixtime)
    migration_vars[c.NAME] = scrubbed_name.translate(
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
    migration_vars[c.VERSION] = bou.chrono.as_int(unixtime)

    return migration_vars


def from_filename(basename):
    """ Given :basename:, reverse back to migration_vars """
    ts, fs = basename.split(c.UNDERSCORE, 1)
    fs = fs.split(c.UNDERSCORE)

    return from_args(fs, ts)


def to_filename(migration_vars):
    """ Return the filename for the template

    :param ts: to parse.
    :type ts: time.st_time
    :param name: to include in the filename.
    :type name: str
    """
    prefix = c.UNDERSCORE.join([
        str(migration_vars[c.VERSION]),
        migration_vars[c.NAME].replace(
            c.SPACE, c.UNDERSCORE
        ).lower()
    ])

    return f'{prefix}{c.DOT_PY}'
