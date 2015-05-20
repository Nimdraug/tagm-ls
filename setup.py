#!/usr/bin/env python2
from setuptools import setup

setup(
    name = 'tagm-ls',
    version = '0.1-dev',

    maintainer = u'Martin Hult\xe9n-Ashauer',
    maintainer_email = 'tagm@nimdraug.com',
    url = 'http://github.com/Nimdraug/tagm-ls',
    license = 'MIT',
    description = 'Script to list files and their tags. Inspired by the ls command.',

    install_requires = [
        'tagm==0.2-dev'
    ],

    py_modules = [
        'tagm_ls'
    ],
    entry_points = {
        'console_scripts': [
            'tagm-ls = tagm_ls:main'
        ]
    }
)
