# -*- coding: utf-8 -*-
"""This is a custom local plugin to ad extra functionality to site."""

# Third party imports
from setuptools import setup


setup(
    name='lektor-website-plugin',
    author='Taylor',
    author_email='Taylor@openddd.com',
    version='0.1',
    license='MIT',
    py_modules=['lektor_website_plugin'],
    install_requires=['Lektor', 'MarkupSafe', 'Pygments'],
    entry_points={
        'lektor.plugins': [
            'website-plugin = lektor_website_plugin:WebsitePlugin',
        ]
    }
)
