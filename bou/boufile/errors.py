""" bou.boufile.errors
    ~~~
    Both BouDir{...} and BouFile{...} errors are here.
"""

from bou.errors import BouError


class BouDirError(BouError):
    """ raised for Boudir problems """
    pass


class BouDirCreateError(BouDirError):
    """ bou.boufile.api.create() failed. """
    pass


class BouFileError(BouError):
    """ raised for BouFile problems """
    pass


class BouFileCreateError(BouFileError):
    """ Couldn't be made """
    pass


class BoufileInvalidError(BouFileError):
    """ Can't be read or corrupted """
    pass
