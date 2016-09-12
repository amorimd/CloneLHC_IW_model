#!/usr/bin/python

import sys
import numpy as np
import csv
import warnings
import argparse

parser = argparse.ArgumentParser(description='Change sigma in IR7.')
parser.add_argument('-tcp', action = 'store', dest = 'tcp', type = float, help='numer of sigma at TCP7')
parser.add_argument('-tcsg', action = 'store', dest = 'tcsg', type = float, help='numer of sigma at TCSG7')

args = parser.parse_args()

en=3.5e-6 # emittance for collgaps
gamma=6927. # gamma at 6.5TeV

nsig_new_TCP7, nsig_new_TCSG7 = args.tcp, args.tcsg

dircollscan=np.array(['LHC_ft_6.5TeV_B1_2016']);

for name in dircollscan: 
    reader = csv.DictReader(open(name+'.txt'),delimiter='\t')
    lista=[];
    for row in reader:
        print row['Name']
        if 'TCP' in row['Name'] and '7' in row['Name']:
            print row['Name']
            newrow=row.copy();
            
            
            bety=eval(row['Betay[m]'])
            betx=eval(row['Betax[m]'])
            phi=eval(row['Angle[rad]'])
            nsig=eval(row['nsig'])
            sigma=np.sqrt(en/gamma*betx*np.cos(phi)**2+en/gamma*bety*np.sin(phi)**2)
            hgap=sigma*nsig
            if abs(hgap-eval(row['Halfgap[m]']))>1e-4:
                warnings.warn('Warning: it seems the calculated gap differs the nominal gap in table!')
            
            nsig_new=nsig_new_TCP7
            hgap_new=sigma*nsig_new
            
            newrow['Halfgap[m]']='%.5f'%(hgap_new);
            newrow['nsig']='%.1f'%(nsig_new);
            lista.append(newrow);
        
        elif 'TCSG' in row['Name'] and '7' in row['Name']:
            print row['Name']
            newrow=row.copy();
            
            en=3.5e-6
            gamma=6927.
            bety=eval(row['Betay[m]'])
            betx=eval(row['Betax[m]'])
            phi=eval(row['Angle[rad]'])
            nsig=eval(row['nsig'])
            sigma=np.sqrt(en/gamma*betx*np.cos(phi)**2+en/gamma*bety*np.sin(phi)**2)
            hgap=sigma*nsig
            if abs(hgap-eval(row['Halfgap[m]']))>1e-4:
                warnings.warn('Warning: it seems the calculated gap differs the nominal gap in table!')
            
            nsig_new=nsig_new_TCSG7
            hgap_new=sigma*nsig_new
            
            newrow['Halfgap[m]']='%.5f'%(hgap_new);
            newrow['nsig']='%.1f'%(nsig_new);
            lista.append(newrow);
            
        else:
            lista.append(row);
            
    name_converted=name+'_TCP7_%.1fsig_TCSG7_%.1fsig.txt'%(nsig_new_TCP7,nsig_new_TCSG7)
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

# row.items()
