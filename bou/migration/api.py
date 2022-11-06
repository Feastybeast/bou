""" bou.boufile.api
    ~~~
    Interacts with the Boufile, a uuid stored in migrations and a managed
    database to prevent contamination of migrations.
"""

import time
import types

import bou.chrono
import bou.constants as const

from bou.boufile.errors import BoufileInvalidError

from bou.types import TemplateVars


def from_args(name: str, unixtime: time.struct_time) -> TemplateVars:
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


def to_filename(template_vars: TemplateVars) -> str:
    """ Generate the filename of the given :template_vars:

    :param template_vars: to parse.
    """
    prefix = const.UNDERSCORE.join([
        str(template_vars.version),
        template_vars.name.replace(
            const.SPACE, const.UNDERSCORE
        ).lower()
    ])

    return f'{prefix}{const.DOT_PY}'


def validate(boufile: types.ModuleType):
    """ Ensure :boufile: looks legitimate, or throw a fit.

    :param module: to inspect.
    """
    if not all([
        hasattr(boufile, const.DOWNGRADE),
        callable(boufile[const.DOWNGRADE]),

        hasattr(boufile, const.UPGRADE),
        callable(boufile[const.UPGRADE]),

        hasattr(boufile, const.UUID_CONST),
        hasattr(boufile, const.VERSION_CONST)
    ]):
        raise BoufileInvalidError
