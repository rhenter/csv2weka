#!/usr/bin/env python
# encoding: utf-8
import codecs
import os
import re
from setuptools import find_packages, setup, Command

from csv2weka import __version__

here = os.path.dirname(os.path.abspath(__file__))
version = __version__
description = (
    'CSV2ARFF is a simple analize tool written in python using '
    'One Hot Encoding to Label classification.'
)


class VersionCommand(Command):
    description = 'Show library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


# Get the long description
with codecs.open(os.path.join(here, 'README.rst')) as f:
    long_description = '\n{}'.format(f.read())

# Requirements
with codecs.open(os.path.join(here, 'requirements.txt')) as f:
    install_requirements = [line.split('#')[0].strip() for line in f.readlines() if not line.startswith('#')]

with codecs.open(os.path.join(here, 'requirements-dev.txt')) as f:
    tests_requirements = [line.replace('\n', '') for line in f.readlines() if not line == '-r requirements.txt\n']


setup(
    author='Rafael Henter',
    author_email='rafael@henter.com.br',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Education',
    ],
    cmdclass={'version': VersionCommand},
    description=description,
    entry_points='''
        [console_scripts]
        csv2weka=csv2weka.__main__:cli
    ''',
    install_requires=install_requirements,
    keywords='Weka',
    license='MIT',
    long_description=long_description,
    name='csv2weka',
    packages=find_packages(exclude=['requirements']),
    version=version,
)
