#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
#filename = sys.argv[1]
filename = "ls8\\examples\\mult.ls8"
cpu.load(filename)
cpu.run()