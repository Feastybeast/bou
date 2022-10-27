""" bou.acts.add.helpers
    ~~~
    Support methods to generate migration templates.
"""

import time
import types

import bou.lib.chrono
import bou.lib.constants as const
from bou.lib.types import TemplateVars


def from_args(name: str, unixtime: time.st_time) -> TemplateVars:
    """ Generate TemplateVars for the given :name: and :unixtime:

    :param name: to include in the filename.
    :param unixtime: to utilize.
    """
    localtime = bou.chrono.as_readable(unixtime)

    version = bou.chrono.as_int(unixtime)

    scrubbed_name = name.translate(
        str.maketrans({
            const.ASTERISK: const.BLANK,
            const.BACK_SLASH: const.BLANK,
            const.GT: const.BLANK,
            const.LT: const.BLANK,
            const.PIPE: const.BLANK,
            const.QUESTION_MARK: const.BLANK,
            const.QUOTE: const.BLANK,
        })
    )

    return TemplateVars(localtime, scrubbed_name, version)


def from_filename(basename: str) -> TemplateVars:
    """ Generates TemplateVars from :basename:

    :param basename: of the file to reverse.

    @consider if basename should be a Path?
    """
    ts, fs = basename.split(const.UNDERSCORE, 1)
    ts = bou.chrono.at(int(ts))
    fs = fs.replace(const.UNDERSCORE, const.SPACE)

    return from_args(fs, ts)


def is_valid(module: types.ModuleType) -> bool:
    """ Does this look like it's a real module?

    :param module: to inspect.
    """
    return all([
        hasattr(module, const.DOWNGRADE),
        callable(module[const.DOWNGRADE]),

        hasattr(module, const.UPGRADE),
        callable(module[const.UPGRADE]),

        hasattr(module, const.VERSION_CONST)
    ])


def to_filename(migration_vars: TemplateVars) -> str:
    """ Generate the filename of the given :migration_vars:

    :param migration_vars: to parse.
    """
    prefix = const.UNDERSCORE.join([
        str(migration_vars.version),
        migration_vars.name.replace(
            const.SPACE, const.UNDERSCORE
        ).lower()
    ])

    return f'{prefix}{const.DOT_PY}'
