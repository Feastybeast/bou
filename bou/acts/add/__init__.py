""" bou.acts.add
    ~~~
    `bou add migration_loc human readables`
    produces a template at `migration_loc/{unixgmttime}_human_readables.py`
"""

import os

from jinja2 import Environment, PackageLoader

import bou.lib.chrono
from bou.lib.types import Migration


def action(migration_loc: Migration, *human_readables: list[str]):
    """ Creates a template at ":migration_loc:/<gmtime>_:human_readable:.py"

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    migration_ts = bou.chrono.now()
    m_vars = bou.migration.from_args(*human_readables, migration_ts)
    fn = bou.migration.to_filename(m_vars)

    tmpl = _template(m_vars._asdict())

    fully_qualified_path = os.path.join(migration_loc, fn)

    with open(fully_qualified_path, 'w') as fh:
        fh.write(tmpl)


def _template(values):
    """ Generates a Jinja template from :values:

    :param values: to digest.
    :type values: dict
    """
    template = Environment(
        loader=PackageLoader('bou', 'res')
    ).get_template('migration_template')

    return template.render(**values)
