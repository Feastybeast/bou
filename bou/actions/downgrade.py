""" bou.actions.downgrade """


def downgrade(database, version, migrations):
    """ Downgrades :database: to :migrations: location's :version:.

    :param database: location on the filesystem.
    :type database: str
    :param version: to migrate down to.
    :type version: int
    :param migrations: location to use.
    :type migrations: a filesystem path or fully qualified python package
    """
    pass
