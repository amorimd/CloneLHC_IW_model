#!/usr/bin/python

import sys
import commands


from string import *
import os 
import numpy as np
from io_lib import *

path_here=os.getcwd()+'/';
namefile=path_here+'aperture_transition.txt';
header,cols=read_multiform_file(namefile,'\t',1);

trans_type=[];
[trans_type.append(el[1]) for el in cols];
name_type=[];
[name_type.append(el[0]) for el in cols];

namefile=path_here+'warm_transition.txt';
header,cols=read_multiform_file(namefile,'\t',1);

name=[];
[name.append(el[8]) for ind,el in enumerate(cols)];
beam=[];
[beam.append(el[9][-1]) for ind,el in enumerate(cols)];
position=[];
[position.append(el[4]) for ind,el in enumerate(cols)];

aperture=[];
for el in name:
	print el
	try:
		ind=name_type.index(el);
		print ind
		aperture.append(trans_type[ind])
	except ValueError:
		ind=-1;
		aperture.append('60-60')

namefile1='vacuum_B1.txt';
namefile2='vacuum_B2.txt';
fa1=open(namefile1,'w');
fa2=open(namefile2,'w');

for i,el in enumerate(name):
	if '60-60' not in aperture[i] and ('B' in beam[i] or 'X' in beam[i]):
		fa1.write(str(name[i])+'\t'+str(beam[i])+'\t'+str(aperture[i])+'\t'+str(position[i])+'\n');
	elif '60-60' not in aperture[i] and ('R' in beam[i] or 'X' in beam[i]):
		fa2.write(str(name[i])+'\t'+str(beam[i])+'\t'+str(aperture[i])+'\t'+str(position[i])+'\n');
			
a_vec=[];
[a_vec.append(float(str.split(el,'-')[0])) for el in aperture];
a_vec=(np.asarray(a_vec)*1e-3);
b_vec=[];
[b_vec.append(float(str.split(el,'-')[1])) for el in aperture];
b_vec=(np.asarray(b_vec)*1e-3);

Z0=120*np.pi;
theta=15*2*np.pi/360;
Zdip=1j*Z0/2/np.pi*np.tan(theta)*np.abs(1./a_vec-1./b_vec);
avbetaY=70;
print sum(Zdip)*avbetaY


