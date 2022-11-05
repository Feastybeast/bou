""" bou.errors
    ~~~
    BouError is broadest Exception of the application,
    and shouldn't really be thrown.
"""


class BouError(Exception):
    """ Root exception for the application """
    pass
