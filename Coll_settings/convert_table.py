#!/usr/bin/python

# script to convert R.Bruce tables for LHC/HLLHC impedance model.
# takes into account the coatings that might be present in different scenarios. Only TDI and TCDQ are considered.

import numpy as np
from string import replace
from io_lib import *
import csv
#dircollscan=np.array(['LHC_50cm_tight_6.5TeV_B1_fromCollimation','LHC_50cm_relaxed_6.5TeV_B1_fromCollimation','LHC_40cm_6.5TeV_B1_fromCollimation','LHC_inj_450GeV_B2_fromCollimation','LHC_inj_450GeV_B1_fromCollimation','LHC_ft_6.5TeV_B2_fromCollimation','LHC_ft_6.5TeV_B1_fromCollimation','LHC_80cm_6.5TeV_B2_fromCollimation','LHC_80cm_6.5TeV_B1_fromCollimation']);
dircollscan=np.array(['HLLHC_60cm_7TeV_B1_2016_fromCollimation'])

TDIscenario='TDI-2016'; #'TDI-2015', 'TDI-preLS1'
TCDQscenario='TCDQpostLS1'; # 'TCDQpreLS1' # TCDQ will be increased to 3 modules of 3m jaw length copper coated of 5um.
#comment_scenario='_2016';
comment_scenario='';
for name in dircollscan: 
	reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
	lista=[];
	for row in reader:
		row['Name']=row.pop('name');
		row['Halfgap[m]']=row.pop('halfgap[m]');
		row['Angle[rad]']=row.pop('angle[rad]');
		row['Betax[m]']=row.pop('betax[m]');
		row['Betay[m]']=row.pop('betay[m]');

		if 'TCSG' in row['Name'] or 'TCP' in row['Name'] or 'TCLIB' in row['Name']:
			# In Roderik tables these appears as C=Graphite but they are in CFC. The rest stay as it is
			row['Material']='CFC';

		if 'TDI' in row['Name']:
			if 'TDI-2015' in TDIscenario:
				# TDI coated of Cu and Ti block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(5e-6);
				newrow['Length[m]']=str(2.836);		
				newrow['Material']='Ti_in_TDI';
				newrow['Name']='TDI.4L2.B1.1';
				lista.append(newrow);

				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(2.836);		
				newrow['Material']='HBN';
				newrow['Name']='TDI.4L2.B1.1';
				lista.append(newrow);

				# Cu coated Al block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(2e-6);
				newrow['Length[m]']=str(0.6);
				newrow['Material']='CU300K_in_TDI';
				newrow['Name']='TDI.4L2.B1.2';
				lista.append(newrow);
				
				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(0.6);
				newrow['Material']='Al';
				newrow['Name']='TDI.4L2.B1.2';	
				lista.append(newrow);
				
				# Copper block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(0.7);
				newrow['Material']='Cu';
				newrow['Name']='TDI.4L2.B1.3';	
				lista.append(newrow);		

			elif 'TDI-2016' in TDIscenario:
				
				# TDI coated of Cu and Ti block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(2e-6);
				newrow['Length[m]']=str(2.826);		
				newrow['Material']='Cu300K_in_TDI';
				newrow['Name']='TDI.4L2.B1.1';
				lista.append(newrow);

				newrow=row.copy();
				newrow['Thickness[m]']=str(0.1e-6);
				newrow['Length[m]']=str(2.826);		
				newrow['Material']='Ti';
				newrow['Name']='TDI.4L2.B1.1';
				lista.append(newrow);

				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(2.826);		
				newrow['Material']='graphite';
				newrow['Name']='TDI.4L2.B1.1';
				lista.append(newrow);

				# Ti coated Al block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(1e-6);
				newrow['Length[m]']=str(0.6);
				newrow['Material']='Ti_in_TDI';
				newrow['Name']='TDI.4L2.B1.2';
				lista.append(newrow);
				
				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(0.6);
				newrow['Material']='Al';
				newrow['Name']='TDI.4L2.B1.2';	
				lista.append(newrow);
				
				# Copper block in TDI
				newrow=row.copy();
				newrow['Thickness[m]']=str(0.054);
				newrow['Length[m]']=str(0.7);
				newrow['Material']='CuCr1Zr';
				newrow['Name']='TDI.4L2.B1.3';	
				lista.append(newrow);		
		
		elif 'TCDQ' in row['Name']:
			# There are 3 modules, each of 3m for a total of 9m. 
			# Font: http://199.190.250.75/prepress/MOPPD081.PDF
			if 'TCDQpostLS1' in TCDQscenario:
				# Copper coating in TCDQA
				newrow=row.copy();
				newrow['Thickness[m]']=str(5e-6);
				newrow['Length[m]']=str(3);
				newrow['Material']='CU300K_in_TDI';	
				lista.append(newrow);		
		
				# CFC block in TCDQA
				newrow=row.copy();
				newrow['Thickness[m]']=str(3.5e-2);
				newrow['Length[m]']=str(3);
				newrow['Material']='CFC';
				lista.append(newrow);			
				
				# Graphite block in TCDQA
				newrow=row.copy();
				newrow['Thickness[m]']=str(4e-2);
				newrow['Length[m]']=str(3);
				newrow['Material']='graphite';
				lista.append(newrow);		

			if 'TCDQpreLS1' in TCDQscenario:
				
				# Graphite block in TCDQA
				newrow=row.copy();
				newrow['Thickness[m]']=str(7.5e-2);
				newrow['Length[m]']=str(6);
				newrow['Material']='graphite';
				lista.append(newrow);		
 				
		
		elif 'TCLIA' in row['Name']:
			row['Thickness[m]']=str(0.033);
			lista.append(row);
		else: 
			row['Thickness[m]']=str(0.025)
			lista.append(row);
	name_converted=name.replace('_fromCollimation','')+comment_scenario+'.txt';		
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
