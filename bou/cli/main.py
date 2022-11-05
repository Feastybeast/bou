""" bou.cli.main
    ~~~
    The CLI to the bou library.
    @see bou.acts.<method>.<method>() for implementations.
"""

import click

from bou.constants import ASTERISK, BOU, DOT
import bou.modules


@click.group()
def main():
    pass


ANY_SUBMODULE_CLI = f'{BOU}{DOT}{ASTERISK}{DOT}cli'

for each in bou.modules.matching(ANY_SUBMODULE_CLI):
    bou.modules.load(each)


if __name__ == "__main__":
    main()
