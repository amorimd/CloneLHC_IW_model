#!/usr/bin/python

import sys
import commands
# import local libraries if needed
#pymod=commands.getoutput("echo $PYMOD");
#if pymod.startswith('local'):
#    py_numpy=commands.getoutput("echo $PY_NUMPY");sys.path.insert(1,py_numpy);
#    py_matpl=commands.getoutput("echo $PY_MATPL");sys.path.insert(1,py_matpl);

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
from HLLHC_param import *
from LHC_imp import *
from HLLHC_imp import *
from LHC_coll_imp import *


if __name__ == "__main__":

    # beam parameters
    e,m0,c,E0=proton_param();

    # machine parameters
    machine2save='HLLHC';
    beam='1';

    # directory (inside DELPHI_results/[machine]) where to put the results
    RunDir='IP7-coatings_DQW-IP15/';
    ResultDir=path_here+'../../../DELPHI_results/'+machine2save+'/'+RunDir;
    ResultDir2012=path_here+'../../../DELPHI_results/'+machine2save+'/'+RunDir;
    os.system("mkdir -p "+ResultDir);

    # flags for plotting and DELPHI
    flagdamperimp=0; # 1 to use frequency dependent damper gain (provided in Zd,fd)
    strnorm=[''];
    flagnorm=0; # 1 if damper matrix normalized at current chromaticity (instead of at zero chroma)
    flagplot=True; # to plot impedances
    nevery=1; # downsampling of the impedance (take less points than in the full model)
    wake_calc=False; # True -> compute wake as well (otherwise only imp.)


    kmax=1; # number of converged eigenvalues (kmax most unstable ones are converged)
    kmaxplot=20; # number of kept and plotted eigenvalues (in TMCI plot)
    col=['b','r','g','m','k','c','y','b--','r--','g--','m--','k--','c--','y--']; # colors
    linetype=['-','--',':'];

    # scan definition
    strsubscan='_LHC_v2_all_postLS1_options';margin_factor=1;
    scenarioscan=np.array([
	    'HL-LHC_15cm_7TeV_baseline_TCT5_B1',
	    'HL-LHC_15cm_7TeV_MoC_IP7_TCT5_B1',
	    'HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1',
	    'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1',
	    'HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1',
	    'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_IR3_open_B1',
	    'HL-LHC_15cm_7TeV_5umMo+MoC_IP3+IP7_TCT5_B1',]);

    print scenarioscan
    dircollscan=scenarioscan; # name of the subdirectory in ImpedanceWake2D
    
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2012/LHC-squeeze60cm/'
    LHC2012_60cm=optics_dir+'LHC_beta_length_B'+beam+'_sq0p6m_3m_0p6m_3m.dat';
    
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2016/LHC-squeeze50cm/'
    LHC2016_50cm=optics_dir+'/twiss.lhc.b'+beam+'.coll6.5tev_50cm.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2016/LHC-squeeze40cm/'
    LHC2016_40cm=optics_dir+'twiss.lhc.b'+beam+'.coll6.5tev_40cm.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/LHC-squeeze80cm/'
    LHC2015_80cm=optics_dir+'twiss.lhc.b'+beam+'.coll6.5tev_80cm.thick_beta_elements.dat';
    
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/LHC-injection'
    LHC2015_inj=optics_dir+'/twiss.lhc.b'+beam+'.inj450gev.thick_beta_elements.dat';

    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/LHC-ft'
    LHC2015_ft=optics_dir+'/twiss.lhc.b'+beam+'.ft6.5tev.thick_beta_elements.dat';
	
    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/HLLHCV1.1'
    HLLHC_15cm=optics_dir+'/twiss.hllhc.b'+beam+'.coll7tev_round.thick_beta_elements.dat';

    optics_dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/HLLHC-squeeze60cm/'
    HLLHC_60cm=optics_dir+'twiss.hllhc.b'+beam+'.coll7tev_squeeze60cm.thick_beta_elements.dat';
    
    squeezescan=np.array([HLLHC_15cm for ii in scenarioscan])

    model=['HLLHC 25ns'  for ii in scenarioscan];
    Escan=np.array([7000e9 for ii in scenarioscan]); # Energy
    #subscan=np.array([0])
    subscan=np.arange(0,len(Escan))
    print subscan

    param_filename_coll_root=path_here+'Coll_settings/'; #name collgap file
    planes=['x','y'];
    Qpscan=np.arange(14,17,1);
    dampscan=np.array([0.02]); # damper gain scan
    Nbscan=np.array([1e10, 1.1e11, 2.1e11, 3.1e11, 4.1e11])
    Mscan=np.array([1]); # scan on number of bunches


    # stabilizing emittance from 2012
    estimation_scale_2012=1; # for intensity vs emittance data
    
    Qpaver=np.array([14,15,16]); # for stability limits
    iQpaver=select_in_table(Qpaver,Qpscan);

    # initialize impedance model and tune shifts
    tuneshiftQp=np.zeros((len(subscan),2,len(Mscan),len(Qpscan),len(dampscan),len(Nbscan),1,1,kmaxplot),dtype=complex);
    
    tuneshiftm0Qp=np.zeros((len(subscan),2,len(Mscan),len(Qpscan),len(dampscan),len(Nbscan),1,1),dtype=complex);
    imp_mod_list=[]; # complete list of impedance scenarios
    wake_mod_list=[];# complete list of wake scenarios

    for iscenario,scenario in enumerate(scenarioscan[subscan]):

        root_result=ResultDir+scenarioscan[subscan[iscenario]]+'/'
        os.system("mkdir -p "+root_result);

	if machine2save=='LHC':
		machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h, M,en=LHC_param(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
        	machine=LHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
	elif machine2save=='HLLHC':
		machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en=HLLHC_param(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]]);
	        machine=HLLHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
	g,a,b=longdistribution_decomp(taub,typelong="Gaussian");
        avbetax=R/Qx;avbetay=R/Qy; # average beta functions used
        print "scenario: ",scenario
        param_filename_coll=param_filename_coll_root+scenario+'.txt';
        settings_filename_coll=param_filename_coll;
        comment_coll_machine=scenario;

        # compute imp. model

        if ((lxplusbatchImp.startswith('retrieve'))or(lxplusbatchImp.startswith('launch')))and(lxplusbatchDEL==None):


            imp_mod=[]; wake_mod=[];
	    if machine2save=='HLLHC':
                imp_mod,wake_mod=HLLHC_imp_model_v2(machine, E,avbetax,avbetay,param_filename_coll,settings_filename_coll,dire=path_here+"LHC_elements/",commentcoll=comment_coll_machine,direcoll=dircollscan[subscan[iscenario]]+'/',lxplusbatch=lxplusbatchImp,beam=beam,squeeze=squeezescan[subscan[iscenario]],wake_calc=wake_calc,BPM=False,optionCrab=['DQW_20151001','DQW_20151001'], optics_dir=optics_dir, Ncav=4 ,optionBBC=0,margin_factor=1,fcutoffBB=50e9,flagplot=flagplot,root_result=root_result,commentsave=scenario);

            elif machine2save=='LHC':
                imp_mod,wake_mod=LHC_imp_model_v2(E,avbetax,avbetay,param_filename_coll,settings_filename_coll,dire=path_here+"LHC_elements/",commentcoll=comment_coll_machine,direcoll=dircollscan[subscan[iscenario]]+'/',lxplusbatch=lxplusbatchImp,beam=beam,squeeze=squeezescan[subscan[iscenario]],wake_calc=wake_calc,flagplot=flagplot,root_result=root_result,commentsave=scenario);


        elif (lxplusbatchImp.startswith('restore')):
            print 'Loading from impedance database...'+scenario
            imp_mod=[]; wake_mod=[];
	    suffix='_Allthemachine_'+Estr+'_B'+beam+'_'+scenario+'.dat';
            freq_mod,Z_mod=readZ(root_result+"Zxdip"+suffix);
            if 'fact2' in scenario:
		    Z_mod=Z_mod*2;
		    print scenario+': Impedance x-plane multiplied by 2.'

	    imp_mod.append(impedance_wake(a=1,b=0,c=0,d=0,plane='x',var=freq_mod,func=Z_mod));

            freq_mod,Z_mod=readZ(root_result+"Zydip"+suffix);
		
	    if 'fact2' in scenario:
		    Z_mod=Z_mod*2;
		    print scenario+': Impedance y-plane multiplied by 2.'

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
		for iscenario,scenario in enumerate(scenarioscan[subscan]):

		    root_result=ResultDir+scenario;
		    print 'DELPHI computation for '+scenario
		    if model[subscan[iscenario]]=='LHC':
		    	machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en=LHC_param(E0,E=Escan[subscan[iscenario]]);
		        machine=LHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])
		    elif model[subscan[iscenario]]=='HLLHC':
                        machine_str,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en=HLLHC_param(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]]);
                        machine=HLLHC(E0,E=Escan[subscan[iscenario]],scenario=model[subscan[iscenario]])

		    # DELPHI run
		    tuneshiftQp[iscenario,:,:,:,:,:,:,:,:],tuneshiftm0Qp[iscenario,:,:,:,:,:,:,:]=DELPHI_wrapper(imp_mod_list[iscenario],Mscan,Qpscan,dampscan,Nbscan,[omegas],[dphase],omega0,Qx,Qy,gamma,eta,a,b,taub,g,planes,nevery=nevery,particle='proton',flagnorm=0,flagdamperimp=0,d=None,freqd=None,kmax=kmax,kmaxplot=kmaxplot,crit=5.e-2,abseps=1e-4,flagm0=True,lxplusbatch=lxplusbatchDEL,comment=machine_str+scenario+'_'+float_to_str(round(E/1e9))+'GeV',queue='1nw',dire=root_result+'/',flagQpscan_outside=True);


	    # now the most unstable modes
	    if (lxplusbatchDEL.startswith('retrieve')):

		for iplane,plane in enumerate(planes):
		    for iM,M in enumerate(Mscan):
			for idamp,damp in enumerate(dampscan):
			    for Nb in Nbscan:
				strpart=['Re','Im'];
				for ir,r in enumerate(['real','imag']):
				    for iscenario,scenario in enumerate(scenarioscan[subscan]):

					# output files name for data vs Qp
					Estr=float_to_str(round(Escan[subscan[iscenario]]/1e9))+'GeV';
					root_result=ResultDir+scenarioscan[subscan[iscenario]]+'/';
					fileoutdataQp=root_result+'/data_vs_Qp_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane;
					fileoutdataQpm0=root_result+'/data_vs_Qp_m0_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane;
					fileoutdata_all=root_result+'/data_vs_Qp_all_'+machine_str+'_'+Estr+scenario+'_'+str(M)+'b_d'+float_to_str(damp)+'_Nb'+float_to_str(Nb/1.e11)+'e11_converged'+strnorm[flagnorm]+'_'+plane;

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
    LHC2012_60cm='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2012/LHC-squeeze60cm/LHC_beta_length_B'+beam+'_sq0p6m_3m_0p6m_3m.dat';
    param_filename_coll_2012=path_here+'Coll_settings/'+scenario2012+'.txt';
    settings_filename_coll_2012=param_filename_coll_2012;
    comment_coll_machine=scenario2012;

    root_result2012=ResultDir2012+scenario2012+'/';

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
        imp_mod_2012,wake_mod_2012=LHC_imp_model_v2(E_2012,avbetax_2012,avbetay_2012,param_filename_coll_2012,settings_filename_coll_2012,dire=path_here+"LHC_elements/",commentcoll=scenario2012,direcoll='LHC_60cm_4TeV_2012_B1/',lxplusbatch=lxplusbatchImp,beam=beam,squeeze=LHC2012_60cm,wake_calc=wake_calc,flagplot=flagplot,root_result=root_result2012,commentsave=scenario2012)

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
            flagdamperimp=0,d=None,freqd=None,kmax=kmax,kmaxplot=kmaxplot,crit=5.e-2,
            abseps=1.e-4,flagm0=False,lxplusbatch=lxplusbatchDEL,
            comment=machine_str+'_2012_v2_'+float_to_str(round(E_2012/1e9))+'GeV_'+str(M_2012)+'b_Qp'+str(Qp)+'_'+plane,
            queue='2nd',dire=root_result2012+'/');

        
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

