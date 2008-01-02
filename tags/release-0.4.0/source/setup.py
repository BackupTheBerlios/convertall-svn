#!/usr/bin/env python
from distutils.core import setup
import py2exe

setup(name='convertall',
      windows = [{'script': 'convertall.py',
                  'icon_resources': [(1, 'convertall.ico')]}],
      options = {'py2exe': {'includes': ['sip'],
                            'dist_dir': 'dist/lib'}})

# run with: python setup.py py2exe
