#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djlibcloud

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djlibcloud.__version__

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        print("Please install wheel: pip install wheel")
        sys.exit()
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='dj-libcloud',
    version=version,
    description="""Adds easy python 3 and 2.7 support to Django for management of static assets.""",
    long_description=readme + '\n\n' + history,
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/dj-libcloud',
    packages=[
        'djlibcloud',
    ],
    include_package_data=True,
    install_requires=[
        'apache-libcloud>=0.14.1',
        'django>=1.6.0'
    ],
    license="BSD",
    zip_safe=False,
    keywords='dj-libcloud',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)