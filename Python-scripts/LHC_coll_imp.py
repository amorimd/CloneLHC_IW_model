#!/usr/bin/python

import sys
import commands
# import local libraries if needed
pymod=commands.getoutput("echo $PYMOD");
if pymod.startswith('local'):
    py_numpy=commands.getoutput("echo $PY_NUMPY");sys.path.insert(1,py_numpy);
    py_matpl=commands.getoutput("echo $PY_MATPL");sys.path.insert(1,py_matpl);

from string import *
import numpy as np
import pickle as pick
#import pylab
import os,re
path_here=os.getcwd()+"/";
#from plot_lib import plot,init_figure,end_figure
from io_lib import *
from string_lib import *
from particle_param import *
from Impedance import *

def LHC_many_RP_iw_model_with_geom_v2(E,avbetax,avbetay,param_filename,wake_calc=False,ftypescan=2,nflog=100,zpar=z_param(),namesref=None,BPM=False,flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire='',assymetry_factor_TCL6=1.,root_result=path_here+'../../../DELPHI_results/LHC'):

    ''' creates an impedance or wake model for all collimators.
    E is the energy in eV,
    avbetax and avbetay the average beta functions used for the weighting,
    param_filename is the file with all parameters and half-gaps and betas,
    wake_calc selects the wake computation if True.
    nflog is the number of frequencies per decade,
    ftypescan the type of frequency scan (0,1 or 2: logarithmic only,
    linear only or logarithmic with refinement around high-frequency resonance(s) ).
    zpar gives the distance scan for the wake.
    namesref are the coll. names (from param_filename) to select (if None take all),
    BPM: geometry contains a BPM cavity if BPM is True, otherwise old LHC coll. geometry
    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov
    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators
    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)
    assymetry_factor_TCL6: assymetry factor between the distance beam-jaw
    in the case of the TCL6 (1 means that jaws are symmetric).
    In this version, the parameter file can contain several material rows
    (with the associated thickness columns) and the geometric impedance is
    taken into account'''

    e,m0,c,E0=proton_param();
    gamma=E*e/E0;

    header,cols=read_multiform_file(param_filename+'.txt','\t',1)
    #print header
    ind,namesref=select_col(header,cols,'Name');
    if ind==-1: sys.exit("No Names");
    ind,material=select_col(header,cols,'Material');
    if ind==-1: sys.exit("No Materials");
    ind,thick=select_col(header,cols,'Thickness[m]');
    if ind==-1: sys.exit("No Thickness");
    ind,angle=select_col(header,cols,'Angle[rad]');
    if ind==-1: sys.exit("No Angles");
    ind,length=select_col(header,cols,'Length[m]');
    if ind==-1: sys.exit("No Length");
    ind,halfgap=select_col(header,cols,'Halfgap[m]');
    if ind==-1: sys.exit("No Gaps");
    ind,betax=select_col(header,cols,'Betax[m]');
    if ind==-1: sys.exit("No Betax");
    ind,betay=select_col(header,cols,'Betay[m]');
    if ind==-1: sys.exit("No Betay");
    ind,ageing_factor=select_col(header,cols,'Ageing_factor');
    if ind==-1: ageing_factor=[]; print "No ageing considered."# setting default no ageing on collimator materials.



    # read files

    name_uniq=[];
    [name_uniq.append(n) for n in namesref if n not in name_uniq];
    # main loop to construct model
    imp_mod_RW=[];wake_mod_RW=[];imp_mod_geom=[];wake_mod_geom=[];
    for iname,name in enumerate(name_uniq):
        fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000
        ind=[];
        materials=[];
        thicks=[];
        betx=[];
        bety=[];
        age=[];

        [ind.append(i) for i,n in enumerate(namesref) if n==name];
        materials=[material[i] for i in ind];
        thicks=[thick[i] for i in ind];
        betx=[betax[i] for i in ind];
        bety=[betay[i] for i in ind];
        if ageing_factor: age=[ageing_factor[i] for i in ind];

        # reorder materials and thicknesses
        assymetry_factor=0
        if (assymetry_factor != 1.): comment_assym='assym'+float_to_str(assymetry_factor);
        
        imp_RW,wake_RW,imp_geom,wake_geom=LHC_single_RP_iw_model_with_geom(name,materials,float(halfgap[ind[0]]),float(angle[ind[0]]),gamma,float(length[ind[0]]),thickness=thicks,ageing_factor=age,wake_calc=wake_calc,fpar=freq_param(ftypescan=ftypescan,nflog=nflog,fminrefine=fminrefine,fmaxrefine=fmaxrefine,nrefine=nrefine),zpar=zpar,BPM=BPM,flag_wakefiles=flag_wakefiles,fcutoffBB=fcutoffBB,lxplusbatch=lxplusbatch,comment='_'+materials[0]+'_'+comment_assym+'_'+comment,dire=dire,assymetry_factor=assymetry_factor,param_filename=param_filename);
	
	imp_RW_weighted=[]	
	wake_RW_weighted=[];
	imp_geom_weighted=[]
	wake_geom_weighted=[];

	add_impedance_wake(imp_RW_weighted,imp_RW,float(betx[0])/avbetax,float(bety[0])/avbetay);
       	add_impedance_wake(imp_geom_weighted,imp_geom,float(betx[0])/avbetax,float(bety[0])/avbetay);
	add_impedance_wake(wake_RW_weighted,wake_RW,float(betx[0])/avbetax,float(bety[0])/avbetay);
       	add_impedance_wake(wake_geom_weighted,wake_geom,float(betx[0])/avbetax,float(bety[0])/avbetay);

	
	write_imp_wake_mod(imp_RW_weighted,"_"+name+'_RW',listcomp=['Zlong','Zxdip','Zydip','Zxquad','Zyquad','Wlong','Wxdip','Wydip','Wxquad','Wyquad'],dire=root_result+'/');

	write_imp_wake_mod(imp_geom_weighted,"_"+name+'_Geom',listcomp=['Zlong','Zxdip','Zydip','Zxquad','Zyquad','Wlong','Wxdip','Wydip','Wxquad','Wyquad'],dire=root_result+'/');
	
	add_impedance_wake(imp_mod_RW,imp_RW_weighted,1,1);
        add_impedance_wake(wake_mod_RW,wake_RW_weighted,1,1);
        add_impedance_wake(imp_mod_geom,imp_geom_weighted,1,1);
        add_impedance_wake(wake_mod_geom,wake_geom_weighted,1,1);

    return imp_mod_RW,wake_mod_RW,imp_mod_geom,wake_mod_geom;


def LHC_single_RP_iw_model_with_geom(name,materials,halfgap,angle,gamma,length,
        thickness=[],ageing_factor=[],wake_calc=False,fpar=freq_param(),zpar=z_param(),BPM=False,
        flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire='',queue=None,
        assymetry_factor=1.,param_filename=''):

    ''' construct impedance/wake model (flat chamber) for an LHC collimator
    with a skew angle (as defined in N. Mounet PhD, p. 56)
    name is the name of the collimator, materials its materials
    (list of names or layer objects), angle in rad, halfgap in m,
    layers thickness in m except the last (and main) jaw material (e.g. CFC, hBN, etc.)
    which is hard-coded.
    geometry contains a BPM cavity if BPM is True, otherwise old LHC coll. geometry
    wake_calc: flag for wake calculation
    This includes geometric impedance from Stupakov's analytical formula
    (flat tapers), thanks to INFN computations (M. Zobov, O. Frasciello)

    last layer is always stainless steel 304L

    fpar and zpar select the frequencies and distances (for the wake) scans
    (objects of the classes freq_param and z_param).

    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov

    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators

    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    comment is added to the name for IW2D output files
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)
    if queue is not None, it is the lxbatch queue where to launch the calculation.
    if assymetry factor is different from 1, uppper & lower jaws are not at the same
    distance from the beam, and assymetry_factor represents the factor applied to
    the distance to the upper jaw to get that of the lower jaw (can be zero - no lower
    jaw, as in TCDQ)
    param_filename: collimator settings name to distinguish 2012 from postLS1 cases.
    '''


    materials=create_list(materials,n=1);

    queue= '2nd';
    # material names convenions
    freqlin=1.e11;
    print materials, queue, name, thickness;
    Bfield=0; # no magnetoresistance effects in collimators
    # construct layers list
    layers=construct_layers(materials,thickness=thickness,Bfield=Bfield,Age=ageing_factor);
    # add infinite stainless-steel in the end
    layers.append(ss304L_layer());

    if assymetry_factor!=1:
        # assymetric jaws
        b=[halfgap,halfgap*assymetry_factor];
        print 'asymmetric jaw'
        if assymetry_factor>0:
            # lower layers assumed identical to the upper ones
            layerslow=deepcopy(layers)
            layers.extend(layerslow);


    # construct input file for resistive-wall computation
    iw_input=impedance_wake_input(gamma=gamma,length=length,b=b,
        layers=layers,fpar=fpar,zpar=zpar,freqlinbisect=freqlin,geometry='flat',comment='_'+name+comment);

    imp_mod,wake_mod=imp_model_from_IW2D(iw_input,wake_calc=wake_calc,flagrm=True,lxplusbatch=lxplusbatch,queue=queue,dire=dire);

    imp_mod_RW=rotate_imp_wake(imp_mod,np.pi/2.-angle);
    wake_mod_RW=rotate_imp_wake(wake_mod,np.pi/2.-angle);

    # compute geometric impedance
    R= 150e3/0.1e-3*halfgap # linear w.r.t. value caluculated at 0.1mm [BS from CST]
    fr = 50e9
    Q = 1.

    if wake_calc:
        imp_modg,wake_modg=imp_model_resonator(R,fr,Q,wake_calc=wake_calc,fpar=fpar,
                zpar=zpar,listcomp=['Zlong', 'Zxdip', 'Zydip', 'Zxquad', 'Zyquad']);
        
    else:
        imp_modg,wake_modg=imp_model_resonator(R,fr,Q,wake_calc=wake_calc,fpar=fpar,
                zpar=zpar,listcomp=['Zlong', 'Zxdip', 'Zydip', 'Zxquad', 'Zyquad']);

    imp_mod_geom=rotate_imp_wake(imp_modg,np.pi/2.-angle);
    wake_mod_geom=rotate_imp_wake(wake_modg,np.pi/2.-angle);

    return imp_mod_RW,wake_mod_RW,imp_mod_geom,wake_mod_geom;



def LHC_singlecoll_iw_model(name,materials,halfgap,angle,gamma,length,thickness=[],rhoDC=[],
        wake_calc=False,coatingmat=None,coatingthickness=0,assymetry_factor=1.,fpar=freq_param(),zpar=z_param(),
        lxplusbatch=None,comment='',dire='',queue=None):

    ''' construct impedance/wake model (flat chamber) for an LHC collimator
    with a skew angle (as defined in N. Mounet PhD, p. 56)
    name is the name of the collimator, material its main material,
    angle in rad, halfgap in m
    wake_calc: flag for wake calculation
    if coatingmat is not None, first layer is a coating defined
    by this and coatingthickness
    last layer is vacuum (NB 25-08-2015)

    fpar and zpar select the frequencies and distances (for the wake) scans
    (objects of the classes freq_param and z_param).

    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    comment is added to the name for IW2D output files
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)
    if queue is not None, it is the lxbatch queue where to launch the calculation.'''
    materials=create_list(materials,n=1);

    if (queue==None):
        # find on which queue to launch calculation (case when lxplusbatch=='launch')
        queues=['2nd','2nd','2nd','2nd','2nd','2nd','1nw'];
        if wake_calc:
            if materials[0].startswith('hBN'): iq=5;
            elif (materials[0]=="C")or(materials[0]=="CFC"): iq=4;
            else: iq=3;
            if (gamma>=3000): iq+=1; # flat top settings -> convergence is slower
        else:
            nfreq=(np.mod(fpar.ftypescan,2)==0)*((np.log10(fpar.fmax)-np.log10(fpar.fmin))*fpar.nflog+1) + (fpar.ftypescan==1)*round((fpar.fmax-fpar.fmin)/fpar.fsamplin)+(fpar.ftypescan==2)*fpar.nrefine;
            iq=max(int(np.ceil(np.log10(nfreq/500.))),0); # =0 up to 500 frequencies; 1 up to 5000; 2 up to 50000; etc.
            iq+=1;
            if materials[0].startswith('Ti_in_TDI'): iq+=2;
        queue=queues[iq];

    # material names convenions
    freqlin=1.e11;b=[halfgap];
    for imat,mat in enumerate(materials):
        if (mat!=None)and(not(isinstance(mat,layer))):
            if (mat.startswith('CU'))or(mat.startswith('Cu')): materials[imat]='Cu300K';
            elif (mat=='C'): materials[imat]='graphite';
            elif (mat.startswith('HBN')): materials[imat]='hBN';freqlin=1.e9;
            elif (mat.startswith('MO')): materials[imat]='Mo';


    print materials, queue, name, thickness;
    Bfield=0; # no magnetoresistance effects in collimators
    # construct layers list
    layers=construct_layers(materials,thickness=thickness,Bfield=Bfield,Age=1,rhoDC=rhoDC);
    # add infinite vacuum in the end
    layers.append(vacuum_layer());

    if assymetry_factor!=1:
        # assymetric jaws
        b=[halfgap,halfgap*assymetry_factor];
        if assymetry_factor>0:
            # lower layers assumed identical to the upper ones
            layerslow=deepcopy(layers)
            layers.extend(layerslow);

    iw_input=impedance_wake_input(gamma=gamma,length=length,b=b,
        layers=layers,fpar=fpar,zpar=zpar,freqlinbisect=freqlin,geometry='flat',comment='_'+name+comment);
    print dire
    imp_mod,wake_mod=imp_model_from_IW2D(iw_input,wake_calc=wake_calc,flagrm=True,lxplusbatch=lxplusbatch,queue=queue,dire=dire);

    imp_mod_new=rotate_imp_wake(imp_mod,np.pi/2.-angle);
    wake_mod_new=rotate_imp_wake(wake_mod,np.pi/2.-angle);

    return imp_mod_new,wake_mod_new;


def LHC_TDI_iw_model(name,material,halfgap,angle,gamma,wake_calc=False,
        TDIcoating=['Ti_in_TDI',None,None],TDIcoatingthickness=[5e-6,0,0],
        ftypescan=2,nflog=100,lxplusbatch=None,comment='',dire=''):

    ''' impedance/wake model for the LHC TDI (particular case: 3 blocks)
    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)'''

    # TDI main materials and lengths
    TDImat=['hBN','Al','Cu300K'];TDIlength=[2.8,0.6,0.7];

    imp=[];wake=[];
    # three different blocks
    for i in range(3):

        if (i==0): fminrefine=8.e8;fmaxrefine=2.e12;nrefine=40000;
        else: fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000;

        imp1,wake1=LHC_singlecoll_iw_model(name+'_'+str(i+1),TDImat[i],halfgap,angle,gamma,TDIlength[i],
                wake_calc=wake_calc,coatingmat=TDIcoating[i],coatingthickness=TDIcoatingthickness[i],
                fpar=freq_param(ftypescan=ftypescan,nflog=nflog,fminrefine=fminrefine,
                fmaxrefine=fmaxrefine,nrefine=nrefine),lxplusbatch=lxplusbatch,
                comment=comment+'_'+TDImat[i]+'_'+float_to_str(round(halfgap*1e5)/1e2)+'mm',dire=dire);
        add_impedance_wake(imp,imp1,1,1);
        add_impedance_wake(wake,wake1,1,1);
    return imp,wake;


def select_LHC_coll_IR(names,pattern='',IRlist=range(1,9)):
    ''' select from a list of LHC device names those that begin with "pattern" and that are in
    an IR in the list "IRlist" (from 1 to 8)
    By default, pattern and IRlist are such that all names are
    selected.'''

    namesnew=[];
    for name in names:
        IR=int(name.split('.')[1][-1]); # IR in which is this device
        if (name.startswith(pattern))and(IR in IRlist): namesnew.append(name);

    return namesnew;


def LHC_manycoll_iw_model(E,avbetax,avbetay,param_filename,settings_filename,
        beta_filename,wake_calc=False,ftypescan=2,nflog=100,namesref=None,
        coatingmat=None,coatingthickness=0,lxplusbatch=None,comment='',dire=''):

    ''' creates an impedance or wake model for all collimators.
    E is the energy in eV, avbetax and avbetay the average beta functions
    used for the weighting, param_filename is the file with all parameters
    except half-gaps and betas, settings_filename is the file with half-gaps (in m),
    beta_filename the file with beta functions (in m).
    wake_calc selects the wake computation if True, nflog are the number of frequencies
    per decade, and ftypescan the type of frequency scan (0,1 or 2: logarithmic only,
    linear only or logarithmic with refinement around high-frequency resonance(s) ).
    namesref are the coll. names (from param_filename) to select (if None take all),
    coatingmat and coatingthickness is the info about an added coating.
    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)'''

    e,m0,c,E0=proton_param();
    gamma=E*e/E0;

    # read files
    namesref,material,angle,length,halfgap,betax,betay=read_coll_files(param_filename,settings_filename,beta_filename,namesref=namesref);
    for i,name in enumerate(namesref): print name,material[i],angle[i],length[i],halfgap[i],betax[i],betay[i]

    # main loop to construct model
    imp_mod=[];wake_mod=[];
    for iname,name in enumerate(namesref):

        fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000;

        if name.startswith('TDI'):
            # special case of the TDI
            imp,wake=LHC_TDI_iw_model(name,material[iname],halfgap[iname],angle[iname],gamma,
                    wake_calc=wake_calc,ftypescan=ftypescan,nflog=nflog,lxplusbatch=lxplusbatch,
                    comment=comment,dire=dire);

        else:
            imp,wake=LHC_singlecoll_iw_model(name,material[iname],
                halfgap[iname],angle[iname],gamma,length[iname],wake_calc=wake_calc,
                coatingmat=coatingmat,coatingthickness=coatingthickness,fpar=freq_param(ftypescan=ftypescan,
                nflog=nflog,fminrefine=fminrefine,fmaxrefine=fmaxrefine,nrefine=nrefine),lxplusbatch=lxplusbatch,
                comment=comment+'_'+material[iname]+'_'+float_to_str(round(halfgap[iname]*1e5)/1e2)+'mm',dire=dire);

        add_impedance_wake(imp_mod,imp,betax[iname]/avbetax,betay[iname]/avbetay);
        add_impedance_wake(wake_mod,wake,betax[iname]/avbetax,betay[iname]/avbetay);

    return imp_mod,wake_mod;


def read_coll_files(param_filename,settings_filename,beta_filename,namesref=None):
    ''' read collimator files and output parameters.'''

    # file with materials, angles and lengths
    if (namesref==None): namesref=read_ncol_file_identify_header(param_filename,'[nN]ame');
    names=read_ncol_file_identify_header(param_filename,'[nN]ame');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    angle=read_ncol_file_identify_header(param_filename,'[aA]ngle');
    length=read_ncol_file_identify_header(param_filename,'[lL]ength');
    material=read_ncol_file_identify_header(param_filename,'[mM]aterial');
    material=[material[i] for i in ind];angle=angle[ind];length=length[ind];

    # file with settings
    names=read_ncol_file_identify_header(settings_filename,'[nN]ame');
    halfgap=read_ncol_file_identify_header(settings_filename,'[hH]alfgap');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    halfgap=halfgap[ind];



    # file with beta functions
    names=read_ncol_file_identify_header(beta_filename,'[nN]ame');
    betax=read_ncol_file_identify_header(beta_filename,'[bB]etax');
    betay=read_ncol_file_identify_header(beta_filename,'[bB]etay');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    betax=betax[ind];betay=betay[ind];

    return namesref,material,angle,length,halfgap,betax,betay;


def read_coll_files_several_mat(param_filename,settings_filename,beta_filename,namesref=None):
    ''' read collimator files and output parameters. Version with
    possibility to have several material columns (with the associated
    thickness columns)'''

    # file with materials, angles and lengths
    if (namesref==None): namesref=read_ncol_file_identify_header(param_filename,'[nN]ame');
    names=read_ncol_file_identify_header(param_filename,'[nN]ame');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    angle=read_ncol_file_identify_header(param_filename,'[aA]ngle');
    length=read_ncol_file_identify_header(param_filename,'[lL]ength');
    angle=angle[ind];length=length[ind];

    # read materials and thicknesses
    material,thick,nmat=read_materials(param_filename,ind);
    #print material,thick,nmat

    # file with settings
    names=read_ncol_file_identify_header(settings_filename,'[nN]ame');
    halfgap=read_ncol_file_identify_header(settings_filename,'[hH]alfgap');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    halfgap=halfgap[ind];

    # file with beta functions
    names=read_ncol_file_identify_header(beta_filename,'[nN]ame');
    betax=read_ncol_file_identify_header(beta_filename,'[bB]etax');
    betay=read_ncol_file_identify_header(beta_filename,'[bB]etay');
    # reorder such that the coll. names match with namesref
    ind=find_ind_names(namesref,names);
    betax=betax[ind];betay=betay[ind];

    return namesref,material,thick,angle,length,halfgap,betax,betay;


def LHC_singlecoll_iw_model_with_geom(name,materials,halfgap,angle,gamma,length,
        thickness=[],ageing_factor=[],wake_calc=False,fpar=freq_param(),zpar=z_param(),BPM=False,
        flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire='',queue=None,
        assymetry_factor=1.,param_filename=''):

    ''' construct impedance/wake model (flat chamber) for an LHC collimator
    with a skew angle (as defined in N. Mounet PhD, p. 56)
    name is the name of the collimator, materials its materials
    (list of names or layer objects), angle in rad, halfgap in m,
    layers thickness in m except the last (and main) jaw material (e.g. CFC, hBN, etc.)
    which is hard-coded.
    geometry contains a BPM cavity if BPM is True, otherwise old LHC coll. geometry
    wake_calc: flag for wake calculation
    This includes geometric impedance from Stupakov's analytical formula
    (flat tapers), thanks to INFN computations (M. Zobov, O. Frasciello)

    last layer is always stainless steel 304L

    fpar and zpar select the frequencies and distances (for the wake) scans
    (objects of the classes freq_param and z_param).

    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov

    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators

    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    comment is added to the name for IW2D output files
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)
    if queue is not None, it is the lxbatch queue where to launch the calculation.
    if assymetry factor is different from 1, uppper & lower jaws are not at the same
    distance from the beam, and assymetry_factor represents the factor applied to
    the distance to the upper jaw to get that of the lower jaw (can be zero - no lower
    jaw, as in TCDQ)
    param_filename: collimator settings name to distinguish 2012 from postLS1 cases.
    '''


    materials=create_list(materials,n=1);

    if (queue==None):
        # find on which queue to launch calculation (case when lxplusbatch=='launch')
        queues=['2nd','2nd','2nd','2nd','2nd','2nd','1nw'];
        if wake_calc:
            if materials[0].startswith('hBN'): iq=5;
            elif (materials[0]=="C")or(materials[0]=="CFC"): iq=4;
            else: iq=3;
            if (gamma>=3000): iq+=1; # flat top settings -> convergence is slower
        else:
            nfreq=(np.mod(fpar.ftypescan,2)==0)*((np.log10(fpar.fmax)-np.log10(fpar.fmin))*fpar.nflog+1) + (fpar.ftypescan==1)*round((fpar.fmax-fpar.fmin)/fpar.fsamplin)+(fpar.ftypescan==2)*fpar.nrefine;
            iq=max(int(np.ceil(np.log10(nfreq/500.))),0); # =0 up to 500 frequencies; 1 up to 5000; 2 up to 50000; etc.
            iq+=1;
            if materials[0].startswith('Ti_in_TDI'): iq+=2;
        queue=queues[iq];

    # material names convenions
    freqlin=1.e11;b=[halfgap];
    for imat,mat in enumerate(materials):
        if (mat!=None)and(not(isinstance(mat,layer))):
            if (mat.startswith('CU'))or(mat.startswith('Cu')): materials[imat]='Cu300K';
            elif (mat=='C'): materials[imat]='graphite';
            elif (mat.startswith('HBN')): materials[imat]='hBN';freqlin=1.e9;
            elif (mat.startswith('MO')): materials[imat]='Mo';


    print materials, queue, name, thickness;
    Bfield=0; # no magnetoresistance effects in collimators
    # construct layers list
    layers=construct_layers(materials,thickness=thickness,Bfield=Bfield,Age=ageing_factor);
    # add infinite stainless-steel in the end
    layers.append(ss304L_layer());

    if assymetry_factor!=1:
        # assymetric jaws
        b=[halfgap,halfgap*assymetry_factor];
        if assymetry_factor>0:
            # lower layers assumed identical to the upper ones
            layerslow=deepcopy(layers)
            layers.extend(layerslow);


    # construct input file for resistive-wall computation
    iw_input=impedance_wake_input(gamma=gamma,length=length,b=b,
        layers=layers,fpar=fpar,zpar=zpar,freqlinbisect=freqlin,geometry='flat',comment='_'+name+comment);

    imp_mod,wake_mod=imp_model_from_IW2D(iw_input,wake_calc=wake_calc,flagrm=True,lxplusbatch=lxplusbatch,queue=queue,dire=dire);

    if ((name.startswith('TCT')) or (name.startswith('TCSG.4R6'))) and ('2012' not in param_filename):
        # add low frequency mode in TCTs and TCSG in IP6
        print name+' adding peak'
        fpar=freq_param(ftypescan=1,fmin=0.5e8,fmax=3e8,fsamplin=1e6,fadded=[1e-2,0.1,1,1e15]);
        TCTPmodeFileName='/afs/cern.ch/user/d/damorim/work/GitIRIS/LHC_IW_model/Coll_settings/TCTPmode_Vs_fgap_BS.txt';

        fg,r1,r2,q1,q2,f1,f2=np.loadtxt(TCTPmodeFileName, delimiter='\t',skiprows=1,unpack=True);
        hg=fg/2;
        hg_int=halfgap*1000;
        #print hg_int
        r1_int=np.interp(hg_int, hg, r1);
        r2_int=np.interp(hg_int, hg, r2);
        q1_int=np.interp(hg_int, hg, q1);
        q2_int=np.interp(hg_int, hg, q2);
        f1_int=np.interp(hg_int, hg, f1);
        f2_int=np.interp(hg_int, hg, f2);
        listcomp=['Zydip'];
        R=r1_int;Q=q1_int; fr=f1_int; beta=1;
        #print R, Q, fr, listcomp
        imp_res1,wake_res1=imp_model_resonator(R,fr,Q,beta,wake_calc=wake_calc,fpar=fpar,zpar=zpar,listcomp=listcomp);
        add_impedance_wake(imp_mod,imp_res1,1,1);
        add_impedance_wake(wake_mod,wake_res1,1,1);

    imp_mod_RW=rotate_imp_wake(imp_mod,np.pi/2.-angle);
    wake_mod_RW=rotate_imp_wake(wake_mod,np.pi/2.-angle);

    # compute geometric impedance
    fr=fcutoffBB;Q=1; # parameters for broad-band model
    # note: in R there is a factor 2 because there are two tapers
    if BPM:
        print 'Adding BPM taper'
	# tapers parameters with BPM cavity
        l1=(95-37.32-31.9)*1e-3;delta1=8e-3;w1=(33e-3+23.3e-3)/2;
        l2=37.32e-3;delta2=10.7e-3;w2=70e-3/2;
        R1=2*broadband_imp_taper_flat_Stupakov(halfgap,halfgap+delta1,delta1/l1,w1,fr);#,approx=False);
        R2=2*broadband_imp_taper_flat_Stupakov(halfgap+delta1,halfgap+delta1+delta2,delta2/l2,w2,fr);#,approx=False);
        R=R1+R2;
        factwake=1.3; # factor for wake from file (WARNING: rough estimate)
    else:
	print 'Adding Stupakov taper impedance'    
        # tapers parameters without BPM cavity
        w=70e-3/2;l=97e-3;delta=17.6e-3;
        R=2*broadband_imp_taper_flat_Stupakov(halfgap,halfgap+delta,delta/l,w,fr);#,approx=False);
        factwake=1.;

    if (wake_calc)and(flag_wakefiles):
        imp_modg,wake_modg=imp_model_resonator(R,fr,Q,wake_calc=wake_calc,fpar=fpar,
                zpar=zpar,listcomp=['Zlong', 'Zxdip', 'Zydip', 'Zxquad', 'Zyquad']);
        # replace this wake by wake potential simulated by GdFidl (M. Zobov & O. Frasciello - INFN)
        # but keep Stupakov's impedance
        halfgapscan=[1,3,5,11.5,20];wake_modg=[];
        filenamelist_l=[];filenamelist_yd=[];filenamelist_yq=[];
        for hg in halfgapscan[:-1]: filenamelist_l.append(path_here+'Coll_settings/TCS_TCT_geometric/GdfidLWakepotential_long_halfgap'+str(hg)+'mm_bunchlength2mm_mesh0p2mm.txt');
        for hg in halfgapscan: filenamelist_yd.append(path_here+'Coll_settings/TCS_TCT_geometric/GdfidLWakepotential_dip_halfgap'+str(hg)+'mm_bunchlength2mm_mesh0p2mm.txt');
        for hg in halfgapscan: filenamelist_yq.append(path_here+'Coll_settings/TCS_TCT_geometric/GdfidLWakepotential_quad_halfgap'+str(hg)+'mm_bunchlength2mm_mesh0p2mm.txt');

        wake_modg_l=imp_model_from_files(filenamelist_l,halfgapscan[:-1],halfgap,'Wlong',ignored_rows=0,sign=-1)
        wake_modg_yd=imp_model_from_files(filenamelist_yd,halfgapscan,halfgap,'Wydip',ignored_rows=0,sign=-1)
        wake_modg_yq=imp_model_from_files(filenamelist_yq,halfgapscan,halfgap,'Wyquad',ignored_rows=0,sign=-1)

        add_impedance_wake(wake_modg,wake_modg_l,1,1);
        add_impedance_wake(wake_modg,wake_modg_yd,1,1);
        add_impedance_wake(wake_modg,wake_modg_yq,1,1);
        multiply_impedance_wake(wake_modg,factwake);

    else:
        imp_modg,wake_modg=imp_model_resonator(R,fr,Q,wake_calc=wake_calc,fpar=fpar,
                zpar=zpar,listcomp=['Zlong', 'Zxdip', 'Zydip', 'Zxquad', 'Zyquad']);

    imp_mod_geom=rotate_imp_wake(imp_modg,np.pi/2.-angle);
    wake_mod_geom=rotate_imp_wake(wake_modg,np.pi/2.-angle);

    return imp_mod_RW,wake_mod_RW,imp_mod_geom,wake_mod_geom;


def LHC_TDI_iw_model_with_geom(name,halfgap,angle,gamma,wake_calc=False,
        TDIcoating='postLS1',ftypescan=2,nflog=100,zpar=z_param(),
        flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire=''):

    ''' impedance/wake model for the LHC TDI (particular case: 3 blocks)
    TDIcoating: for first block it can be 'preLS1' (5mum Ti) or 'postLS1'
    (1mum NEG + 2mum CU + 0.3mum NEG + 5mum Ti) or directly a list of
    layer objects
    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov

    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators

    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)

    In this version geometric impedance is taken into account (SAME AS FOR
    TCS coll -> BIG WARNING !!!)'''

    # TDI main materials and lengths
    TDImat=[];TDIthickness=[];
    # first block
    if TDIcoating.startswith('preLS1'): TDImat.append(['Ti_in_TDI','hBN']);TDIthickness.append([5e-6]);
    elif TDIcoating.startswith('postLS1'): TDImat.append(['NEG_in_TDI','Cu300K_in_TDI','NEG_in_TDI','Ti_in_TDI','hBN']);TDIthickness.append([1e-6,2e-6,0.3e-6,5e-6]);
    else: TDImat.append(TDIcoating.append('hBN')); # assumes TDIcoating is a list of layer objects defining the coating
    # 2 other blocks
    TDImat.append(['Al']);TDIthickness.append([]);
    TDImat.append(['Cu300K']);TDIthickness.append([]);
    TDIlength=[2.8,0.6,0.7];

    imp_RW=[];wake_RW=[];
    # three different blocks. Note: only RW is cumulated; geom. imp is
    # counted only once (and model yet to be refined)
    for i in range(3):

        if (i==0): fminrefine=8.e8;fmaxrefine=2.e12;nrefine=40000;
        else: fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000;

        imp1,wake1,imp_geom,wake_geom=LHC_singlecoll_iw_model_with_geom(name+'_'+str(i+1),
                TDImat[i],halfgap,angle,gamma,TDIlength[i],thickness=TDIthickness[i],
                wake_calc=wake_calc,fpar=freq_param(ftypescan=ftypescan,nflog=nflog,fminrefine=fminrefine,
                fmaxrefine=fmaxrefine,nrefine=nrefine),zpar=zpar,flag_wakefiles=flag_wakefiles,
                fcutoffBB=fcutoffBB,lxplusbatch=lxplusbatch,
                comment=comment+'_'+TDImat[i][-1]+'_'+float_to_str(round(halfgap*1e5)/1e2)+'mm',dire=dire);
        add_impedance_wake(imp_RW,imp1,1,1);
        add_impedance_wake(wake_RW,wake1,1,1);

    return imp_RW,wake_RW,imp_geom,wake_geom;


def LHC_manycoll_iw_model_with_geom(E,avbetax,avbetay,param_filename,settings_filename,
        beta_filename,wake_calc=False,ftypescan=2,nflog=100,zpar=z_param(),namesref=None,
        coatingmat=None,coatingthickness=0,TDIcoating='postLS1',BPM=False,
        flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire='',
        assymetry_factor_TCL6=1.):

    ''' creates an impedance or wake model for all collimators.
    E is the energy in eV,
    avbetax and avbetay the average beta functions used for the weighting,
    param_filename is the file with all parameters except half-gaps and betas,
    settings_filename is the file with half-gaps (in m),
    beta_filename the file with beta functions (in m),
    wake_calc selects the wake computation if True.
    nflog is the number of frequencies per decade,
    ftypescan the type of frequency scan (0,1 or 2: logarithmic only,
    linear only or logarithmic with refinement around high-frequency resonance(s) ).
    zpar gives the distance scan for the wake.
    namesref are the coll. names (from param_filename) to select (if None take all),
    coatingmat and coatingthickness is the info about an added coating (material
    name + thickness or layer object directly in coatingmat).
    TDIcoating indicates kind of coatgin for first block of TDI: can be 'preLS1'
    (5mum Ti) or 'postLS1' (1mum NEG + 2mum CU + 0.3mum NEG + 5mum Ti) or directly
    a list of layer objects
    BPM: geometry contains a BPM cavity if BPM is True, otherwise old LHC coll. geometry
    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov

    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators

    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)

    assymetry_factor_TCL6: assymetry factor between the distance beam-jaw
    in the case of the TCL6 (1 means that jaws are symmetric).

    In this version, the parameter file can contain several material columns
    (with the associated thickness columns) and the geometric impedance is
    taken into account'''

    e,m0,c,E0=proton_param();
    gamma=E*e/E0;

    # read files
    namesref,material,thick,angle,length,halfgap,betax,betay=read_coll_files_several_mat(param_filename,settings_filename,beta_filename,namesref=namesref);
    #print len(namesref),material,angle,length,halfgap,betax,betay

    # main loop to construct model
    imp_mod_RW=[];wake_mod_RW=[];imp_mod_geom=[];wake_mod_geom=[];
    for iname,name in enumerate(namesref):

        fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000;

        # reorder materials and thicknesses, and add coating in case
        materials=[material[n][iname] for n in range(len(material))];
        thicks=[thick[n][iname] for n in range(0,len(material)-1)];#thicks.append(np.inf);

        assymetry_factor=1;comment_assym=''; # by default, jaws are symmetric
        if name.startswith('TCDQ'): assymetry_factor=0; # single jaw
        if name.startswith('TCL.6'):
            assymetry_factor=assymetry_factor_TCL6; # assymetric jaws for TCL6
        if (assymetry_factor != 1.): comment_assym='_assym'+float_to_str(assymetry_factor);
        imp_RW,wake_RW,imp_geom,wake_geom=LHC_singlecoll_iw_model_with_geom(name,materials,halfgap[iname],angle[iname],gamma,length[iname],thickness=thicks,wake_calc=wake_calc,fpar=freq_param(ftypescan=ftypescan,nflog=nflog,fminrefine=fminrefine,
                fmaxrefine=fmaxrefine,nrefine=nrefine),zpar=zpar,BPM=BPM,
                flag_wakefiles=flag_wakefiles,fcutoffBB=fcutoffBB,lxplusbatch=lxplusbatch,
                comment=comment+'_'+materials[0]+'_'+float_to_str(round(halfgap[iname]*1e5)/1e2)+'mm'+comment_assym,
                dire=dire,assymetry_factor=assymetry_factor,param_filename=param_filename);

        add_impedance_wake(imp_mod_RW,imp_RW,betax[iname]/avbetax,betay[iname]/avbetay);
        add_impedance_wake(wake_mod_RW,wake_RW,betax[iname]/avbetax,betay[iname]/avbetay);
        add_impedance_wake(imp_mod_geom,imp_geom,betax[iname]/avbetax,betay[iname]/avbetay);
        add_impedance_wake(wake_mod_geom,wake_geom,betax[iname]/avbetax,betay[iname]/avbetay);

    return imp_mod_RW,wake_mod_RW,imp_mod_geom,wake_mod_geom;

def LHC_manycoll_iw_model_with_geom_v2(E,avbetax,avbetay,param_filename,wake_calc=False,ftypescan=2,nflog=100,zpar=z_param(),namesref=None,BPM=False,flag_wakefiles=False,fcutoffBB=5e9,lxplusbatch=None,comment='',dire='',assymetry_factor_TCL6=1.,root_result=path_here+'../../../DELPHI_results/LHC'):

    ''' creates an impedance or wake model for all collimators.
    E is the energy in eV,
    avbetax and avbetay the average beta functions used for the weighting,
    param_filename is the file with all parameters and half-gaps and betas,
    wake_calc selects the wake computation if True.
    nflog is the number of frequencies per decade,
    ftypescan the type of frequency scan (0,1 or 2: logarithmic only,
    linear only or logarithmic with refinement around high-frequency resonance(s) ).
    zpar gives the distance scan for the wake.
    namesref are the coll. names (from param_filename) to select (if None take all),
    BPM: geometry contains a BPM cavity if BPM is True, otherwise old LHC coll. geometry
    flag_wakefiles: True to use GdFidl wake potential files instead of Stupakov
    fcutoffBB: cutoff frequency for broad-band model of geometric impedance
    of collimators
    lxplusbatch: if None, no use of lxplus batch system
                   if 'launch' -> launch calculation on lxplus on queue 'queue'
                   if 'retrieve' -> retrieve outputs
    dire contains the directory name where to put the outputs (default='./'=directory of IW2D)
    assymetry_factor_TCL6: assymetry factor between the distance beam-jaw
    in the case of the TCL6 (1 means that jaws are symmetric).
    In this version, the parameter file can contain several material rows
    (with the associated thickness columns) and the geometric impedance is
    taken into account'''

    e,m0,c,E0=proton_param();
    gamma=E*e/E0;

    header,cols=read_multiform_file(param_filename,'\t',1)
    #print header
    ind,namesref=select_col(header,cols,'Name');
    if ind==-1: sys.exit("No Names");
    ind,material=select_col(header,cols,'Material');
    if ind==-1: sys.exit("No Materials");
    ind,thick=select_col(header,cols,'Thickness[m]');
    if ind==-1: sys.exit("No Thickness");
    ind,angle=select_col(header,cols,'Angle[rad]');
    if ind==-1: sys.exit("No Angles");
    ind,length=select_col(header,cols,'Length[m]');
    if ind==-1: sys.exit("No Length");
    ind,halfgap=select_col(header,cols,'Halfgap[m]');
    if ind==-1: sys.exit("No Gaps");
    ind,betax=select_col(header,cols,'Betax[m]');
    if ind==-1: sys.exit("No Betax");
    ind,betay=select_col(header,cols,'Betay[m]');
    if ind==-1: sys.exit("No Betay");
    ind,ageing_factor=select_col(header,cols,'Ageing_factor');
    if ind==-1: ageing_factor=[]; print "No ageing considered."# setting default no ageing on collimator materials.



    # read files

    name_uniq=[];
    [name_uniq.append(n) for n in namesref if n not in name_uniq];
    # main loop to construct model
    imp_mod_RW=[];wake_mod_RW=[];imp_mod_geom=[];wake_mod_geom=[];
    for iname,name in enumerate(name_uniq):
        fminrefine=1.e11;fmaxrefine=5.e12;nrefine=5000
        ind=[];
        materials=[];
        thicks=[];
        betx=[];
        bety=[];
        age=[];

        [ind.append(i) for i,n in enumerate(namesref) if n==name];
        materials=[material[i] for i in ind];
        thicks=[thick[i] for i in ind];
        betx=[betax[i] for i in ind];
        bety=[betay[i] for i in ind];
        if ageing_factor: age=[ageing_factor[i] for i in ind];

        # reorder materials and thicknesses
        assymetry_factor=1;comment_assym=''; # by default, jaws are symmetric
        if name.startswith('TCDQ'): assymetry_factor=0; # single jaw
        if name.startswith('TCL.6'):assymetry_factor=assymetry_factor_TCL6; # assymetric jaws for TCL6
        if (assymetry_factor != 1.): comment_assym='assym'+float_to_str(assymetry_factor);
        else: comment_assym='sym';


        imp_RW,wake_RW,imp_geom,wake_geom=LHC_singlecoll_iw_model_with_geom(name,materials,float(halfgap[ind[0]]),float(angle[ind[0]]),gamma,float(length[ind[0]]),thickness=thicks,ageing_factor=age,wake_calc=wake_calc,fpar=freq_param(ftypescan=ftypescan,nflog=nflog,fminrefine=fminrefine,fmaxrefine=fmaxrefine,nrefine=nrefine),zpar=zpar,BPM=BPM,flag_wakefiles=flag_wakefiles,fcutoffBB=fcutoffBB,lxplusbatch=lxplusbatch,comment='_'+materials[0]+'_'+comment_assym+'_'+comment,dire=dire,assymetry_factor=assymetry_factor,param_filename=param_filename);
	
	imp_RW_weighted=[]	
	wake_RW_weighted=[];
	imp_geom_weighted=[]
	wake_geom_weighted=[];

	add_impedance_wake(imp_RW_weighted,imp_RW,float(betx[0])/avbetax,float(bety[0])/avbetay);
       	add_impedance_wake(imp_geom_weighted,imp_geom,float(betx[0])/avbetax,float(bety[0])/avbetay);
	add_impedance_wake(wake_RW_weighted,wake_RW,float(betx[0])/avbetax,float(bety[0])/avbetay);
       	add_impedance_wake(wake_geom_weighted,wake_geom,float(betx[0])/avbetax,float(bety[0])/avbetay);

	print name	
	write_imp_wake_mod(imp_RW_weighted,"_"+name+'_RW',listcomp=['Zlong','Zxdip','Zydip','Zxquad','Zyquad','Wlong','Wxdip','Wydip','Wxquad','Wyquad'],dire=root_result+'/');

	write_imp_wake_mod(imp_geom_weighted,"_"+name+'_Geom',listcomp=['Zlong','Zxdip','Zydip','Zxquad','Zyquad','Wlong','Wxdip','Wydip','Wxquad','Wyquad'],dire=root_result+'/');
	
	add_impedance_wake(imp_mod_RW,imp_RW_weighted,1,1);
        add_impedance_wake(wake_mod_RW,wake_RW_weighted,1,1);
        add_impedance_wake(imp_mod_geom,imp_geom_weighted,1,1);
        add_impedance_wake(wake_mod_geom,wake_geom_weighted,1,1);

    return imp_mod_RW,wake_mod_RW,imp_mod_geom,wake_mod_geom;
