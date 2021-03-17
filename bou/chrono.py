""" bou.chrono
    ~~~
    Details about timing for the application.
"""

import time


def as_int(st_time):
    """ Truncates :st_time: into a discrete amount of seconds.

    :param st_time: to convert to an integer.
    :type st_time: time.st_time
    :returns int: of :st_time: rounded to the second
    """
    return int(time.mktime(st_time))


def as_readable(st_time):
    """ Transcribe :st_time: into a human readable string.

    :param st_time: to convert to an integer.
    :type st_time: time.st_time
    :returns str: of locale appropriate timestamps.
    """
    return time.strftime('%x %X GMT', st_time)


def at(timestamp):
    """ Sugarcoats :timestamp: with standard library calls.

    :returns time.st_time: of time.gmtime()
    """
    return time.gmtime(timestamp)


def now():
    """ Gets "now" at GMT.

    :returns time.st_time: of time.gmtime()
    """
    return at(None)
