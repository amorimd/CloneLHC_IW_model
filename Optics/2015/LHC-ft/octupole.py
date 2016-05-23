#!/usr/bin/env python

from pyoptics import *
from string import *
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("optics", help="optics file")
args = parser.parse_args()
filename=args.optics;

t=optics.open(filename);
itemlist=t.dumplist('MO','s l betx bety dx dy');

outfile=open('octupole.dat', 'w');
outfile.write("\n".join(itemlist))
outfile.close();


