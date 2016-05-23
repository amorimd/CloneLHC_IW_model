#!/usr/bin/python

# script to add coatings on converted R.Bruce tables for LHC/HLLHC impedance model.

import numpy as np
from string import replace
from io_lib import *
import csv


dircollscan=np.array(['HL-LHC_15cm_7TeV_baseline_B1']);

for coat in np.array([5]): #micron
	case=str(coat)+'um'+'Cu+MoC_IP7'

	for name in dircollscan: 
		reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
		lista=[];
		for row in reader:
			if '5umMo+CFC_IP3+IP7' in case:

				if 'TCSG' in row['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(5e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='CFC';
					lista.append(newrow);
				else:
					lista.append(row);
			
			if '5umMo+MoC_IP3+IP7' in case:

				if 'TCSG' in row['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(5e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);

			
			if '5umMo+CFC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(5e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='CFC';
					lista.append(newrow);
				else:
					lista.append(row);

				
			if 'TiB2+MoC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='TiB2';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);

			if 'TiN+CFC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='TiN';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='CFC';
					lista.append(newrow);
				else:
					lista.append(row);

			if 'Mo+CFC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='CFC';
					lista.append(newrow);
				else:
					lista.append(row);
			if 'Cu+CFC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Cu300K_layer';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='CFC';
					lista.append(newrow);
				else:
					lista.append(row);
			if 'TiN+MoC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='TiN';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);

			if 'Mo+MoC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);
			if 'Cu+MoC_IP7' in case:

				if 'TCSG' in row['Name'] and '7.B1' in row ['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Cu300K_layer';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);
			
			if 'TiN+MoC_5-TCSG' in case:
				if 'TCSG.6R7' in row ['Name'] or 'TCSG.D4L7' in row ['Name'] or 'TCSG.A6L7' in row ['Name'] or 'TCSG.B4L7' in row ['Name'] or 'TCSG.B5L7' in row['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='TiN';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);

			if 'Mo+MoC_5-TCSG' in case:

				if 'TCSG.6R7' in row ['Name'] or 'TCSG.D4L7' in row ['Name'] or 'TCSG.A6L7' in row ['Name'] or 'TCSG.B4L7' in row ['Name'] or 'TCSG.B5L7' in row['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Mo';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);
			if 'Cu+MoC_5-TCSG' in case:

				if 'TCSG.6R7' in row ['Name'] or 'TCSG.D4L7' in row ['Name'] or 'TCSG.A6L7' in row ['Name'] or 'TCSG.B4L7' in row ['Name'] or 'TCSG.B5L7' in row['Name']:
					newrow=row.copy();
					newrow['Thickness[m]']=str(coat*1e-6);
					newrow['Material']='Cu300K_layer';
					lista.append(newrow);
					
					newrow=row.copy();
					newrow['Material']='MoC';
					lista.append(newrow);
				else:
					lista.append(row);


		name_converted=name+'_'+case+'.txt';		
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
