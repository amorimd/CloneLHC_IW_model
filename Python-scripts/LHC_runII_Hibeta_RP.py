#!/usr/bin/python
# use "./LHC_runII.py launch" to launch the impedance model calculation
# use "./LHC_runII.py retrieve" to retrieve the impedance model results
# use "./LHC_runII.py restore launch" to restore impedance model results and launch DELPHI scans
# use "./LHC_runII.py restore retrieve" to retrieve the results of DELPHI scans

import sys
import commands

if len(sys.argv)>2: lxplusbatchImp=str(sys.argv[1]);lxplusbatchDEL=str(sys.argv[2]);
elif len(sys.argv)>1: lxplusbatchImp=str(sys.argv[1]);lxplusbatchDEL=None;
else: lxplusbatchImp=None;lxplusbatchDEL=None;
print lxplusbatchImp,lxplusbatchDEL;

from string import *
import time
import numpy as np
from copy import deepcopy
#import pylab
import os,re
path_here=os.getcwd()+"/";
from io_lib import *
from tables_lib import select_in_table
from particle_param import *
from Impedance import *
from DELPHI import *
from LHC_param import *
from LHC_imp import *
from LHC_coll_imp import *
import pickle as pkl
import inspect
import datetime

if __name__ == "__main__":

    # beam parameters
    e,m0,c,E0=proton_param();

    # machine parameters
    machine2save='LHC'; 
    beam="1";

    # subdirectory (inside DELPHI_results/[machine2save]) where to put the results
    RunDir='RunII/';
    ResultDir='/afs/cern.ch/work/d/damorim/work/DELPHI_results/'+machine2save+'/'+RunDir;
    ResultDir2012='/afs/cern.ch/work/d/damorim/work/DELPHI_results/'+machine2save+'/'+RunDir;
    os.system("mkdir -p "+ResultDir);

    # flags for plotting and DELPHI
    flagdamperimp=0; # 1 to use frequency dependent damper gain (provided in Zd,fd)
    strnorm=[''];
    flagnorm=0; # 1 if damper matrix normalized at current chromaticity (instead of at zero chroma)
    flagplot=True; # to write impedance files by elements
    nevery=1; # downsampling of the impedance (take less points than in the full model)
    wake_calc=False; # True -> compute wake as well (otherwise only imp.)


    kmax=1; # number of converged eigenvalues (kmax most unstable ones are converged)
    kmaxplot=200; # number of kept and plotted eigenvalues (in TMCI plot)
    col=['b','r','g','m','k','c','y','b--','r--','g--','m--','k--','c--','y--']; # colors
    linetype=['-','--',':'];

    # scan definition
    # scenarioscan=np.array([('LHC_ft_6.5TeV_B1_2016_TCP7_5.5sig_TCSG7_%.1fsig')%(sig) for sig in np.array([6,7,8,9,10])]) # name in Coll_settings without ".txt"
    #scenarioscan = np.array(['LHC_inj_450GeV_B1_2016']) 
    scenarioscan=np.array(['LHC_highbeta_6.5TeV_B2_fill5313_20h20_fill_5313_2016-09-19_20:00:00','LHC_highbeta_6.5TeV_B2_fill5313_20h20_fill_5313_2016-09-19_20:00:00','LHC_highbeta_6.5TeV_B2_fill5313_20h20_fill_5313_2016-09-19_20:00:00'])
    RP_scenarioscan = np.array(['LHC_RP_highbeta_6.5TeV_B2_fill_5313_2016-09-19_21:15:00','LHC_RP_highbeta_6.5TeV_B2_fill_5313_2016-09-19_21:40:00','LHC_RP_highbeta_6.5TeV_B2_fill_5313_2016-09-19_22:04:00'])
    print scenarioscan
    print RP_scenarioscan
    dircollscan=scenarioscan; # name of the subdirectory created in ImpedanceWake2D folder
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2012/LHC-squeezer60cm/'
    
    LHC2012_60cm=optics_dir+'LHC_beta_length_B'+beam+'_sq0p6m_3m_0p6m_3m.dat';
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2016/LHC-squeeze50cm/'
    LHC2016_50cm=optics_dir+'/twiss.lhc.b'+beam+'.coll6.5tev_50cm.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2016/LHC-squeeze40cm/'
    LHC2016_40cm=optics_dir+'twiss.lhc.b'+beam+'.coll6.5tev_40cm.thick_beta_elements.dat';
    
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2015/LHC-ft'
    LHC2015_ft=optics_dir+'/twiss.lhc.b'+beam+'.ft6.5tev.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2015/LHC-injection'
    LHC2015_inj=optics_dir+'/twiss.lhc.b'+beam+'.inj450gev.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Optics/2016/LHC-HighBeta'
    LHC2016_ft_highbeta=optics_dir+'/twiss.lhc.b'+beam+'.coll6.5tev_highbeta.thick_beta_elements.dat';

    squeezescan=np.array([LHC2016_ft_highbeta for ii in scenarioscan])

    model=['Nominal LHC'  for ii in scenarioscan]; # case in LHC_param
    Escan=np.array([6500e9 for ii in scenarioscan]); # Energy
    #subscan=np.array([0])
    subscan=np.arange(0,len(Escan))
    print subscan

    param_filename_coll_root=path_here+'../Coll_settings/'; # path for collimator gaps file
    

    #DELPHI convergence criterion
    crit=5e-2
    abseps=1e-4

    # setting the scans
    planes=['x','y'];
    Qpscan=np.arange(-4,22,2);
    dampscan=np.array([0, 0.005, 0.01, 0.02]); # damper gain scan
    Nbscan=np.array([0.1e11,0.5e11,1.0e11,1.5e11])
    Mscan=np.array([1]); # scan on number of bunches
    imp_fact=1. #impedance factor

    # Longitudinal distribution
    typelong='Gaussian'


    queue='2nd'

    estimation_scale_2012=0; # to deduce intensity vs emittance curves based on 2012 instabilites
    
    Qpaver=np.array([-1,0,1]); # averages between these chromas to deduce the stability limits in the intensity vs emittance plot
    iQpaver=select_in_table(Qpaver,Qpscan);

    simulation_parameters={\
            'Simulation_time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),\
            'DELPHI_version':inspect.getmodule(DELPHI_wrapper).__file__,\
            'flagdamperimp':flagdamperimp,\
            'strnorm':strnorm,\
            'flagnorm':flagnorm,\
            'flagplot':flagplot,\
            'nevery':nevery,\
            'wake_calc':wake_calc,\
            'kmax':kmax,\
            'kmaxplot':kmaxplot,\
            'crit':crit,\
            'abseps':abseps,\
            'scenarioscan':scenarioscan,\
            'squeezescan':squeezescan,\
            'model':model,\
            'Escan':Escan,\
            'subscan':subscan,\
            'planes':planes,\
            'Qpscan':Qpscan,\
            'dampscan':dampscan,\
            'Nbscan':Nbscan,\
            'Mscan':Mscan,\
            'imp_fact':imp_fact,\
            'queue':queue,\
            'estimation_scale_2012':estimation_scale_2012,\
            'Qpaver':Qpaver,\
            'iQpaver':iQpaver
            }

    # initialize impedance model and tune shifts
    tuneshiftQp=np.zeros((len(subscan),2,len(Mscan),len(Qpscan),len(dampscan),len(Nbscan),1,1,kmaxplot),dtype=complex);
    
    tuneshiftm0Qp=np.zeros((len(subscan),2,len(Mscan),len(Qpscan),len(dampscan),len(Nbscan),1,1),dtype=complex);
    imp_mod_list=[]; # complete list of impedance scenarios
    wake_mod_list=[];# complete list of wake scenarios

    for iscenario,scenario in enumerate(RP_scenarioscan[subscan]):

        root_result=ResultDir+RP_scenarioscan[subscan[iscenario]]+'/'
        os.system("mkdir -p "+root_result);

	if machine2save=='LHC':
		machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h, M,en=LHC_param(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
        	machine=LHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
		machine.opticsDir = squeezescan[subscan[iscenario]]
		machine.model = model[subscan[iscenario]]
		fid = open(root_result+'/machine_configuration.pkl','w')
		pkl.dump(machine,fid)
		fid.close()
	
	g,a,b=longdistribution_decomp(taub,typelong=typelong);
        avbetax=R/Qx;avbetay=R/Qy; # average beta functions used
        simulation_parameters.update({'g':g,'a':a,'b':b,'typelong':typelong})
        print "scenario: ",scenario
        param_filename_coll=param_filename_coll_root+dircollscan[subscan[iscenario]]+'.txt';
        settings_filename_coll=param_filename_coll;
        comment_coll_machine=dircollscan[subscan[iscenario]];

        # compute imp. model

        if ((lxplusbatchImp.startswith('retrieve'))or(lxplusbatchImp.startswith('launch')))and(lxplusbatchDEL==None):


            imp_mod=[]; wake_mod=[];

            if machine2save=='LHC':
                imp_mod,wake_mod=LHC_imp_model_v2(E,avbetax,avbetay,param_filename_coll,settings_filename_coll,dire=path_here+"../LHC_elements/",commentcoll=comment_coll_machine,direcoll=dircollscan[subscan[iscenario]]+'/',lxplusbatch=lxplusbatchImp,beam=beam, RP_settings = param_filename_coll_root+RP_scenarioscan[subscan[iscenario]], squeeze=squeezescan[subscan[iscenario]],wake_calc=wake_calc,flagplot=flagplot,root_result=root_result,commentsave=RP_scenarioscan[subscan[iscenario]]);


        elif (lxplusbatchImp.startswith('restore')):
            print 'Loading from impedance database...'+scenario
            imp_mod=[]; wake_mod=[];
	    suffix='_Allthemachine_'+Estr+'_B'+beam+'_'+scenario+'.dat';
            freq_mod,Z_mod=readZ(root_result+"Zxdip"+suffix);
	    Z_mod*=imp_fact

	    imp_mod.append(impedance_wake(a=1,b=0,c=0,d=0,plane='x',var=freq_mod,func=Z_mod));

            freq_mod,Z_mod=readZ(root_result+"Zydip"+suffix);
	    Z_mod*=imp_fact
		

            imp_mod.append(impedance_wake(a=0,b=1,c=0,d=0,plane='y',var=freq_mod,func=Z_mod));

        imp_mod_list.append(imp_mod);
        wake_mod_list.append(wake_mod);


        if (lxplusbatchImp.startswith('retrieve'))and(lxplusbatchDEL==None):

            # write Ascii files with each component
            write_imp_wake_mod(imp_mod,"_Allthemachine_"+Estr+"_B"+str(beam)+'_'+scenario,
                listcomp=['Zlong','Zxdip','Zydip','Zxquad','Zyquad','Zxydip','Zyxdip','Zxyquad','Zyxquad','Zxcst','Zycst'],
                dire=root_result+'/')

            if (wake_calc):
            # write Ascii files with each component
                write_imp_wake_mod(wake_mod,"_Allthemachine_"+Estr+"_B"+str(beam)+'_'+scenario,
                    listcomp=['Wlong','Wxdip','Wydip','Wxquad','Wyquad','Wxydip','Wyxdip','Wxyquad','Wyxquad','Wxcst','Wycst'],
                dire=root_result+'/')
                # wake for HEADTAIL
                write_wake_HEADTAIL(wake_mod,root_result+"/wakeforhdtl_PyZbase_Allthemachine_"+Estr+"_B"+str(beam)+'_'+scenario+'.dat',beta=np.sqrt(1.-1./(gamma**2)),ncomp=6)
                # dip only
                write_wake_HEADTAIL(wake_mod,root_result+"/wakeforhdtl_PyZbase_Allthemachine_"+Estr+"_B"+str(beam)+'_'+scenario+'_dip.dat',beta=np.sqrt(1.-1./(gamma**2)),ncomp=2)

	
    if (lxplusbatchDEL!=None):
	    if (lxplusbatchDEL.startswith('launch'))or(lxplusbatchDEL.startswith('retrieve')):

		# DELPHI scans now
		for iscenario,scenario in enumerate(RP_scenarioscan[subscan]):

		    root_result=ResultDir+scenario;
		    print 'DELPHI computation for '+scenario
		    if model[subscan[iscenario]]=='Nominal LHC':

		    	machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en=LHC_param(E0,E=Escan[subscan[iscenario]]);
		        machine=LHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
			
                        if not os.path.isfile(root_result+'/last_folder_index.pkl'):
                            pkl.dump(0, open(root_result+'/last_folder_index.pkl','wb'))
                                                    
                                                        
                        last_folder_index=pkl.load(open(root_result+'/last_folder_index.pkl','rb'))
                                                                
                        last_folder_index+=1
                        pkl.dump(last_folder_index, open(root_result+'/last_folder_index.pkl','wb'))
                                                            
                        ResultsFolderDELPHI='ResultsFolderDELPHI_'+str(last_folder_index)
                        os.system("mkdir -p "+root_result+'/'+ResultsFolderDELPHI);
                        
                        if (lxplusbatchDEL.startswith('launch')):
                            with open(root_result+'/parameters_ResultsFolderDELPHI_'+str(last_folder_index)+'.pkl', 'w') as f:
			        #pkl.dump(machine, f)
                                pkl.dump(simulation_parameters,f)
			    f.close()


		    # DELPHI run
		    tuneshiftQp[iscenario,:,:,:,:,:,:,:,:],tuneshiftm0Qp[iscenario,:,:,:,:,:,:,:]=DELPHI_wrapper(imp_mod_list[iscenario],Mscan,Qpscan,dampscan,Nbscan,[omegas],[dphase],omega0,Qx,Qy,gamma,eta,a,b,taub,g,planes,nevery=nevery,particle='proton',flagnorm=0,flagdamperimp=0,d=None,freqd=None,kmax=kmax,kmaxplot=kmaxplot,crit=crit,abseps=abseps,flagm0=True,lxplusbatch=lxplusbatchDEL,comment=machine_str+scenario+'_'+float_to_str(round(E/1e9))+'GeV_Z'+str(imp_fact),queue=queue,dire=root_result+'/'+ResultsFolderDELPHI+'/',flagQpscan_outside=True);


	    # now the most unstable modes
	    if (lxplusbatchDEL.startswith('retrieve')):

		for iplane,plane in enumerate(planes):
		    for iM,M in enumerate(Mscan):
			for idamp,damp in enumerate(dampscan):
			    for Nb in Nbscan:
				strpart=['Re','Im'];
				for ir,r in enumerate(['real','imag']):
				    for iscenario,scenario in enumerate(RP_scenarioscan[subscan]):

					# output files name for data vs Qp
					Estr=float_to_str(round(Escan[subscan[iscenario]]/1e9))+'GeV';
					root_result=ResultDir+scenarioscan[subscan[iscenario]]+'/';
					fileoutdataQp=root_result+'/data_vs_Qp_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane+'_Z'+str(imp_fact);
					fileoutdataQpm0=root_result+'/data_vs_Qp_m0_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane+'_Z'+str(imp_fact);
					fileoutdata_all=root_result+'/data_vs_Qp_all_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane+'_Z'+str(imp_fact);

					ts=getattr(tuneshiftQp[iscenario,iplane,iM,:,idamp,np.where(Nbscan==Nb),0,0,0],r);
					data=np.hstack((Qpscan.reshape((-1,1)),ts.reshape((-1,1))));
					write_ncol_file(fileoutdataQp+'_'+r+'.dat',data,header="Qp\t"+strpart[ir]+"_tuneshift")

					tsm0=getattr(tuneshiftm0Qp[iscenario,iplane,iM,:,idamp,np.where(Nbscan==Nb),0,0],r);
					data=np.hstack((Qpscan.reshape((-1,1)),ts.reshape((-1,1))));
					write_ncol_file(fileoutdataQpm0+'_'+r+'.dat',data,header="Qp\t"+strpart[ir]+"_tuneshiftm0")
					
					all_unstable_modes=getattr(tuneshiftQp[iscenario,iplane,iM,:,idamp,np.where(Nbscan==Nb),0,0,:],r);
					data=np.hstack((Qpscan.reshape((-1,1)),all_unstable_modes.reshape((-1,kmaxplot))));
					write_ncol_file(fileoutdata_all+'_'+r+'.dat',data,header="Qp\t"+strpart[ir]+"_tuneshift")


					
 




if estimation_scale_2012==1:

    #####################################################
    # plots stabilizing emittance vs Nb for certain Qp
    #####################################################

    # post-LS1 scenarios
    #legbeam=['Classical 25 ns','BCMS 25 ns', 'Classical 50 ns','BCMS 50 ns'];
    #emitbeam=[3.75,1.9,2.2,1.6];
    #intbeam=[1.35,1.15,1.65,1.6];
    #Mbeam=[3564,3564,1782,1782];
    #colbeam=['ok','xk','oc','xc'];
    # from Giovanni Rumolo LBOC talk, 8/4/2014, with 0.6 mm.mrad emittance blow-up in LHC
    # except emittance standard 25ns (3.75 -> nominal)
    legbeam=['25 ns, standard','25 ns, BCMS','25ns, standard, 8b+4e','50 ns, standard (2012)'];
    emitbeam=[3.75,1.9,2.9,2.2];
    intbeam=[1.3,1.3,1.8,1.7];
    Mbeam=[3564,3564,3564,1782];
    colbeam=['ok','xk','+k','dc'];
    # HL-LHC scenarios
    #legbeam=['PIC low emit.','PIC high emit.', 'US1',"US2 low int. & low emit.","US2 high int. & high emit."];
    #emitbeam=[1.8,2.22,2.62,2.26,2.5];
    #intbeam=[1.38,1.38,1.9,1.9,2.2];
    #colbeam=['or','+m','xg','dk','vb'];

    #t1=ti.clock()

    # NEW VERSION (14/05/2014)
    #colscen=['b','r','g','m','k','c','y'];
    colscen=['b','r','g','m','k','c','y','b--','r--','g--','m--','k--','c--','y--','b','r','g','m','k','c','y','b--','r--','g--','m--','k--','c--','y--'];
    colscen2=np.array([(0,0,1),(1,0,0),(0,1,0),(1,0,1),(0,0,0),(0,1,1),(1,1,0)]);
    hatch=np.array(["/","\\","|","X","/","\\","|","X"]);

    oct2012signscan=['_neg_oct','_pos_oct'];
    legsignscan=["negative polarity (\"old\")","positive polarity (\"new\")"];
    octLS1=550.;

    # relevant 2012 instability data - based on files ../Mesures_LHC/instability_table_B2V_pos_oct_flattop.csv &
    # ../Mesures_LHC/instability_table_B2H_pos_oct_flattop.csv (Q' > 10)
    # and file ../Mesures_LHC/instability_table_B2H_neg_oct_squeeze.csv (Q'>5)
    # There are also a 3 flat top instabilities taken from an LMC talk
    # by G. Arduini in August 2012 (slides in ../Docs/lmc_145c_talk_instabilities2012_LHC_Gianluigi.pdf,
    # slide 14&15, fills 2919, 2920 & 2932 - damper gain from Timber & trim editor)
    en2012=4;M_2012=1782;
    # negative octupole polarity
    dataoct_neg2012=np.array([58.,200.,200.]);
    meanoct_neg2012=np.average(dataoct_neg2012);erroct_neg2012=np.sqrt(np.var(dataoct_neg2012));
    dataemit_neg2012=np.array([2.3,2.5,2.5]);
    meanemit_neg2012=np.average(dataemit_neg2012);erremit_neg2012=0.5;
    dataNb_neg2012=np.array([1.4,1.47,1.46])*1e11;
    dataQp_neg2012=np.array([5.9,7.,7.]);
    dataplane_neg2012=np.array(['x','x','x']);
    datadamp_neg2012=1./np.array([50.,100.,100.]);
    # positive octupole polarity
    dataoct_pos2012=np.array([209.,487.,510.,35.,35.,510.]);
    meanoct_pos2012=np.average(dataoct_pos2012);erroct_pos2012=np.sqrt(np.var(dataoct_pos2012));
    dataemit_pos2012=np.array([2.3,2.3,2.3,2.2,2.2,2.5]);
    meanemit_pos2012=np.average(dataemit_pos2012);erremit_pos2012=0.5;
    dataNb_pos2012=np.array([1.64,1.64,1.63,1.64,1.64,1.44])*1e11;
    dataQp_pos2012=np.array([15.4,18.3,10.3,13.6,17.8,9.]);
    dataplane_pos2012=np.array(['x','x','x','x','y','x']);
    datadamp_pos2012=1./np.array([100.,100.,100.,100.,100.,100.]);

    # scan parameters for DELPHI computation at 4 TeV for those experimental cases
    oct_2012=np.hstack((dataoct_neg2012,dataoct_pos2012));
    emit_2012=np.hstack((dataemit_neg2012,dataemit_pos2012));
    Nb_2012=np.hstack((dataNb_neg2012,dataNb_pos2012));
    Qp_2012=np.hstack((dataQp_neg2012,dataQp_pos2012));
    damp_2012=np.hstack((datadamp_neg2012,datadamp_pos2012));
    plane_2012=np.hstack((dataplane_neg2012,dataplane_pos2012));
    ind_neg2012=np.arange(3);ind_pos2012=np.arange(3,9); # indices in the above tables, for resp. neg. and oct. polarities

    # compute first with 2012 imp. model
    scenario2012='LHC_60cm_4TeV_2012_B1';
    LHC2012_60cm='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/LHC_IW_model/Optics/2012/LHC-squeeze60cm/LHC_beta_length_B'+beam+'_sq0p6m_3m_0p6m_3m.dat';
    param_filename_coll_2012=path_here+'../Coll_settings/'+scenario2012+'.txt';
    settings_filename_coll_2012=param_filename_coll_2012;
    comment_coll_machine=scenario2012;

    root_result2012=ResultDir2012+scenario2012+'/';
    os.system("mkdir -p "+root_result2012);

    # fixed parameters
    machine_str,E_2012,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en=LHC_param(E0,E=en2012*1e12,scenario='Nominal LHC');
    machine=LHC(E0,E=en2012*1e12,scenario='Nominal LHC');
    avbetax_2012=R/Qx;avbetay_2012=R/Qy; # average beta functions used

    # model
    imp_mod_2012=[];wake_mod_2012=[];
    if (lxplusbatchImp.startswith('restore')):
        print 'Loading from impedance database...'+scenario2012
        imp_read=[];
        imp_mod=[]; wake_mod=[];
        suffix='_Allthemachine_'+scenario2012+'.dat';
        freq_mod,Z_mod=readZ(root_result2012+"Zxdip"+suffix);
        imp_mod_2012.append(impedance_wake(a=1,b=0,c=0,d=0,plane='x',var=freq_mod,func=Z_mod));

        freq_mod,Z_mod=readZ(root_result2012+"Zydip"+suffix);
        imp_mod_2012.append(impedance_wake(a=0,b=1,c=0,d=0,plane='y',var=freq_mod,func=Z_mod));

        wake_mod_2012.append(wake_mod);
    else:
        imp_mod_2012,wake_mod_2012=LHC_imp_model_v2(E_2012,avbetax_2012,avbetay_2012,param_filename_coll_2012,settings_filename_coll_2012,dire=path_here+"../LHC_elements/",commentcoll=scenario2012,direcoll='LHC_60cm_4TeV_2012_B1/',lxplusbatch=lxplusbatchImp,beam=beam,squeeze=LHC2012_60cm,wake_calc=wake_calc,flagplot=flagplot,root_result=root_result2012,commentsave=scenario2012)

    # longitudinal distribution initialization
    g,a,b=longdistribution_decomp(taub,typelong="Gaussian");

    #t1=ti.clock()
    tuneshiftQp_2012=np.zeros((len(Qp_2012),1,1,1,1,kmaxplot),dtype=complex);
    factor_2012=np.zeros(len(Qp_2012));
    for iQp,Qp in enumerate(Qp_2012):

        # select parameters
        plane=plane_2012[iQp];iplane=int(plane=='y');print plane,iplane
        Nb=Nb_2012[iQp];damp=damp_2012[iQp];
        # select Zxdip or Zydip
        for iw in imp_mod_2012:
            if test_impedance_wake_comp(iw,1-iplane,iplane,0,0,plane): Z=deepcopy(iw.func[::nevery,:]);freq=deepcopy(iw.var[::nevery]);

        flag_trapz=0; # by default no trapz method
        if (M_2012==1): nxscan=np.array([0]);flag_trapz=1;
        else: nxscan=sort_and_delete_duplicates(np.concatenate((np.arange(0,M_2012,M_2012/20),np.arange(M_2012/2-10,M_2012/2+11),
                np.arange(M_2012-10,M_2012),np.arange(0,10))));
        print "number of coupled-bunch modes=",len(nxscan);

        tuneshiftnx=np.zeros((1,len(nxscan),1,1,1,1,kmaxplot),dtype=complex);

        tuneshiftQp_2012[iQp,:,:,:,:,:],tuneshiftnx=eigenmodesDELPHI_converged_scan_lxplus([Qp],
            nxscan,[damp],[Nb],[omegas],[dphase],M_2012,omega0,eval('Q'+plane),
            gamma,eta,a,b,taub,g,Z,freq,particle='proton',flagnorm=flagnorm,flag_trapz=flag_trapz,
            flagdamperimp=0,d=None,freqd=None,kmax=kmax,kmaxplot=kmaxplot,crit=crit,
            abseps=abseps,flagm0=False,lxplusbatch=lxplusbatchDEL,
            comment=machine_str+'_2012_v2_'+float_to_str(round(E_2012/1e9))+'GeV_'+str(M_2012)+'b_Qp'+str(Qp)+'_'+plane,
            queue=queue,dire=root_result2012+'/');

        
	# "stability factor" for each case
	factor_2012[iQp]=-oct_2012[iQp]*emit_2012[iQp]/(en2012**2*np.imag(tuneshiftQp_2012[iQp,0,0,0,0,0]))
	#factor_2012[iQp]=-oct_2012[iQp]*emit_2012[iQp]/(en2012**2*(np.imag(tsRe+1j*tsIm)))

        print "all factors 2012:",factor_2012;
        print "all growth rates 2012:",-omega0*np.imag(tuneshiftQp_2012[:,0,0,0,0,0]);
        factor_neg_oct_2012_mean=np.average(factor_2012[ind_neg2012]);
        factor_pos_oct_2012_mean=np.average(factor_2012[ind_pos2012]);
        factor_neg_oct_2012_sig=np.sqrt(np.var(factor_2012[ind_neg2012]));
        factor_pos_oct_2012_sig=np.sqrt(np.var(factor_2012[ind_pos2012]));
        print "averages & sigmas:",factor_neg_oct_2012_mean,factor_neg_oct_2012_sig,factor_pos_oct_2012_mean,factor_pos_oct_2012_sig;

    # end of computations with 2012 model

    if (lxplusbatchImp==None)or(lxplusbatchImp.startswith('restore')):

        if (lxplusbatchDEL==None)or(lxplusbatchDEL.startswith('retrieve')):

            for isign,octsign in enumerate(oct2012signscan):

        # assumes oct*emit/en^2 =  fact *imag(-tuneshift(int));
                fact=eval('factor'+octsign+'_2012_mean');
                sig_fact=eval('factor'+octsign+'_2012_sig');

                for iM,M in enumerate(Mscan):

                    for idamp,damp in enumerate(dampscan):


                        for iscenario,scenario in enumerate(scenarioscan[subscan]):
                            Estr=float_to_str(round(Escan[subscan[iscenario]]/1e9))+'GeV';
                            root_result=ResultDir+scenarioscan[subscan[iscenario]]+'/';
                            fileoutdataemit=root_result+'/data_int_vs_emit_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Qp'+float_to_str(Qpaver[0])+'_'+float_to_str(Qpaver[-1])+octsign+'_converged'+strnorm[flagnorm];
                            fileoutplotemit=root_result+'/plot_int_vs_emit_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Qp'+float_to_str(Qpaver[0])+'_'+float_to_str(Qpaver[-1])+octsign+'_converged'+strnorm[flagnorm];


                            imtu=np.zeros(len(Nbscan));
                            for iNb,Nb in enumerate(Nbscan):
                                tsIm=getattr(tuneshiftQp[iscenario,:,iM,iQpaver,idamp,iNb,0,0,0],'imag');
				tsRe=getattr(tuneshiftQp[iscenario,:,iM,iQpaver,idamp,iNb,0,0,0],'real');

				ts=np.imag(tsRe+1j*tsIm);

                                if len(np.isnan(ts))==0: imtu[iNb]=np.min(ts);
                                else: imtu[iNb]=np.min(ts[~np.isnan(ts)]);
                                #imtu[iNb]=np.max(np.abs(tuneshiftQp[iscenario,:,iM,iQpaver,idamp,iNb,0,0,0]));

                            emit=fact*(Escan[subscan[iscenario]]/1.e12)**2/octLS1 * np.abs(imtu);
                            sig_emit=sig_fact*(Escan[subscan[iscenario]]/1.e12)**2/octLS1 * np.abs(imtu)

                            data=np.hstack((emit.reshape((-1,1)),Nbscan.reshape((-1,1)),sig_emit.reshape((-1,1))));
                            write_ncol_file(fileoutdataemit+'.dat',data,header="emit\tNb\tsig_emit")

