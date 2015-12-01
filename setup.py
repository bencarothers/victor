#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='victor',
      version='1.0',
      long_description=open('README.md').read(),
      author='Ben Carothers',
      author_email='benjamin.carothers13@ncf.edu',
      url='https://github.com/bencarothers/victor',
      packages=['victor', 'victor.interface', 'victor.tests'],
      test_suite='victor.tests',
      install_requires=[
            'nose>=1.3.7',
            'coverage>=4.0.3',
            'flask>=0.10.1',
          ],
      )
