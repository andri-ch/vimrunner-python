#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-


import io
import sys
from setuptools import setup
#from distutils.core import setup
from setuptools.command.test import test as TestCommand


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


class PyTestCommand(TestCommand):
    """ Command to run unit py.test unit tests
    """
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run(self):
        import pytest
        rcode = pytest.main(self.test_args)
        sys.exit(rcode)


setup(
    name='vimrunner',
    version='1.0.1',
    description='Implements a client and server interface useful for controlling a Vim server programatically.',
    long_description=read('README.md'),
    author='Andrei Chiver',
    author_email='andreichiver@gmail.com',
    license='MIT',
    url='https://github.com/andri-ch/vimrunner.py',
    provides=['vimrunner'],
    py_modules=['vimrunner'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='test Vim editor server plugin',
    tests_require=[
        'pytest',
    ],
    cmdclass={
        'test': PyTestCommand,
    },
)
