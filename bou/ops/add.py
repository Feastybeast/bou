""" bou.ops.add
    ~~~
    `bou add database_loc human readables`
        produces `{unixgmttime}_human_readables.py`
        in `database_loc`'s migrations directory.
"""

import pathlib

from jinja2 import Environment, PackageLoader

import bou.lib.chrono
import bou.lib.boufile


def action(database: pathlib.Path, *brief: list[str]):
    """ Creates "<gmtime>_:brief:.py" in :database:'s migration directory.

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    migration_ts = bou.chrono.now()
    m_vars = bou.lib.boufile.from_args(*brief, migration_ts)
    filename = bou.lib.boufile.to_filename(m_vars)

    tmpl = _template(m_vars._asdict())

    fully_qualified_path = pathlib.Path() / filename
    fully_qualified_path.write_text(tmpl)


def _template(values):
    """ Generates a Jinja template from :values:

    :param values: to digest.
    :type values: dict
    """
    template = Environment(
        loader=PackageLoader('bou', 'res')
    ).get_template('migration_template')

    return template.render(**values)
