#!/usr/bin/env python3

import os
import sys
import subprocess

# Test important imports
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
import sklearn

if __name__ == '__main__':
    # Get first program argument, if it exists
    arg = sys.argv[1] if len(sys.argv) >= 2 else ''

    # Get the current computer's name
    comp_name = subprocess.check_output(['uname', '-n']).decode('ascii').strip()

    # Write something to stdout
    print("Hello from %s, arg = '%s'" % (comp_name, arg))

    # Check project-home access
    with open(os.path.expanduser('~/project-home/test.txt')) as f:
        print('Checking project-home access: %s' % f.read())

    # Create an output file of some sort
    with open('test-hello-%s.out' % arg, 'w') as outfile:
        print("%s, arg = '%s'" % (comp_name, arg), file=outfile)
