""" bou.add.api
    ~~~
    `bou add database_loc human readables`
        produces `{unixgmttime}_human_readables.py`
        in `database_loc`'s migrations directory.
"""

import uuid

import bou.backing.api as backing
import bou.boufile.api as boufile
import bou.chrono
from bou.types import (
    Brief, Database, MigrationDir, MigrationFile, TemplateVars
)


def add(database: Database, *brief: Brief):
    """ Creates "<gmtime>_:brief:.py" in :database:'s migration directory.

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    _guard_exists(database)
    migration_dir, uuid = _locate(database)
    _guard_synced(migration_dir, uuid)
    template_vars = _vars(uuid, *brief)
    filename = _filename(template_vars)
    contents = _template(migration_dir, uuid, template_vars)

    _write(migration_dir / filename, contents)


def _filename(template_vars: TemplateVars) -> str:
    """ """
    return boufile.to_filename(template_vars)


def _guard_exists(database: Database):
    """ Ensure :database: actually exists on the filesystem.

    :param database: to look for.
    """
    backing.exists(database)


def _guard_synced():
    """ """
    pass


def _locate(database: Database) -> MigrationDir:
    """ See bou.backing.operations.directory_of(database)

    :param database: to interrogate.
    """
    return bou.backing.api.migrations_for(database)


def _template(mig_dir: MigrationDir, template_vars: TemplateVars) -> str:
    """ Creates "<gmtime>_:brief:.py" in :database:'s migration directory.

    :param migration_loc: to write the template to.
    :param human_readable: space seperated string to describe the migration.
    """
    return bou.boufile.template(template_vars._asdict())


def _vars(uuid: uuid.uuid4, *brief: Brief):
    return bou.boufile.api.from_args(
        *brief,
        bou.chrono.now()
    )


def _write(path: MigrationFile, contents: str):
    """ """
    path.write_text(contents)
