""" bou.chrono
    ~~~
    Details about timing for the application.
"""

import time


def as_int(st_time: time.st_time) -> int:
    """ Truncates :st_time: to the second.

    :param st_time: to convert to an integer.
    :returns: st_time to the second.
    """
    return int(time.mktime(st_time))


def as_readable(st_time: time.st_time) -> str:
    """ Transcribe :st_time: as a GMT based human readable string.

    :returns: a locale appropriate timestamp.
    """
    return time.strftime('%x %X GMT', st_time)


def at(timestamp: int) -> time.st_time:
    """ Sugarcoats :timestamp: with standard library calls. """
    return time.gmtime(timestamp)


def now() -> time.st_time:
    """ Returns now, GMT.

    :returns: "now" at GMT.
    """
    return at(None)
