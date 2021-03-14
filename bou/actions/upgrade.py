""" bou.actions.upgrade """


def upgrade(database, version, migrations):
    """ Upgrades :database: to :migrations: location's :version:.

    :param database: location on the filesystem.
    :type database: str
    :param version: to migrate up to.
    :type version: int
    :param migrations: location to use.
    :type migrations: a filesystem path or fully qualified python package
    """
    pass
