#!/usr/bin/env python

#****************************************************************************
# icons.py, provides xpm icons
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
from PyQt4 import QtCore, QtGui

convert = [
    "16 16 5 1",
    " 	c None",
    ".	c #000000",
    "+	c #C9C12C",
    "@	c #C42727",
    "#	c #6F6FF2",
    "  @@@@@..#####  ",
    " @@@@@@..###### ",
    "@@...@@..#######",
    "@@.@@......#####",
    "@@..@@@..##...##",
    "@.@@.@@..####.##",
    "@.@@.@@..###..##",
    "@.@@.@@..##.##.#",
    ".@@@@.@..##.##.#",
    ".@@@@.@..##.##.#",
    ".@++@.@..#.####.",
    "......@..#.#++#.",
    "@....@@..#.#++#.",
    "@@..@@@..#......",
    " @@@@@@..##.... ",
    "  @@@@@..###..  "]

helpback = [
    "16 14 2 1",
    "       c None",
    "+      c #0000A0",
    "                ",
    "     ++         ",
    "    ++          ",
    "   ++           ",
    "  ++            ",
    " ++             ",
    "++++++++++++++  ",
    "++++++++++++++  ",
    " ++             ",
    "  ++            ",
    "   ++           ",
    "    ++          ",
    "     ++         ",
    "                "]
    
helpforward = [
    "16 14 2 1",
    "       c None",
    "+      c #0000A0",
    "                ",
    "         ++     ",
    "          ++    ",
    "           ++   ",
    "            ++  ",
    "             ++ ",
    "  ++++++++++++++",
    "  ++++++++++++++",
    "             ++ ",
    "            ++  ",
    "           ++   ",
    "          ++    ",
    "         ++     ",
    "                "]

helphome = [
    "16 14 2 1",
    "       c None",
    "+      c #0000A0",
    "       ++       ",
    "      ++++      ",
    "     ++  ++     ",
    "    ++    ++    ",
    "   ++      ++   ",
    "  ++        ++  ",
    " ++          ++ ",
    " ++          ++ ",
    " ++          ++ ",
    " ++          ++ ",
    " ++          ++ ",
    " ++          ++ ",
    " ++++++++++++++ ",
    " ++++++++++++++ "]

iconList = ['convert', 'helpback', 'helpforward', 'helphome']
iconDict = {}

def setupIcons():
    """Create icons from xpm data"""
    global iconDict
    for name in iconList:
        iconDict[name] = QtGui.QIcon(QtGui.QPixmap(globals()[name]))
