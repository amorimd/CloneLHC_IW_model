#!/usr/bin/python

# script to add coatings on converted R.Bruce tables for LHC/HLLHC impedance model.
import sys
sys.path.append('/afs/cern.ch/user/n/nbiancac/ln_delphi/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/')
import numpy as np
from string import replace
from io_lib import *
import csv
from particle_param import *
from LHC_param import LHC_param

dircollscan=np.array(['LHC_inj_450GeV_B1_2015','LHC_inj_450GeV_B1_2016']);


half_gap=np.array([10e-3]);

for name in dircollscan: 
	reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
	lista=[];
	for row in reader:

		if 'TDI' in row['Name']:
			newrow=row.copy();
			newrow['Halfgap[m]']=str(half_gap[0]);
			lista.append(newrow);
			
		else:
			lista.append(row);

	
	
	name_converted=name.replace('inj','inj_TDI_hg'+str(half_gap[0]*1e3)+'mm')+'.txt';		
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
