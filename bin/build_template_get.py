""" <bou_root>/bin/build_template_get.py
    ~~~
    Builds bou.template.get by parsing bou.res for appropriate files.
"""

import pathlib

from jinja2 import Environment, FileSystemLoader, select_autoescape

import bou.constants as const
import bou.modules
import bou.template.helpers

# Locate all known templates
template_module = bou.modules.load(f'{const.BOU}{const.DOT}{const.RES}')
public_templates = bou.modules.files_in(template_module).glob(
    f'{const.ASTERISK}{const.DOT_TEMPLATE}'
)

# Lexically sort the methods.
template_vars = {
    'public_templates': sorted(
        [
            each.stem
            for each
            in public_templates
        ]
    )
}

template_vars.update(
    bou.template.helpers.constants()
)

# Run the template
template = Environment(
    autoescape=select_autoescape(),
    loader=FileSystemLoader(['bin/', '.'])
).get_template('build_template_get.template').render(template_vars)


# Output the results
template_module = bou.modules.path('bou.template')

get_py = pathlib.Path(template_module).parent / 'get.py'
get_py.write_text(template)
