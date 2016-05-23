#!/usr/bin/python

# script to move TCL collimators.
import sys
sys.path.append('/afs/cern.ch/user/n/nbiancac/ln_delphi/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/')
import numpy as np
from string import replace
from io_lib import *
import csv
from particle_param import *
from LHC_param import LHC_param

dircollscan=np.array(['LHC_50cm_tight_6.5TeV_B1_2016','LHC_50cm_relaxed_6.5TeV_B1_2016','LHC_40cm_6.5TeV_B1_2016','LHC_80cm_6.5TeV_B1_2015']);


half_gap=999; # fully retract TCLs
nsigma=999;
comment_scenario='_TCL_out';

for name in dircollscan: 
	reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
	lista=[];
	for row in reader:

		if 'TCL.' in row['Name']:
			newrow=row.copy();
			newrow['Halfgap[m]']=str(half_gap);
			newrow['nsig']=str(nsigma)
			lista.append(newrow);
			
		else:
			lista.append(row);

	
	
	name_converted=name+comment_scenario+'.txt';		
	with open(name_converted, 'wb') as f:
	      # Assuming that all dictionaries in the list have the same keys.
	      headers = lista[0].keys()
	      csv_data = [headers];
	      for d in lista:
		    csv_data.append([d[h] for h in headers])
	      writer = csv.writer(f,delimiter='\t')
	      writer.writerows(csv_data)
	print name+' converted:'
	print name_converted
