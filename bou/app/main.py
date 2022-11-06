""" bou.cli.main
    ~~~
    The CLI to the bou library.
    @see bou.acts.<method>.<method>() for implementations.
"""

import bou.app.core
import bou.app.helpers
from bou.constants import ASTERISK, BOU, DOT


def main():
    """ CLI entrypoint

    Loads bou.*.cli command specific submodules, then runs
    """
    ANY_SUBMODULE_CLI = f'{BOU}{DOT}{ASTERISK}{DOT}cli'

    bou.app.helpers.load_modules(ANY_SUBMODULE_CLI)
    bou.app.core.main()


if __name__ == "__main__":
    main()
