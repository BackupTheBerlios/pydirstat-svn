#!/usr/bin/env python

import string
import os

def make_version_files():
    version=string.strip(open("VERSION").readline())

    # src/dirstat/__version__.py : version for python module

    handle = open(os.path.join('src','dirstat','__version__.py'),'wt')
    handle.write('__version__ = "%s"\n' % version)
    handle.close()

    # src/dirstat/__version__.py : version for NSIS Windows-installer

    handle = open(os.path.join('nsis','version.nsi'),'wt')
    handle.write('!define PRODUCT_VERSION "%s"\n' % version)
    handle.close()

    # setup.py use it's own way to read VERSION

def main():
    make_version_files()

main()
