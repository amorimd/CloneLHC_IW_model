import time
import pytimber
import pyoptics as opt
import numpy as np
import csv

mdb=pytimber.LoggingDB(source='mdb')

filln=5146
beam=1

OpticsDir = '/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/LHC_IW_model/Optics/2016/LHC-HighBeta/' # path for reference optics
CollDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/LHC_IW_model/Coll_settings/'
name = 'LHC_ft_6.5TeV_B1_2016' #name of a recent collimator file
newname = 'LHC_highbeta_6.5TeV_B1'
time_str = '2016-07-31 19:20:00'


scenario_scan=[{'time' : time_str}]

tfs = opt.optics.open((OpticsDir+'twiss_lhcb%d.tfs')%beam)
    
for scenario in scenario_scan:    
    
    en=3.5e-6 # reference normalized emittance
    gamma=tfs.param['gamma']; 
    
    print 'emittance = %.1f'%(en*1e6), 'gamma = %d'%gamma
        
    comment='fill_'+str(filln)
    
    reader = csv.DictReader(open(CollDir+name+'.txt'),delimiter='\t')
    lista=[];
    for row in reader:
        newrow=row.copy();

        phi=eval(row['Angle[rad]'])
        nsig=eval(row['nsig'])
        
        if 'TDI' in row['Name'] and beam==2:
            coll= mdb.search('TDI.4R8:MEAS_LVDT_GD')[0]
            bety= tfs.bety[tfs.pattern('TDI.4R8.B2')]
            betx= tfs.betx[tfs.pattern('TDI.4R8.B2')]
        
        elif 'TDI' in row['Name'] and beam==1:
            coll= mdb.search('TDI.4L2:MEAS_LVDT_GD')[0]
            bety= tfs.bety[tfs.pattern('TDI.4L2.B1')]
            betx= tfs.betx[tfs.pattern('TDI.4L2.B1')]
        
        elif 'TCDQ' in row['Name']:
            coll= mdb.search('TCDQA.%B'+str(beam)+':MEAS_LVDT_LD')[0]
            bety= tfs.bety[tfs.pattern(row['Name']+str(beam))]
            betx= tfs.betx[tfs.pattern(row['Name']+str(beam))]
        
        else:
            coll= mdb.search(row['Name']+'%MEAS_LVDT_GD')[0]
            bety= tfs.bety[tfs.pattern(row['Name'])]
            betx= tfs.betx[tfs.pattern(row['Name'])]
        
        
        data=mdb.get(coll,scenario['time'])
        tt,fullgap=data[coll]; tt+=2*3600
        hgap_new=fullgap/2*1e-3;
        
        newrow['Halfgap[m]']='%.5f'%(hgap_new);
        sigma = np.sqrt(en/gamma*betx*np.cos(phi)**2+en/gamma*bety*np.sin(phi)**2)
        nsig = hgap_new/sigma
        newrow['nsig']='%.3f'%(nsig);
        lista.append(newrow);
        print row['Name'], str(hgap_new)+' m', str(betx)+' m', str(bety)+' m \n',
    name_converted=newname+'_'+comment+'.txt'
    
    with open(CollDir+name_converted, 'wb') as f:
        # Assuming that all dictionaries in the list have the same keys.
        headers = lista[0].keys()
        csv_data = [headers];
        for d in lista:
            csv_data.append([d[h] for h in headers])
        writer = csv.writer(f,delimiter='\t')
        writer.writerows(csv_data)
    print name+' converted:'
    print name_converted