#!/usr/bin/env python
"""
****************************************************************************
 convertall.py, the main program file

 ConvertAll, a units conversion program
 Copyright (C) 2006, Douglas W. Bell

 This is free software; you can redistribute it and/or modify it under the
 terms of the GNU General Public License, either Version 2 or any later
 version.  This program is distributed in the hope that it will be useful,
 but WITTHOUT ANY WARRANTY.  See the included LICENSE file for details.
*****************************************************************************
"""

__progname__ = 'ConvertAll'
__version__ = '0.4.0'
__author__ = 'Doug Bell'

dataFilePath = None    # modified by install script if required
helpFilePath = None    # modified by install script if required

import sys
from PyQt4 import QtGui
import convertdlg


if __name__ == '__main__':
    userStyle = '-style' in ' '.join(sys.argv)
    app = QtGui.QApplication(sys.argv)
    if not userStyle and not sys.platform.startswith('win'):
        QtGui.QApplication.setStyle('plastique')
    win = convertdlg.ConvertDlg()
    win.show()
    app.exec_()
