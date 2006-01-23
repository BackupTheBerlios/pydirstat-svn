#!/usr/bin/env python

from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1 :
    sys.argv += ['py2exe']

# setup(
#     name='pydirstat',
#     console=['pdssvg.py','pdsswf.py','pdshtml.py'],
#     icon='../res/pydirstat.ico',
# )

setup(
    name='pdshtml',
    console=['pdshtml.py','pds-config.py'],
    icon='../res/pydirstat.ico',
    options={
        "py2exe" : {
            "includes" : ["encodings","encodings.latin_1",],
            "excludes": [],
            }
        }
)
