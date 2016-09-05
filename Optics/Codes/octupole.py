#!/usr/bin/env python
def detuning_coeff(opticsDir):

    import pyoptics as pyopt
    from string import join
    import numpy as np
    from scipy.constants import c
    from particle_param import proton_param

    ### compute optics at octupoles

    filename = opticsDir+'/twiss_lhcb1.tfs'

    t=pyopt.optics.open(filename);
    itemlist=t.dumplist('MO','s l betx bety dx dy');

    outfile=open('octupole.dat', 'w');
    outfile.write("\n".join(itemlist))
    outfile.close();

    print "Optics at octupoles written in "+opticsDir+"/octupole.dat\n"

    ### compute detuning coefficients

    O3 = 63100 # maximum absolute octupolar strength in T/m^3 (from MAD-X)
    e, _, _, _ = proton_param()
    mom = 7000*1e9
    K3 = 6*O3/(mom/c) # K3+ (maximum normalized octupolar strength)

    lengt = t.l[t.pattern('MO')]
    betax = t.betx[t.pattern('MO')]
    betay = t.bety[t.pattern('MO')]

    indF = np.where(betax > (betax.max() * 0.8)) # focuses in X plane means high betax
    indD = np.where(betay > (betay.max() * 0.8)) # defocuses in X plane means high betay

    # not: additional minus sign for the defocusing octupoles because O3D=-O3F for
    # the same current in foc. and defoc. octupoles

    axF  =  np.sum(lengt[indF]*betax[indF]**2)*K3/(16*np.pi);
    axD  = -np.sum(lengt[indD]*betax[indD]**2)*K3/(16*np.pi);
    ayF  =  np.sum(lengt[indF]*betay[indF]**2)*K3/(16*np.pi);
    ayD  = -np.sum(lengt[indD]*betay[indD]**2)*K3/(16*np.pi);
    axyF = -np.sum(lengt[indF]*betax[indF]*betay[indF])*K3/(8*np.pi);
    axyD =  np.sum(lengt[indD]*betax[indD]*betay[indD])*K3/(8*np.pi);


    coeff_oct = [axF , axD, ayF , ayD, axyF , axyD]
    print "Detuning coefficients: "+str(coeff_oct)+"\n"

    np.savetxt('coeff_oct.dat', coeff_oct);
    print "Detuning matrix from octupoles written in "+opticsDir+"/coeff_oct.dat\n"
    
    return coeff_oct

def qsec_coeff(opticsDir):

    import pyoptics as pyopt
    from string import join
    import numpy as np
    from scipy.constants import c
    from particle_param import proton_param

    ### compute optics at octupoles

    filename = opticsDir+'/twiss_lhcb1.tfs'

    t=pyopt.optics.open(filename);
    itemlist=t.dumplist('MO','s l betx bety dx dy');

    outfile=open('octupole.dat', 'w');
    outfile.write("\n".join(itemlist))
    outfile.close();

    print "Optics at octupoles written in "+opticsDir+"/octupole.dat\n"

    ### compute detuning coefficients

    O3 = 63100 # maximum absolute octupolar strength in T/m^3 (from MAD-X)
    e, _, _, _ = proton_param()
    mom = 7000*1e9
    K3 = 6*O3/(mom/c) # K3+ (maximum normalized octupolar strength)

    lengt = t.l[t.pattern('MO')]
    betax = t.betx[t.pattern('MO')]
    betay = t.bety[t.pattern('MO')]
    dx =    t.dx[t.pattern('MO')]
    dy =    t.dy[t.pattern('MO')]

    indF = np.where(betax > (betax.max() * 0.8)) # focuses in X plane means high betax
    indD = np.where(betay > (betay.max() * 0.8)) # defocuses in X plane means high betay

    # not: additional minus sign for the defocusing octupoles because O3D=-O3F for
    # the same current in foc. and defoc. octupoles

    qsecxF =  np.sum(lengt[indF]*betax[indF]*dx[indF]**2)*K3/(4*np.pi);
    qsecxD = -np.sum(lengt[indD]*betax[indD]*dx[indD]**2)*K3/(4*np.pi);
    qsecyF = -np.sum(lengt[indF]*betay[indF]*dx[indF]**2)*K3/(4*np.pi);
    qsecyD =  np.sum(lengt[indD]*betay[indD]*dx[indD]**2)*K3/(4*np.pi);

    qsec = [qsecxF, qsecxD, qsecyF, qsecyD]
    print "Q'' values: "+str(qsec)+"\n"

    np.savetxt('qsec.dat', a);
    print "Q'' from octupoles written in "+opticsDir+"/qsec.dat"
    
    return qsec
