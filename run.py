#! /usr/bin/env python
# Boinc cointainer run script
# Copyright (C) 2014 vhb
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import subprocess
import shlex
import os


key = '1687b9802cb646b956c79494e9ebc88e'

def usage():
    print 'Usage: server email password account-name'

def main():
    cmd = 'boinc -attach_project {:s} 949787_15ca7825fb58f9d01b6ad15221c3f048 \\\
            '.format(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
            )
    print cmd
    cmd = shlex.split(cmd)
    subprocess.call(cmd)

if __name__ == '__main__':
    #if '--help' in sys.argv or len(sys.argv) != 5:
        #usage()
    #else:
    main()
