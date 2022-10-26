#!/usr/bin/env python3

from setuptools import setup

DESC = "python migrations for sqlite databases"
LONG_DESC = """
Inspired by clutchski's caribou migrations library

See http://github.com/clutchski/caribou for the original implementation.
"""
AUTHOR = 'Jay Ripley'
EMAIL = 'jay@clearlyoutplayed.com'
LICENSE = 'MIT'
NAME = 'bou'
URL = 'http://github.com/Feastybeast/bou'
VERSION = '2.0.0'

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    long_description=LONG_DESC,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    platforms='any',
    py_modules=['bou'],
    entry_points={
        'console_scripts': [
            'bou=bou.cli.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Topic :: Database',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
