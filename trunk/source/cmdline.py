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
import option
import optiondefaults
import unitdata
import unitgroup

usage = ['',
         'Usage:',
         '',
         '   convertall [QT-OPTIONS]',
         '',
         '-or- (non-interactive):',
         '',
         '   convertall [QUANTITY] FROM_UNIT TO_UNIT',
         '']

availOptions = 'h'
availLongOptions = ['help']

def parseArgs(opts, args):
    """Parse the command line and output conversion results"""
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            printUsage()
            return
    options = option.Option('convertall', 20)
    options.loadAll(optiondefaults.defaultList)
    data = unitdata.UnitData()
    try:
        data.readData()
    except unitdata.UnitDataError, text:
        print 'Error in unit data - %s' % text
        sys.exit(1)
    numStr = args[0]
    try:
        float(numStr)
        del args[0]
    except (ValueError, IndexError):
        numStr = '1.0'
    fromUnit = None
    if args:
        fromUnit = getUnit(data, options, args.pop(0))
    toUnit = None
    if args:
        toUnit = getUnit(data, options, args[0])
    while True:
        while not fromUnit:
            fromText = raw_input('Enter from unit -> ')
            if not fromText:
                return
            fromUnit = getUnit(data, options, fromText)
        while not toUnit:
            toText = raw_input('Enter to unit -> ')
            if not toText:
                return
            toUnit = getUnit(data, options, toText)
        if fromUnit.categoryMatch(toUnit):
            while True:
                print '%s %s = %s %s' % (numStr, fromUnit.unitString(),
                                         fromUnit.convertStr(float(numStr),
                                                             toUnit),
                                         toUnit.unitString())
                print
                rep = raw_input('Enter number, [n]ew, [r]everse or [q]uit -> ')
                if not rep or rep[0] in ('q', 'Q'):
                    return
                if rep[0] in ('r', 'R'):
                    fromUnit, toUnit = toUnit, fromUnit
                elif rep[0] in ('n', 'N'):
                    fromUnit = None
                    toUnit = None
                    numStr = '1.0'
                    print
                    break
                else:
                    try:
                        float(rep)
                        numStr = rep
                    except ValueError:
                        pass
        else:
            print 'Units %s and %s are not compatible' % \
                         (fromUnit.unitString(), toUnit.unitString())
            fromUnit = None
            toUnit = None

def getUnit(data, options, text):
    """Create unit from text, check unit is valid,
       return reduced unit or None"""
    unit = unitgroup.UnitGroup(data, options)
    unit.update(text)
    if unit.groupValid():
        unit.reduceGroup()
        return unit
    print '%s is not a valid unit' % text
    return None

def printUsage():
    """Print usage text"""
    print '\n'.join(usage)
