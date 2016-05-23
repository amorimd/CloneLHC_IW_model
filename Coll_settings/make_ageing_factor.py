#!/usr/bin/python

import numpy as np
from string import replace

age=np.arange(1,4.2,0.2);

for age_val in age:
	f=open('Coll_table_2012_4000GeV_B1.txt','r');	
	name='Coll_table_2012_4000GeV_B1_AgeFactXXX.txt';
	namefile=name.replace('XXX',str(age_val));
	print 'making '+namefile+'...'
	g=open(namefile,'w');
	head=f.readline().replace('\n','');
	g.write(head+'\t'+'Ageing_factor'+'\n');
	for line in f:
		if '\n' in line:
			g.write(line.replace('\n','')+'\t'+str(age_val)+'\n');
		else:
			g.write(line+'\t'+str(age_val));
	g.close();
f.close();
