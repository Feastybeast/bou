""" bou.template """

from jinja2 import Environment, PackageLoader


def apply(template: str, values: dict) -> str:
    """ Generates a Jinja template from :values:

    :param template: to act upon.
    :param values: to process.

    :returns: the processed template.
    """
    template = TEMPLATE_ENV.get_template(template)

    return template.render(**values)


TEMPLATE_ENV = Environment(
    loader=PackageLoader('bou', 'res')
)
