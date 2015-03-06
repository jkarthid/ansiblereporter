
import os
import glob

from setuptools import setup, find_packages

VERSION='1.2'

setup(
    name = 'ansiblereporter',
    keywords = 'system management ansible automation reporting',
    description = 'Scripts for ansible to report host output data',
    author = 'Ilkka Tuohela',
    author_email = 'hile@iki.fi',
    version = VERSION,
    url = 'http://tuohela.net/packages/ansiblereporter',
    license = 'PSF',
    zip_safe = False,
    packages = find_packages(),
    scripts = glob.glob('bin/*'),
    install_requires = (
        'ansible>=1.8.4',
        'systematic>=4.2.6',
        'seine>=3.0.0',
        'termcolor',
    ),
)

