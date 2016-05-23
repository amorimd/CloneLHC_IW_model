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

dircollscan=np.array(['LHC_40cm_6.5TeV_2sig_retr_TCT8.8_TCL.6R5_10sigma_B1']);


# beam parameters   
e,m0,c,E0=proton_param();
# machine parameters
machine,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h=LHC_param(E0,E=6.5e12);

nsigma_vec=np.array([10,20,30,40]);
epsilon_n=3.5e-6;
TCL5_betx=213.6070407;

for nsigma in nsigma_vec:
	half_gap=nsigma*np.sqrt(epsilon_n/gamma*TCL5_betx);
	for name in dircollscan: 
		reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
		lista=[];
		for row in reader:

			if 'TCL.5R5.B1' in row['Name']:
				newrow=row.copy();
				newrow['Halfgap[m]']=str(half_gap);
				newrow['nsig']=str(nsigma)
				lista.append(newrow);
				
			else:
				lista.append(row);

		
		
		name_converted=name.replace('TCL.6R5_10sigma','TCL.6R5_10sigma_TCL.5R5_'+str(nsigma)+'sigma')+'.txt';		
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
