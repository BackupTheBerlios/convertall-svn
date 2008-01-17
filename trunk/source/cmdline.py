#!/usr/bin/env python

#****************************************************************************
# cmdline.py, provides a class to read and execute command line arguments
#
# ConvertAll, a units conversion program
# Copyright (C) 2006, Douglas W. Bell
#
# This is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License, either Version 2 or any later
# version.  This program is distributed in the hope that it will be useful,
# but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
#*****************************************************************************

import sys
from option import Option
import optiondefaults
import unitdata

usage = ['',
         'Usage:',
         '',
         '   convertall [QT-OPTIONS]',
         '',
         '-or- (non-interactive):',
         '',
         '   convertall [QUANTITY] FROM_UNIT TO_UNIT',
         '']

options = 'h'
longOptions = ['help']

def parseArgs(opts, args):
    """Parse the command line and output conversion results"""
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            printUsage()
            return
    options = Option('convertall', 20)
    options.loadAll(optiondefaults.defaultList)
    unitData = unitdata.UnitData()
    try:
        unitData.readData()
    except unitdata.UnitDataError, text:
        print 'Error in unit data - %s' % text
        sys.exit(1)


def printUsage():
    """Print usage text"""
    print '\n'.join(usage)
