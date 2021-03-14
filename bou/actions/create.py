""" bou.actions.create """

import os

from jinja2 import Environment, PackageLoader

import bou.chrono
import bou.migration


def create(name, migrations):
    """ Creates bou template named "<gmtime>_:name:.py" in :migrations: path

    :param name: of the migration file.
    :type name: space seperated string
    :param migrations: location to add to.
    :type migrations: a filesystem path or fully qualified python package
    """
    migration_ts = bou.chrono.now()
    t_vars = bou.migration.from_args(name, migration_ts)
    fn = bou.migration.to_filename(t_vars)
    tmpl = _template(**t_vars)

    fully_qualified_path = os.path.join(migrations, fn)

    with open(fully_qualified_path, 'w') as fh:
        fh.write(tmpl)


def _template(**kwargs):
    """ Generates a Jinja template from :**kwargs:

    :param **kwargs: @see ._vars()
    :type **kwargs: dict
    """
    template = Environment(
        loader=PackageLoader('bou', 'res')
    ).get_template('migration_template')

    return template.render(**kwargs)
