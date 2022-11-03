""" bou.ops.add
    ~~~
    `bou add database_loc human readables`
        produces `{unixgmttime}_human_readables.py`
        in `database_loc`'s migrations directory.
"""

import uuid

import bou.lib.boufile
import bou.lib.chrono
from bou.lib.types import (
    Brief, Database, MigrationDir, MigrationFile, TemplateVars
)

import bou.backing.operations


def add(database: Database, *brief: Brief):
    """ Creates "<gmtime>_:brief:.py" in :database:'s migration directory.

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    migration_dir, uuid = _locate(database)
    _guard(migration_dir, uuid)
    template_vars = _vars(uuid, *brief)
    filename = _filename(template_vars)
    contents = _template(migration_dir, uuid, template_vars)

    _write(migration_dir / filename, contents)


def _filename(template_vars: TemplateVars) -> str:
    """ """
    return bou.lib.boufile.to_filename(template_vars)


def _guard():
    """ """
    pass


def _locate(database: Database) -> MigrationDir:
    """ See bou.backing.operations.directory_of(database)

    :param database: to interrogate.
    """
    return bou.backing.operations.directory_of(database)


def _template(mig_dir: MigrationDir, template_vars: TemplateVars) -> str:
    """ Creates "<gmtime>_:brief:.py" in :database:'s migration directory.

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    return bou.lib.boufile.template(template_vars._asdict())


def _vars(uuid: uuid.uuid4, *brief: Brief):
    return bou.lib.boufile.from_args(
        *brief,
        bou.lib.chrono.now()
    )


def _write(path: MigrationFile, contents: str):
    """ """
    path.write_text(contents)
