% Compare collimator settings


clear all;
close all;
addpath(genpath('/afs/cern.ch/user/n/nbiancac/scratch0/Matlab-scripts/'));

% Directories

% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% namefile='LHC_MD_4291_span';
% system(['mkdir -p ',ResultDir]);

% DataDir1='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/';
% file1='HL-LHC_15cm_7TeV_baseline_B1.txt';
% file1='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_IR3_open_B1.txt';
% file1='LHC_ft_6.5TeV_B1_4290_TCSG_IP7_6.5s.txt';
% DataDir2='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/';
% file2='LHC_ft_6.5TeV_B1_4291_TCSG_IP7_20s.txt';

% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD/Results/';
% namefile='LHC_';
% system(['mkdir -p ',ResultDir]);
% 
% DataDir1='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/';
% file1='LHC_ft_6.5TeV_B1.txt';
% DataDir2='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/';
% file2='LHC_ft_6.5TeV_B1_MD4290-4291_TCSG_IP7_2sigma_retracted.txt';

ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';

system(['mkdir -p ',ResultDir]);

lista.file=[{'LHC_ft_6.5TeV_B1_2016.txt'}];
lista.DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/'},1,length(lista.file));
namefile='LHC_6.5sigma';

% % injection w/wo TDI 2016
% lista.file=[{'LHC_inj_450GeV_B1_2016.txt'},{'LHC_inj_TDI_hg3.8mm_450GeV_B1_2016.txt'}];
% lista.DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/'},1,length(lista.file));
% namefile='LHC_inj_TDI_2016';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)

% 
% lista.file=[{'LHC_ft_6.5TeV_B1_2016.txt'},{'LHC_40cm_6.5TeV_B1_2016_TCL_out.txt'},{'LHC_50cm_tight_6.5TeV_B1_2016_TCL_out.txt'}];
% lista.DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/'},1,length(lista.file));
% namefile='LHC_tight_overview';

% lista.DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/'},1,1);
% lista.file=[{'HL-LHC_15cm_7TeV_baseline_B1.txt'}];

% lista.file=[
% {'HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1.txt'},...      
% {'HL-LHC_15cm_7TeV_MoC_IP7_TCT5_B1.txt'},...
%             ];
% lista.DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/'},1,length(lista.file));        
% commentsave='';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/Results/';
% mkdir(ResultDir)


flagshow='on';
flagsave=0;

%% script
close all;

legend_vec=regexprep(lista.file,[{'_'},{'.txt'}],[{' '},{''}]);
col_vec=distinguishable_colors(length(legend_vec));
h1_vec=[];h2_vec=[];h3_vec=[]; h4_vec=[];h5_vec=[]; h6_vec=[];
for ii=1:length(lista.file)
    
    file1=char(lista.file(ii));
    DataDir1=char(lista.DataDir(ii));
    
    name_gaps=[namefile,'-gaps'];
    name_gaps_ratio=[namefile,'-gaps-ratio'];
    name_betay=[namefile,'-bety'];
    name_betax=[namefile,'-betx'];
    name_sigma=[namefile,'-sigma'];
    name_tsx=[namefile,'-tsx'];
    name_tsy=[namefile,'-tsy'];
    [names1,gaps1,betx1,bety1,sigma1]=read_coll_file([DataDir1,file1],'all','unique');

    disp(['Total collimators in ',file1,':  ',num2str(length(names1))]);

    % correct small bugs
    ind= ismember(names1,'TCTVB.4L8');
    names1(ind)={'TCTVB.4L8.B1'};
    ind= ismember(names1,'TCLIA.4R2');
    names1(ind)={'TCLIA.4R2.B1'};
    ind= ismember(names1,'TCDQA.A4R6.B');
    names1(ind)={'TCDQA.A4R6.B1'};
    ind= ismember(names1,'TCDQA.B4R6.B');
    names1(ind)={'TCDQA.B4R6.B1'};
    ind= ismember(names1,'TCDQA.C4R6.B');
    names1(ind)={'TCDQA.C4R6.B1'};
    ind= ismember(names1,'TCTVA.4L8.B1');
    names1(ind)={'TCTVB.4L8.B1'};
    ind= ismember(names1,'TCLIA.4R2');
    names1(ind)={'TCLIA.4R2.B1'};
    ind= ismember(names1,'TCTVA.4L5.B1');
    names1(ind)={'TCTV.4L5.B1'};
    ind= ismember(names1,'TCTVA.4L1.B1');
    names1(ind)={'TCTV.4L1.B1'};

    if ii==1; names=names1; end
    
% [names2,gaps2,betx2,bety2,sigma2,angle2]=read_coll_file([DataDir2,file2],'all','unique');
% 
% disp(['Total collimators in 2:',num2str(length(names2))])
% 
% % correct small bugs
% ind= ismember(names2,'TCTVB.4L8');
% names2(ind)={'TCTVB.4L8.B1'};
% ind= ismember(names2,'TCLIA.4R2');
% names2(ind)={'TCLIA.4R2.B1'};
% ind= ismember(names2,'TCDQA.A4R6.B');
% names2(ind)={'TCDQA.A4R6.B1'};
% ind= ismember(names2,'TCDQA.B4R6.B');
% names2(ind)={'TCDQA.B4R6.B1'};
% ind= ismember(names2,'TCDQA.C4R6.B');
% names2(ind)={'TCDQA.C4R6.B1'};
% ind= ismember(names2,'TCTVA.4L8.B1');
% names2(ind)={'TCTVB.4L8.B1'};
% ind= ismember(names2,'TCLIA.4R2');
% names2(ind)={'TCLIA.4R2.B1'};
% ind= ismember(names2,'TCTVA.4L5.B1');
% names2(ind)={'TCTV.4L5.B1'};
% ind=find(ismember(names2,'TCTVA.4L1.B1'));
% names2(ind)={'TCTV.4L1.B1'};
% 

    % intersect models
    [c1,ia1,ib1] = intersect(names1,names,'stable');
    name_int=c1;
    gaps1_int=gaps1(ia1);
    % gaps2_int=gaps2(ib1);
    bety1_int=bety1(ia1);
    % bety2_int=bety2(ib1);
    betx1_int=betx1(ia1);
    % betx2_int=betx2(ib1);
    sigma1_int=sigma1(ia1);
    % sigma2_int=sigma2(ib1);
    

    % compare gaps
    figure(1);
    set(gcf,'visible',flagshow)
    X=[gaps1_int(1);gaps1_int]*1e3;
    Y=1:length(gaps1_int)+1;
    name=[{''};name_int];
    h1=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    xlim([0 25])
    ylim([1 length(name)])
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('half gap [mm]')
    box on
    set(gcf,'position',[ 457     1   512   661]);


    h1_vec=[h1_vec,h1];

    % compare sigmas
    figure(2);
    set(gcf,'visible',flagshow)
    X=[sigma1_int(1);sigma1_int];
    Y=1:length(sigma1_int)+1;
    name=[{''};name_int];
    xlim([0 35])
    ylim([1 length(name)])
    h=vline(5:5:35,'-'); hold on;
    set(h,'color',[0.5 0.5 0.5])
    h2=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('number of \sigma')
    box on
    set(gcf,'position',[ 457     1   512   661]);
    h2_vec=[h2_vec,h2];


    % compare betasy
    figure(3);
    set(gcf,'visible',flagshow)
    X=[bety1_int(1);bety1_int];
    Y=1:length(gaps1_int)+1;
    name=[{''};name_int];
    h3=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    ylim([1 length(name)])
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('\beta_y [m]')
    box on
    legend([h1,h2],legend_vec,'location','best','position',[ 0.1802    0.9276    0.7354    0.0690])
    set(gcf,'position',[ 774     1   512   661]);
    h3_vec=[h3_vec,h3];

    % compare betasx
    figure(4);
    set(gcf,'visible',flagshow)
    X=[betx1_int(1);betx1_int];
    Y=1:length(gaps1_int)+1;
    name=[{''};name_int];
    h4=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    ylim([1 length(name)])
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('\beta_x [m]')
    box on
    legend([h1,h2],legend_vec,'location','best','position',[ 0.1802    0.9276    0.7354    0.0690])
    set(gcf,'position',[ 774     1   512   661]);
    h4_vec=[h4_vec,h4];

      % compare betasx / hg^3
    figure(5);
    set(gcf,'visible',flagshow)
    Xb=[betx1_int(1);betx1_int];
    Xg=[gaps1_int(1);gaps1_int]*1e3;
    X=Xb./Xg.^3;
    Y=1:length(gaps1_int)+1;
    name=[{''};name_int];
    h5=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    ylim([1 length(name)])
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('\beta_x./halfgap^3 [1/m^2]')
    box on
    legend([h1,h2],legend_vec,'location','best','position',[ 0.1802    0.9276    0.7354    0.0690])
    set(gcf,'position',[ 774     1   512   661]);
    h5_vec=[h5_vec,h5];
    
      % compare betasy / hg^3
    figure(6);
    set(gcf,'visible',flagshow)
    Xb=[bety1_int(1);bety1_int];
    Xg=[gaps1_int(1);gaps1_int]*1e3;
    X=Xb./Xg.^3;
    Y=1:length(gaps1_int)+1;
    name=[{''};name_int];
    h6=stairs(X,Y,'color',col_vec(ii,:)); hold on;
    for kk=1:length(Y)-1
    h=line([0 X(kk+1)],[.5+kk .5+kk]);
    set(h,'linestyle',':','color',col_vec(ii,:))
    end
    ylim([1 length(name)])
    set(gca,'ytick',1.5:length(name))
    set(gca,'yticklabel',name(2:end))
    xlabel('\beta_y./halfgap^3 [1/m^2]')
    box on
    legend([h1,h2],legend_vec,'location','best','position',[ 0.1802    0.9276    0.7354    0.0690])
    set(gcf,'position',[ 774     1   512   661]);
    h6_vec=[h6_vec,h6];
    
end


figure(1)
name=[name_gaps];
legend(h1_vec,legend_vec,'location','northeast');%''position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

figure(2)
name=[name_sigma];
legend(h2_vec,legend_vec,'location','best');%,'position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

figure(3)
name=[name_betay];
legend(h3_vec,legend_vec,'location','best');%,'position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

figure(4)
name=[name_betax];
legend(h4_vec,legend_vec,'location','best');%,'position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

figure(5)
name=[name_tsx];
legend(h4_vec,legend_vec,'location','best');%,'position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

figure(6)
name=[name_tsy];
legend(h4_vec,legend_vec,'location','best');%,'position',[ 0.1802    0.9276    0.7354    0.0690])
if flagsave==1
    disp(name)
    s=hgexport('readstyle','PRSTAB-6pt');
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

%%


% missing elements
gaps1(ia1)=[];
names1(ia1)=[];
bety1(ia1)=[];

gaps2(ib1)=[];
names2(ib1)=[];
bety2(ib1)=[];

disp(['Elements in 1 not in 2:'])
for ii=1:length(gaps1); disp([char(names1(ii)),' with half gap of ',num2str(gaps1(ii)*1e3),' mm']); end

disp(['Elements in 2 not in 1:'])
for ii=1:length(gaps2); disp([char(names2(ii)),' with half gap of ',num2str(gaps2(ii)*1e3),' mm']); end

