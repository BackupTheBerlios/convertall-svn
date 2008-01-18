#!/usr/bin/env python
"""
****************************************************************************
 convertall.py, the main program file

 ConvertAll, a units conversion program
 Copyright (C) 2008, Douglas W. Bell

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
iconPath = None        # modified by install script if required

import sys
import signal
import getopt
from PyQt4 import QtGui
import cmdline
import convertdlg


if __name__ == '__main__':
    userStyle = '-style' in ' '.join(sys.argv)
    app = QtGui.QApplication(sys.argv)
    try:
        opts, args = getopt.gnu_getopt(sys.argv, cmdline.availOptions,
                                       cmdline.availLongOptions)
    except getopt.GetoptError:
        cmdline.printUsage()
        sys.exit(2)
    args = args[1:]

    if opts or args:
        cmdline.parseArgs(opts, args)
    else:
        if not userStyle and not sys.platform.startswith('win'):
            QtGui.QApplication.setStyle('plastique')
        win = convertdlg.ConvertDlg()
        win.show()
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        app.exec_()
