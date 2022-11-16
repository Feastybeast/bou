""" bou.template.helpers
    ~~~
    Support methods for templating.
"""

from jinja2 import Environment, PackageLoader, select_autoescape

import bou.constants as const
from bou.types import TemplateVars


def apply(template: str, **template_vars: TemplateVars) -> str:
    """ Generates a Jinja template from :values:

    :param template: to act upon.
    :param template_vars: to incorporate.

    :returns: the processed template.
    """
    merged_vars = template_vars.copy()
    merged_vars.update(constants())

    return Environment(
        autoescape=select_autoescape(),
        loader=PackageLoader(const.BOU, const.RES)
    ).get_template(template).render(**merged_vars)


def constants() -> dict:
    """ The dictionary of constants used by bou.template """
    return {
        each: getattr(const, each)
        for each
        in filter(
            lambda x: not x.startswith('__'),
            dir(const)
        )
    }
