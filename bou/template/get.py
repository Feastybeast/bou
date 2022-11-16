""" bou.template.get
    ~~~
    Maps publicly available bou.res templates as .{template}()

    THIS FILE IS BUILT VIA /bin/build_template_api.py. DO NOT MANUALLY EDIT IT.
"""

from bou.constants import DOT_TEMPLATE
import bou.template.helpers
from bou.types import TemplateVars


def boufile(**template_vars: TemplateVars) -> str:
    """ Renders the boufile template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'boufile{ DOT_TEMPLATE }', **template_vars
    )


def downgrade(**template_vars: TemplateVars) -> str:
    """ Renders the downgrade template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'downgrade{ DOT_TEMPLATE }', **template_vars
    )


def initial_downgrade(**template_vars: TemplateVars) -> str:
    """ Renders the initial_downgrade template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'initial_downgrade{ DOT_TEMPLATE }', **template_vars
    )


def initial_upgrade(**template_vars: TemplateVars) -> str:
    """ Renders the initial_upgrade template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'initial_upgrade{ DOT_TEMPLATE }', **template_vars
    )


def migration(**template_vars: TemplateVars) -> str:
    """ Renders the migration template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'migration{ DOT_TEMPLATE }', **template_vars
    )


def upgrade(**template_vars: TemplateVars) -> str:
    """ Renders the upgrade template.

    :param template_vars: to incorporate.
    :returns: the rendered template.
    """
    return bou.template.helpers.apply(
        f'upgrade{ DOT_TEMPLATE }', **template_vars
    )
