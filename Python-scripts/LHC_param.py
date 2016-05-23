#!/usr/bin/python

import sys
import commands
# import local libraries if needed
pymod=commands.getoutput("echo $PYMOD");
if pymod.startswith('local'):
    py_numpy=commands.getoutput("echo $PY_NUMPY");sys.path.insert(1,py_numpy);

from string import *
import numpy as np
from string_lib import *
from DELPHI import Qs_from_RF_param

def LHC_param(E0,E=6.5e12,scenario='Nominal LHC'):

    ''' generate typical LHC parameters, given the proton rest energy E0 in J (from e.g. function
    proton_param) and the beam energy E in eV.
    Outputs:
    - machine: string with machine name,
    - E: same as input (beam energy in eV),
    - gamma: relativistic mass factor,
    - sigmaz: RMS bunch length in m,
    - taub: total bunch length in s (4*RMS),
    - R: machine pysical radius (circumference/(2 pi)),
    - Qx: total horizontal tune (integer + fractional parts),
    - Qxfrac: fractional horizontal tune,
    - Qy: total vertical tune (integer + fractional parts),
    - Qyfrac: fractional vertical,
    - Qs: synchrotron tune,
    - eta: slippage factor (alpha_p-1/gamma^2),
    - f0: revolution frequency,
    - omega0: revolution angular frequency=2pi*f0,
    - omegas: synchrotron angular frequency=Qs*omega0,
    - dphase: phase of damper w.r.t. "normal" purely resistive damper,
    - Estr: string with energy (e.g. '7TeV', '450GeV', etc. - see below),
    - V: RF voltage in V,,
    - h: harmonic number.

    NB: 4-06-2015: updated bunch length values to 9cm, i.e. 1.2ns 4-rms-sigma, 
    as in the LHC operation.
    '''
    
    # E is the energy in eV, V the RF voltage in V
    if (E==6.5e12): 
	    if scenario=='Nominal LHC':
		V=16e6
		Estr='6p5TeV';
		taub=1.2e-9;
	        M=2748
        	en=2.5
    elif (E==4e12): 
	    if scenario=='Nominal LHC':
		    V=12e6
		    Estr='4TeV';
		    taub=1.25e-9; # full length in s
	            M=2748
        	    en=2.5
    elif (E==450e9): 
	    if scenario=='Nominal LHC':
		    V=6e6
		    Estr='450GeV';
		    taub=1.5e-9; # full length in s
	            M=2748
        	    en=2.5
    else:
    	print "LHC energy not recognized; set taub=1.2ns, V=12 MV";
	V=12e6;
	Estr=float_to_str(E/1e12)+'TeV';
	taub=1.2e-9; # full length in s

    e=1.602176487e-19; # elementary charge
    c=299792458;
    # fixed parameters
    machine='LHC';
    h=35640; # harmonic number
    gamma=E*e/E0
    beta=np.sqrt(1.-1./(gamma**2))
    sigmaz=taub*beta*c/4.; # RMS bunch length (m)
    circ=26658.883; # total circumference in m
    R=circ/(2.*np.pi) # machine radius
    Qx=64.31;Qxfrac=Qx-np.floor(Qx);
    Qy=59.32;Qyfrac=Qy-np.floor(Qy);
    alphap=3.225e-4; # momentum compaction factor
    eta=alphap-1./(gamma*gamma); # slip factor
    
    # compute Qs from RF parameters
    Qs=Qs_from_RF_param(V,h,gamma,eta,phis=0.,particle='proton');
    f0=c*beta/circ # rev. frequency
    omega0=2.*np.pi*f0;
    omegas=Qs*omega0;
    dphase=0.; # additional damper phase



    return machine,E,gamma,sigmaz,taub,R,Qx,Qxfrac,Qy,Qyfrac,Qs,eta,f0,omega0,omegas,dphase,Estr,V,h,M,en;

class LHC(object):
	def __init__(self,E0,E,scenario):
		self.name, self.E, self.gamma,self.sigmaz,self.taub,self.R,self.Qx,self.Qxfrac,self.Qy,self.Qyfrac,self.Qs,self.eta,self.f0,self.omega0,self.omegas,self.dphase,self.Estr,self.V,self.h,self.M,self.en=LHC_param(E0,E,scenario)
		
