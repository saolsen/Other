#!usr/bin/env python
"""
    addmon
    A Little Script that I use to add and remove my external monitor
    uses xrandr, hardcoded with my monitor setup,
    feel free to modify for your own use.
"""

__author__="Stephen Olsen"

import sys
import os

try:
    option = sys.argv[1]
    if option == 'on':
        os.system("xrandr --output VGA1 --mode 1600x900 --right-of LVDS1")
    elif option == 'off':
        os.system("xrandr --output VGA1 --off")
    else:
        print "'" + option + "' is not a valid option. 'on' or 'off'"

except IndexError:
    print "Please run 'addmon on' or 'addmon off'"
