""" bou.list.api """

import sys

from bou.types import Migration
from bou.constants import DOT_PY, UNDERSCORE


def action(migrations: Migration, start: int = 0, stop: int = sys.maxsize):
    """ Lists the steps located in :directory:.

    :param migrations: path to iterate.
    """
    candidates = sorted(
        filter(
            _is_migration(start, stop),
            migrations
        )
    )

    if (start - stop) > 0:
        candidates = candidates.reverse()

    for each in candidates:
        yield each


def _is_migration(starting, stopping):
    """ Dynamically construct the filtering critereon.

    :param starting: timestamp to allow.
    :type starting: int
    :param stopping: timestamp to allow.
    :type stopping: int
    """
    min_mig, max_mig = sorted([starting, stopping])

    def _is_migration_filter(file):
        """ Looking for {[min_mig, max_mig]}_{human_readable}.py

        :param file: to consider.
        :type file: str
        """
        if not file.endswith(DOT_PY):
            return

        if len(file) < 14:  # it can't be at least "{unixtime}_.py"
            return

        # Formatting ...
        if not file[:10].isdigit():
            return

        if file[10] != UNDERSCORE:
            return

        timestamp = int(file[:10])

        return all([
            timestamp >= min_mig,
            timestamp <= max_mig
        ])

    return _is_migration_filter
