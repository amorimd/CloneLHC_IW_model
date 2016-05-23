% 
% Script to calculate SD from octupole settings in MAD-X files.
% 

clear all;
close all;
addpath(genpath('/afs/cern.ch/user/n/nbiancac/scratch0/Matlab-scripts/'));

%% Complex tune shift for chosen M, damper, Nb, versus  Qp
clear all;
close all;
clc;

scenario='LHC_inj_450GeV_B1_2015';
% scenario='LHC_inj_TDI_hg3.8mm_450GeV_B1_2015';
% scenario='LHC_inj_TDI_hg5.0mm_450GeV_B1_2015';
% scenario='LHC_inj_TDI_hg10.0mm_450GeV_B1_2015';
% scenario='LHC_inj_450GeV_B1_2016';
% scenario='LHC_inj_TDI_hg3.8mm_450GeV_B1_2016';
% scenario='LHC_inj_TDI_hg3.8mm_noCu-noTi_450GeV_B1_2016';
scenario='LHC_inj_TDI_hg3.8mm_noCu_450GeV_B1_2016';
% scenario='LHC_inj_TDI_hg5.0mm_450GeV_B1_2016';
% scenario='LHC_inj_TDI_hg10.0mm_450GeV_B1_2016';
mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/';

% scenario='LHC_inj_450GeV_B1_2015_TDI2_5.0mm';
% scenario='LHC_inj_450GeV_B1_2015_TDI2_10.0mm';
% scenario='LHC_inj_450GeV_B1_2015_TDI8_5.0mm';
% scenario='LHC_inj_450GeV_B1_2015_TDI8_10.0mm';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII_TDI_measured/';

% scenario='LHC_ft_6.5TeV_B1';
% % scenario='LHC_ft_6.5TeV_B1_2016';
% % scenario='LHC_40cm_6.5TeV_B1_2016_TCL_out';
% scenario='LHC_50cm_relaxed_6.5TeV_B1_2016_TCL_out';
% % scenario='LHC_50cm_tight_6.5TeV_B1_2016_TCL_out';
% scenario='LHC_80cm_6.5TeV_B1_2015_TCL_out';

% % scenario='LHC_40cm_6.5TeV_B1_2016_TCL_out_5umTiN+CFC_IP7';
% % scenario='LHC_40cm_6.5TeV_B1_2016_TCL_out_5umCu+CFC_IP7';
% % scenario='LHC_40cm_6.5TeV_B1_2016_TCL_out_5umMo+CFC_IP7';

% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/';
% scenario='LHC_ft_6.5TeV_B1_4291_TCSG_IP7_20s';
% scenario='LHC_ft_6.5TeV_B1_4290_TCSG_IP7_6.5s';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD/';

% scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
scenario='HLLHC_7TeV_DQW_20151001_IP1-IP5';
mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/';

% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/SepRate-60cm/';
% scenario='HLLHC_60cm_7TeV_B1_2016';

% scenario='HL-LHC_15cm_7TeV_baseline_TCT5_B1';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/';

% scenario='HLLHC_7TeV_DQW_update_IP1-IP5';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/Crab_AllHOM/';

% scenario='HL-LHC_15cm_7TeV_baseline_B1';
% scenario='HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_5-TCSG';
% scenario='HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_5-TCSG';
% scenario='HL-LHC_15cm_7TeV_baseline_B1_5umTiN+MoC_5-TCSG';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/';

% scenario='HL-LHC_15cm_7TeV_baseline_B1';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/';

% scenario='LHC_60cm_4TeV_2012_B1';
% scenario='LHC_60cm_4TeV_19062012-23h48m00_B2';
% scenario='LHC_60cm_4TeV_23062012-20h00m00_B2';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/Intability_2012/';


% scenario='HLLHC_60cm_7TeV_B1_2016';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/SepRate-60cm/';

% scenario='HL-LHC_15cm_7TeV_baseline_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1';

% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/';


% scenario='HL-LHC_15cm_7TeV_baseline_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1';

% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/';


ResultDir=[mainDir,'Results/']; system(['mkdir -p ',ResultDir]);
DataDir=[mainDir,scenario,'/'];
% 64.2174   58.5732   47.9586
%    84.5094   80.9046   70.8432

epsnorm=2.5e-6; % for SD and IE
epsnorm_scaled=2e-6; % for scaling fSD
Nb_scaled=1e11; % for scaling SD
Q_plot=14; % for IE
% !kinit
flagsave=1;
flagshow='off';

% for Nb_vec=[1e10, 1.1e11, 2.1e11, 3.1e11, 4.1e11];
for Nb_vec=[2.2e11];
    Nb_val=Nb_vec;
for damp_vec=[{'0p02'}]
% for damp_vec=[{'0p02'}]
    damp=char(damp_vec);
for M_vec=[{'2748'}];
    M=char(M_vec);

   
for plane_vec=[{'x'}];
    plane=char(plane_vec);




if strfind(scenario,'450GeV')
    disp('LHC 450 GeV model')
    comment='';
    namefile=['data_vs_Qp_LHC_450GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    namefile_all=['data_vs_Qp_all_LHC_450GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,450e9,'Nominal LHC');
    machine.M=M;
elseif strfind(scenario,'6.5TeV')
    disp('LHC 6.5 TeV model')
    comment='';
    namefile=['data_vs_Qp_LHC_6500GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    namefile_all=['data_vs_Qp_all_LHC_6500GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,6500e9,'Nominal LHC');
    machine.M=M;
elseif strfind(scenario,'2012')
    disp('LHC 2012 4 TeV model')
    comment='';
    namefile=['data_vs_Qp_LHC_4000GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    namefile_all=['data_vs_Qp_all_LHC_4000GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,4000e9,'Nominal LHC');
    machine.M=M;
elseif strncmp('HLLHC',regexprep(scenario,'-',''),5) && strfind(regexprep(scenario,'-',''),'7TeV') 
    disp('HLLHC 7 TeV model')
    [~,~,~,E0]=particle_param('proton');
    machine=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
    machine.M=M;
    comment='';
    cd([mainDir,'/',scenario])
    namefile=['data_vs_Qp_HLLHC_7000GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
    namefile_all=['data_vs_Qp_all_HLLHC_7000GeV',scenario,'_',M,'b_d',damp,'_NbNPAR_converged_',plane];
% elseif ~isempty(strncmp('HLLHC',regexprep(scenario,'-',''),5)) && ~isempty(strfind(regexprep(scenario,'-',''),'7TeV')) && (~isempty(strfind(regexprep(scenario,'-',''),'RFD')) || ~isempty(strfind(regexprep(scenario,'-',''),'DQW')))
%     disp('HLLHC 7 TeV model')
%     [~,~,~,E0]=particle_param('proton');
%     machine=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
%     machine.M=M;
%     comment='';
%     caseFM='RovQ';
%     model_crab_scenario='Crab+HLLHC';
%     spreadmode='On';
%     casenum=1;
%     if floor(Nb_val/1e10)
%         namefile=['data_vs_Qp_FM',caseFM,'_M',M,'_Nb',[regexprep(sprintf('%.1f',Nb_val/1e10),'\.','p'),'e10'],'_d',damp,'_model',model_crab_scenario,'_spread',spreadmode,'_case',num2str(casenum),'_x'];
%         namefile_all=['data_vs_Qp_all_FM',caseFM,'_M',M,'_Nb',[regexprep(sprintf('%.1f',Nb_val/1e10),'\.','p'),'e10'],'_d',damp,'_model',model_crab_scenario,'_spread',spreadmode,'_case',num2str(casenum),'_x'];
%     elseif floor(Nb_val/1e11)
%         namefile=['data_vs_Qp_FM',caseFM,'_M',M,'_Nb',[regexprep(sprintf('%.1f',Nb_val/1e11),'\.','p'),'e11'],'_d',damp,'_model',model_crab_scenario,'_spread',spreadmode,'_case',num2str(casenum),'_x'];
%         namefile_all=['data_vs_Qp_all_FM',caseFM,'_M',M,'_Nb',[regexprep(sprintf('%.1f',Nb_val/1e11),'\.','p'),'e11'],'_d',damp,'_model',model_crab_scenario,'_spread',spreadmode,'_case',num2str(casenum),'_x'];
%     end
else
    warning('Unknown machine!!!');
end

Q_all_vec=[];
Q_vec=[];
Qp_vec=[];

if ~mod(Nb_val,1e11)
   namefile2=regexprep(namefile,'NPAR',[sprintf('%.0d',Nb_val/1e11),'e11']);
   namefile2_all=regexprep(namefile_all,'NPAR',[regexprep(sprintf('%.0f',Nb_val/1e11),'\.','p'),'e11']);
else
   namefile2=regexprep(namefile,'NPAR',[regexprep(sprintf('%.1f',Nb_val/1e11),'\.','p'),'e11']);
   namefile2_all=regexprep(namefile_all,'NPAR',[regexprep(sprintf('%.1f',Nb_val/1e11),'\.','p'),'e11']);
end

try 
    Lre=dlmread([DataDir,namefile2,'_real.dat'],'',0,0);
    Lim=dlmread([DataDir,namefile2,'_imag.dat'],'',0,0);
catch 
    Lre=dlmread([DataDir,namefile2,'_real.dat'],'',1,0);
    Lim=dlmread([DataDir,namefile2,'_imag.dat'],'',1,0);
end

Qp_vec=Lre(:,1);
Q_vec=Lre(:,2)+1i*Lim(:,2);

if sum(isnan(Q_vec))>0
    sumnan=sum(isnan(Q_vec));
    disp([num2str(sumnan),'nan in Q data. Interpolating around.'])
    ind=find(isnan(Q_vec)==1);
    Q_vec(ind)=nan;
end

disp([num2str(length(Q_vec)),' values found for Q''']);

try Lre=dlmread([DataDir,namefile2_all,'_real.dat'],'',1,0);
    Lim=dlmread([DataDir,namefile2_all,'_imag.dat'],'',1,0);
    Q_all_vec=Lre(:,2:end)+1i*Lim(:,2:end);
    disp([num2str(size(Q_all_vec,2)),' values found for all the unstable modes Q'' ']);
catch, warning('No data_vs_Qp_all files..');
end

damp_title_str=['=',num2str(1/eval(regexprep(damp,'p','.'))),' turns'];
% %  
% %%  MUM
% figure(1);
% set(gcf,'visible',flagshow)
% for Qp_select=Q_plot;
%     iQp=find(ismember(Qp_vec,Q_plot)==1);
%     for kk=1:size(Q_all_vec,2) 
%         h1=plot((real(Q_all_vec(iQp,kk))-round(real(Q_all_vec(iQp,kk))./machine.Qs)*machine.Qs)/1e-4,-imag(Q_all_vec(iQp,kk))/1e-4,'or','markersize',5,'markerfacecolor','r'); hold on;
%     end
%     h2=plot((real(Q_vec(iQp))-round(real(Q_vec(iQp))./machine.Qs)*machine.Qs)/1e-4,-imag(Q_vec(iQp))/1e-4,'ok','markerfacecolor','k'); hold on;
% end
% h=hline(0,'k'); set(h,'color',[.5 .5 .5])
% h=vline(0,'k'); set(h,'color',[.5 .5 .5])
% 
% hold off;
% title(regexprep(['Mum_Qp',num2str(Qp_vec(iQp)),'_d',damp_title_str,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))
% legend([h1,h2],'unstable mode (u.m.)','most unstable mode','location','best'); 
% legend boxon
% ylabel('-Im(\DeltaQ) [10^{-4}]');xlabel('Re(\DeltaQ) [10^{-4}]')
% grid on;
% 
% if flagsave
%     name=[scenario,'_','Mum_Qp',num2str(Qp_vec(iQp)),'_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
%     s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='15';s.width='20'; set(gcf,'PaperType','A3')
%     hgexport(gcf,'',s,'applystyle',true);
%     set(gcf,'position',[417   120   709   532])
%     set(gca,'position',[ 0.1185    0.1955    0.7221    0.7103])
%     saveas(gcf, [ResultDir,name,'.fig'],'fig');
%     hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
%     hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
%     disp([ResultDir,name,comment,'.png'])
% end
% 
% name=[scenario,'_','Mum_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
% dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,Q_all_vec],'delimiter','\t','precision',8)
% 
% figure(11);
% set(gcf,'visible',flagshow)
% col_vec=hot(length(Qp_vec));
% for iQp=1:length(Qp_vec);
%     
%     for kk=1:size(Q_all_vec,2) 
%         h1=plot((real(Q_all_vec(iQp,kk))-0*round(real(Q_all_vec(iQp,kk))./machine.Qs)*machine.Qs)/1e-4,-imag(Q_all_vec(iQp,kk))/1e-4,'o','color',[.5 .5 .5],'markersize',5,'markerfacecolor',[.5 .5 .5]); hold on;
%     end
%     h2=plot((real(Q_vec(iQp))-0*round(real(Q_vec(iQp))./machine.Qs)*machine.Qs)/1e-4,-imag(Q_vec(iQp))/1e-4,'ok','markerfacecolor',col_vec(iQp,:)); hold on;
% end
% h=hline(0,'k'); set(h,'color',[.5 .5 .5])
% h=vline(0,'k'); set(h,'color',[.5 .5 .5])
% colormap(col_vec);
% h=colorbar;
% set(h,'YTick',1:2:41);
% set(h,'YTicklabel',Qp_vec(1:2:end));
% ylabel('-Im(\DeltaQ) [10^{-4}]');xlabel('Re(\DeltaQ) [10^{-4}]');
% grid on;

%% ImQ vs Q'

c=hsv(length(Nb_val));
for ii=1:length(Nb_val)
    figure(2);
    set(gcf,'visible',flagshow)
    plot(Qp_vec,-imag(Q_vec(:,(ii)))/1e-4,'color',c(ii,:),'linewidth',2);
    hold on;
    try 
        for kk=1:size(Q_all_mat,2)
            plot(Qp_vec,-imag(Q_all_vec{ii}(:,kk))/1e-4,'.','color','k','linewidth',1);
        end
    catch, 'exception';
    end
    
end

% ylim([0 max(-imag(Q_vec(:,(ii)))/1e-4)])
% xlim([-20 20])
grid on;
title(regexprep(['Im(\DeltaQ)_vs_Q''_d',damp_title_str,'_plane ',plane,'_M',M,' Nb',num2str(Nb_val/1e11),'e11 ',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))
xlabel('Q''');
ylabel('-Im(\DeltaQ) [10^{-4}]');

if flagsave
    name=[scenario,'_','ImQ_vs_Qp_d',damp,'_plane_',plane,'_M',M,'_Nb',num2str(Nb_val/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='20';s.width='20'; set(gcf,'PaperType','A3')
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,comment,'.png'])
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,-imag(Q_vec(:,(ii)))/1e-4],'delimiter','\t','precision',8)
end

%% GR vs Q'

c=hsv(length(Nb_val));
for ii=1:length(Nb_val)
    figure(3);
    set(gcf,'visible',flagshow)
    plot(Qp_vec,-imag(Q_vec(:,(ii)))*machine.omega0,'color',c(ii,:),'linewidth',2);
    name=[scenario,'_','GR_vs_Qp_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)];
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,-imag(Q_vec(:,(ii)))/1e-4])
end
% ylim([0 1e-4])
xlim([-20 20])
grid on;
title(regexprep(['GR d',damp_title_str,'_plane ',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))
xlabel('Q''');
ylabel('Growth rate [s^{-1}]');

if flagsave
    name=[scenario,'_','GR_vs_Qp_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='20';s.width='20'; set(gcf,'PaperType','A3')
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,-imag(Q_vec(:,(ii)))*machine.omega0],'delimiter','\t','precision',8)
end

%% RT vs Q'

c=hsv(length(Nb_val));
for ii=1:length(Nb_val)
    figure(4);
    set(gcf,'visible',flagshow)
    plot(Qp_vec,1./(-imag(Q_vec(:,(ii)))*machine.omega0),'color',c(ii,:),'linewidth',2);
    name=[scenario,'_','RT_vs_Qp_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)];
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,1./(-imag(Q_vec)*machine.omega0)])
end
ylim([0 100])
xlim([-20 20])
grid on;
title(regexprep(['RT d',damp_title_str,'_plane ',plane,'_M',M,sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))
xlabel('Q''');
ylabel('\tau [s]');

if flagsave
    name=[scenario,'_','RT_vs_Qp_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='20';s.width='20'; set(gcf,'PaperType','A3')
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,1./(-imag(Q_vec(:,(ii)))*machine.omega0)],'delimiter','\t','precision',8)
end

%% ReQ vs Q'

c=hsv(length(Nb_val));
for ii=1:length(Nb_val)
    figure(5);
    set(gcf,'visible',flagshow)
    plot(Qp_vec,real(Q_vec(:,(ii)))./machine.Qs,'color',c(ii,:),'linewidth',2);
end
ylim([-5 5])
xlim([-20 20])
set(gca,'ytick',-15:15);
l=hline(-15:15,'-'); set(l,'color',[.5,.5,.5]);
title(regexprep(['ReQ d',damp_title_str,'_plane ',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))
xlabel('Q''');
ylabel('Re(\DeltaQ)/Q_s');

if flagsave
    name=[scenario,'_','ReQ_vs_Qp_d',damp,'_plane',plane,'_M',M,'_Nb',num2str(Nb_val((ii))/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='20';s.width='20'; set(gcf,'PaperType','A3')
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
    dlmwrite([ResultDir,name,comment,'.txt'],[Qp_vec,real(Q_vec(:,(ii)))./machine.Qs],'delimiter','\t','precision',8)
end

%% IE
close all
flagcheck=0;
epsmax=5; % limit for plot
Nmax=5; % in 1e11 ppb max intensity

% Octupoles
if strncmp('HLLHC',regexprep(scenario,'-',''),5)
    disp('HLLHC octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/HLLHCV1.1/';
elseif  strncmp('LHC',scenario,3) 
    disp('LHC octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2016/LHC-squeeze40cm/';
elseif  strncmp('LHC_inj',scenario,7) 
    disp('LHC injection octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/LHC-inj/';
end

current_octF=1; % max oct current
disp(['Max current @ ',num2str(current_octF),'A'])

% distribution
distribution='gaussian';
notesign='opposite';

% general machine parameters
if strncmp(scenario,'LHC_inj',7)
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,450e9,'Nominal LHC');
elseif strfind(scenario,'6.5TeV')
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,6500e9,'Nominal LHC');
    machine.M=M;    
elseif strfind(scenario,'2012')
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,4000e9,'Nominal LHC');
elseif ~isempty([strfind(scenario,'HLLHC'),strfind(scenario,'HL-LHC')])
    [~,~,~,E0]=particle_param('proton');
    machine=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
    disp(['HLLHC Energy=',machine.Estr])
else
   error('Unknown machine!!!'); 
end

disp([scenario,' @ ',machine.Estr]);
% SD for given max octupole current and emittance=epsnorm

if strcmp(notesign,'opposite');
    disp('Octupole with opposite sign');
    current_octD=-current_octF;
elseif strcmp(notesign,'same');
    disp('Octupole with same sign');
    current_octD=current_octF;
end
epsnormx=epsnorm;epsnormy=epsnorm;
[a,~]=octupole(OctDir); 

stab_plus=stab_diagramLHC_diffFD(machine.gamma,epsnormx,epsnormy,plane, a,current_octF,current_octD,distribution);
stab_minus=stab_diagramLHC_diffFD(machine.gamma,epsnormx,epsnormy,plane, a,-current_octF,-current_octD,distribution);
stab_plus_mat=stab_plus(:,1)+1i*stab_plus(:,2);
stab_minus_mat=stab_minus(:,1)+1i*stab_minus(:,2);
    
% Finding stabilizing emittance for each intensity
stab_oct_plus_vec=[];
stab_oct_minus_vec=[];

for Nb_plot=Nb_val;
    
    ind=find(Qp_vec==Q_plot); % select chosen chromaticty
    disp(['Nb= ',num2str(Nb_plot/1e11),'e11 at Qp=',num2str(Qp_vec(ind))]);
    Qie=Q_vec(ind,Nb_val==Nb_plot); % select intensity at that chromaticity
    Qie_re=real(Qie)-round(real(Qie)/machine.Qs)*machine.Qs;
    Qie_im=imag(Qie);
    Qie=Qie_re-1i*Qie_im; % takes conjugate
    
    if isnan(real(Qie))
        stab_oct_plus_vec=[stab_oct_plus_vec,nan];
        stab_oct_minus_vec=[stab_oct_minus_vec,nan];
    else
        x=real(stab_plus_mat);
        y=imag(stab_plus_mat);
        N=length(x);
        x_int_plus=min(x):(max(x)-min(x))/(1000*N):max(x);
        y_int_plus=interp1(x,y,x_int_plus,'linear');
        GCVk = @(k) min(((k*x_int_plus-real(Qie)).^2+(k*y_int_plus-imag(Qie)).^2));
        k_plus = fminbnd(GCVk,0,60);
        stab_oct_plus_vec=[stab_oct_plus_vec,k_plus];


        x=real(stab_minus_mat);
        y=imag(stab_minus_mat);
        N=length(x);
        x_int_minus=min(x):(max(x)-min(x))/(1000*N):max(x);
        y_int_minus=interp1(x,y,x_int_minus,'linear');
        GCVk = @(k) min(((k*x_int_minus-real(Qie)).^2+(k*y_int_minus-imag(Qie)).^2));
        k_minus = fminbnd(GCVk,0,60);
        stab_oct_minus_vec=[stab_oct_minus_vec,k_minus];
    end
    if flagcheck==1
        
        set(gcf,'visible',flagshow)
        plot(k_minus*real(stab_minus_mat),k_minus*imag(stab_minus_mat),'-k'); hold on;
        plot(k_plus*real(stab_plus_mat),k_plus*imag(stab_plus_mat),'-r'); hold on;
        plot(real(Qie),imag(Qie),'dk');
    end
end

figure(6)
set(gcf,'visible',flagshow)
h1=plot(stab_oct_plus_vec*(epsnorm*1e6),Nb_val/1e11,'dr','linewidth',2); hold on;
h2=plot(stab_oct_minus_vec*(epsnorm*1e6),Nb_val/1e11,'dk','linewidth',2);
p=polyfit([0,stab_oct_plus_vec*epsnorm*1e6],[0,Nb_val/1e11],1);
plot(0:epsmax,polyval(p,0:epsmax),'--r','linewidth',1);
p=polyfit([0,stab_oct_minus_vec*epsnorm*1e6],[0,Nb_val/1e11],1);
plot(0:epsmax,polyval(p,0:epsmax),'--k','linewidth',1);
ylim([0 Nmax])
% xlim([0 epsmax])
grid on;
xlabel('\epsilon_n [\mum]');
ylabel('N_{b} [1e11 ppb]');
legend([h1,h2],'I_{oct}>0','I_{oct}<0','location','northwest'); legend boxoff
title(regexprep(['IE_Qp',num2str(Q_plot),'_d',damp_title_str,'_plane_',plane,'_M',M,'_',distribution,'_Ioct=',num2str(current_octF),'A',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' '))

nametxt=[scenario,'_IE_Nb',num2str(Nb_val),'_Qp',num2str(Q_plot),'_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_Ioct',num2str(current_octF),sprintf('_sigmaz_%.3fm',machine.sigmaz),''];
dlmwrite([ResultDir,nametxt,comment,'_oct_positive.txt'],[stab_oct_plus_vec'*epsnorm,Nb_val']);
dlmwrite([ResultDir,nametxt,comment,'_oct_negative.txt'],[stab_oct_minus_vec'*epsnorm,Nb_val']);

if flagsave
    name=[scenario,'_IE_Qp',num2str(Q_plot),'_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_Ioct',num2str(current_octF),sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12'; set(gcf,'PaperType','A3'); 
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
end

% % 
%% SD
% close all

DataDir=[mainDir,scenario,'/'];
if strncmp('HLLHC',regexprep(scenario,'-',''),5)
    disp('HLLHC octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/HLLHCV1.1/';
elseif  strncmp('LHC',scenario,3) 
    disp('LHC octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2016/LHC-squeeze40cm/';
elseif  strncmp('LHC_inj',scenario,7) 
    disp('LHC injection octupoles')
    OctDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/Getting_LHC_beta_functions/2015/LHC-inj/';
else
    error('Undefined machine!')
end

current_octF=1;
distribution='gaussian';
notesign='opposite';

if strncmp(scenario,'LHC_inj',7)
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,450e9,'Nominal LHC');
elseif ~isempty(strfind(scenario,'2012'))
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,4000e9,'Nominal LHC');
elseif ~isempty(strfind(scenario,'ft'))
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,6500e9,'Nominal LHC');
elseif ~isempty(strfind(scenario,'40cm')) || ~isempty( strfind(scenario,'50cm')) || ~isempty(strfind(scenario,'80cm'))
    [~,~,~,E0]=particle_param('proton');
    machine=LHC_param(E0,6500e9,'Nominal LHC');
elseif ~isempty(strfind(regexprep(scenario,'-',''),'HLLHC'))
    [~,~,~,E0]=particle_param('proton');
    machine=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
    disp(['Energy=',machine.Estr])
else
    warning('No machine')
end

Qoct_vec=[]; Qp_vec=[];

for Nb=Nb_val
    if ~mod(Nb,1e11)
       namefile2=regexprep(namefile,'NPAR',[sprintf('%.0d',Nb/1e11),'e11']);
    else
       namefile2=regexprep(namefile,'NPAR',[regexprep(sprintf('%.1f',Nb/1e11),'\.','p'),'e11']);
    end
    L=dlmread([DataDir,namefile2,'_real.dat'],'',1,0);
    Qp_vec=L(:,1);
    Q=L(:,2);
    L=dlmread([DataDir,namefile2,'_imag.dat'],'',1,0);
    Q=Q+1i*L(:,2);
    
    if sum(isnan(Q))>0
        sumnan=sum(isnan(Q));
        disp([num2str(sumnan),'nan in Q data. Interpolating around.'])
        ind=find(isnan(Q)==1);
        
        if numel(ind)==1
            Q(ind)=mean([Q(ind+1),Q(ind-1)]);
            disp('1 nan found and interpolated around.')
        else
            Q(ind)=nan;
            disp('more than 1 nan found.')
        end
    end
    Qoct_vec=[Qoct_vec,Q];
end

if length(Nb_val)==1
    Nb=Nb_val;
else
    error('Must specify one value for Nb_val in the range of Nb_val')
end

Q_vec=Qoct_vec;
Q_vec=conj(Q_vec);
Q_vec=Q_vec-round(real(Q_vec)/machine.Qs)*machine.Qs; % refer around Qs


disp(['Ioct=',num2str(current_octF),'/',num2str(max(current_octF))])
if strcmp(notesign,'opposite');
    current_octD=-current_octF;
elseif strcmp(notesign,'same');
    current_octD=current_octF;
end
epsnormx=epsnorm;epsnormy=epsnorm;
[a,qsec]=octupole(OctDir); 

stab_plus=stab_diagramLHC_diffFD(machine.gamma,epsnormx,epsnormy,plane, a,current_octF,current_octD,distribution);
stab_minus=stab_diagramLHC_diffFD(machine.gamma,epsnormx,epsnormy,plane, a,-current_octF,-current_octD,distribution);
stab_plus_mat=stab_plus(:,1)+1i*stab_plus(:,2);
stab_minus_mat=stab_minus(:,1)+1i*stab_minus(:,2);


stab_oct_plus_vec=[];
stab_oct_minus_vec=[];

for ii=25%1:length(Q_vec)
    disp(['Qp=',num2str(Qp_vec(ii))])
    exit_status=0;
    close all
    while exit_status~=1
        if isnan(real(Q_vec(ii)))
            stab_oct_plus_vec(ii)=nan;
            stab_oct_minus_vec(ii)=nan;
            exit_status=1;
        else
            x=real(stab_plus_mat);
            y=imag(stab_plus_mat);
            N=length(x);
            x_int_plus=min(x):(max(x)-min(x))/(1000*N):max(x);
            y_int_plus=interp1(x,y,x_int_plus,'linear');
            GCVk = @(k) min(((k*x_int_plus-real(Q_vec(ii))).^2+(k*y_int_plus-imag(Q_vec(ii))).^2));
            k_plus = fminbnd(GCVk,0,6000);
            stab_oct_plus_vec(ii)=k_plus;


            x=real(stab_minus_mat);
            y=imag(stab_minus_mat);
            N=length(x);
            x_int_minus=min(x):(max(x)-min(x))/(1000*N):max(x);
            y_int_minus=interp1(x,y,x_int_minus,'linear');
            GCVk = @(k) min(((k*x_int_minus-real(Q_vec(ii))).^2+(k*y_int_minus-imag(Q_vec(ii))).^2));
            k_minus = fminbnd(GCVk,0,6000);
            stab_oct_minus_vec(ii)=k_minus;

            disp('checking mum in SD')
            figure(7)
            set(gcf,'visible',flagshow)
            plot(k_plus*x_int_plus,k_plus*y_int_plus,'-r'); hold on;
            plot(k_minus*x_int_minus,k_minus*y_int_minus,'-k'); 
            plot([real(Q_vec(ii))],[imag(Q_vec(ii))],'ok','markerfacecolor','r'); 
            legend([distribution,' I_{oct}>0'],[distribution,' I_{oct}<0'],'M.u.m.')
            xlabel('Re(\DeltaQ)')
            ylabel('Im(\DeltaQ)')
            xlim([-4e-4 4e-4])
            title([regexprep(scenario,'_',' '),' Q''=',num2str(Qp_vec(ii))])


            reQ_all=(real(Q_all_vec(ii,:))-round(real(Q_all_vec(ii,:))./machine.Qs)*machine.Qs);
            imQ_all=imag(Q_all_vec(ii,:));
            
            delta_im_vec=[];index_mum=[];
            for kk=1:length(reQ_all)
                delta_im=interp1(k_plus*x_int_plus,k_plus*y_int_plus,reQ_all(kk))-(-imQ_all(kk));
                delta_im_vec=[delta_im_vec,delta_im];
                index_mum=[index_mum,kk];    
            end

            [min_delta_im,ind_min]=min(delta_im_vec);
            if min_delta_im<-1e-6
                
                warning('The m.u.m. has lower risetime but higher frequency shift: new iteration on the most critical one.')
                new_Q=reQ_all(ind_min)-1i*imQ_all(ind_min);
                Q_vec(ii)=new_Q;
                exit_status=0;
            else
               exit_status=1;
            end
        end
% pause

    end
end

   
figure(8)
set(gcf,'visible',flagshow)
h1=plot(Qp_vec,stab_oct_plus_vec,'-r','linewidth',2); hold on;
h2=plot(Qp_vec,stab_oct_minus_vec,'-k','linewidth',2);
grid on;
xlabel('Q''');
ylabel('I_{oct} [A]');
legend([h1,h2],'I_{oct}>0','I_{oct}<0','location','northwest'); legend boxoff
title([{regexprep(scenario,'_',' ')},{regexprep(['SD_vs_Qp_d',damp_title_str,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm*1e6),'um_','Nb',num2str(Nb/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' ')}])

if strcmp(machine.Estr,'450GeV') && eval(M)==1
ylim([0 10])
elseif strcmp(machine.Estr,'450GeV') && eval(M)>1
ylim([0 10])
else
ylim([0 600])
end
xlim([-20 20])


nametxt=[scenario,'_SD_vs_Qp_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm*1e6),'um_','Nb',num2str(Nb/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)];
dlmwrite([ResultDir,nametxt,comment,'_oct_positive.txt'],[Qp_vec,stab_oct_plus_vec']);
dlmwrite([ResultDir,nametxt,comment,'_oct_negative.txt'],[Qp_vec,stab_oct_minus_vec']);

if flagsave
    name=[scenario,'_SD_vs_Qp_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm*1e6),'um_','Nb',num2str(Nb/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12'; set(gcf,'PaperType','A3'); 
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
end

figure(9)
set(gcf,'visible',flagshow)
h1=plot(Qp_vec,stab_oct_plus_vec*(Nb_scaled/epsnorm_scaled)/(Nb_val/epsnorm),'-r','linewidth',2); hold on;
h2=plot(Qp_vec,stab_oct_minus_vec*(Nb_scaled/epsnorm_scaled)/(Nb_val/epsnorm),'-k','linewidth',2);
grid on;
xlabel('Q''');
ylabel('I_{oct} [A]');
legend([h1,h2],'I_{oct}>0','I_{oct}<0','location','northwest'); legend boxoff
title([{regexprep(scenario,'_',' ')},{regexprep(['SD_vs_Qp_d',damp_title_str,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm_scaled*1e6),'um_','Nb',num2str(Nb_scaled/1e11),'e11',sprintf('_sigmaz_%.3fm',machine.sigmaz)],'_',' ')}])


if strcmp(machine.Estr,'450GeV') && eval(M)==1
ylim([0 10])
elseif strcmp(machine.Estr,'450GeV') && eval(M)>1
ylim([0 10])
else
ylim([0 600])
end
xlim([-20 20])


nametxt=[scenario,'_SD_vs_Qp_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm_scaled*1e6),'um_scaled_','Nb',num2str(Nb_scaled/1e11),'e11_scaled',sprintf('_sigmaz_%.3fm',machine.sigmaz)];
dlmwrite([ResultDir,nametxt,comment,'_oct_positive.txt'],[Qp_vec,stab_oct_plus_vec']);
dlmwrite([ResultDir,nametxt,comment,'_oct_negative.txt'],[Qp_vec,stab_oct_minus_vec']);

if flagsave
    name=[scenario,'_SD_vs_Qp_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_eps',num2str(epsnorm_scaled*1e6),'um_scaled_Nb',num2str(Nb_scaled/1e11),'e11_scaled',sprintf('_sigmaz_%.3fm',machine.sigmaz),comment];
    s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12'; set(gcf,'PaperType','A3'); 
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
end

end % plane
end % M
end % damp
end % Nb

%% Compare scenario
close all;
% addpath(genpath('/afs/cern.ch/user/n/nbiancac/scratch0/Matlab-scripts/'));
flagshow='on';
flagsave=1;


% % 2016 relaxed
% lista.scenario=[{'LHC_ft_6.5TeV_B1'},...
%     {'LHC_50cm_relaxed_6.5TeV_B1_2016_TCL_out'}];
% lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,length(lista.scenario));
% comment='overview_relaxed';
% lista.subscenario=repmat([{'SD_vs_Qp_d0_plane_y_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.090m_oct_positive'}],1,length(lista.scenario));
% lista.color=hsv(length(lista.scenario));
% replacestr='';withstr='';
% leg_pos='northwest';

% % 2015 vs 2016
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,4);
scenario='LHC_50cm_tight_6.5TeV_B1_2016_TCL_out'; % blength 0.112
lista.scenario=repmat([{scenario}],1,4);
comment=[scenario,'_'];
plane='y';
lista.subscenario=[...
    {['SD_vs_Qp_d0_plane_',plane,'_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.090m_oct_positive']},...
    {['SD_vs_Qp_d0p005_plane_',plane,'_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.090m_oct_positive']},...
    {['SD_vs_Qp_d0p01_plane_',plane,'_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.090m_oct_positive']},...
    {['SD_vs_Qp_d0p02_plane_',plane,'_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.090m_oct_positive']}];
lista.color=hsv(length(lista.scenario));
replacestr=regexprep(scenario,'_',' ');withstr='';
leg_pos='northwest';
clean_val=-7;

% After LS2 new coated IP7
% lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/Results/'}],1,4);
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/Results/';
% lista.scenario=[...,
% {'HL-LHC_15cm_7TeV_baseline_B1'},...    
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_5-TCSG'},...
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_5-TCSG'},...
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umTiN+MoC_5-TCSG'}];
% comment='afterLS2_';
% lista.subscenario=repmat([{'SD_vs_Qp_d0_plane_x_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.081m_oct_positive'}],1,4);
% lista.subscenario=[{'RT_vs_Qp_d0p02_planey_M1_Nb1.2e11_sigmaz_0.081m'},...    
%     {'RT_vs_Qp_d0p02_planey_M1_Nb1.2e11_sigmaz_0.081m'}];


% % 2015 injection
% lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,4);
% lista.scenario=repmat([{'LHC_inj_450GeV_B1_2015'},{'LHC_inj_TDI_hg3.8mm_450GeV_B1_2015'},{'LHC_inj_TDI_hg5.0mm_450GeV_B1_2015'},...
% {'LHC_inj_TDI_hg10.0mm_450GeV_B1_2015'}],1,1);
% comment=['injTDI_'];
% lista.subscenario=repmat([{'SD_vs_Qp_d0_plane_x_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.112m_oct_positive'}],1,4);
% lista.color=hsv(length(lista.scenario));
% replacestr='inj 450GeV';withstr='inj TDI open';
% 
% 2016 injection
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,2);
lista.scenario=repmat([{'LHC_inj_450GeV_B1_2016'},{'LHC_inj_TDI_hg3.8mm_450GeV_B1_2016'},...
],1,1);
comment=['injTDI_2016_'];
lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.112m_oct_positive'}],1,2);
lista.color=hsv(length(lista.scenario));
replacestr='inj 450GeV';withstr='inj TDI open';
clean_val=-15;

% 2016 injection failure
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,3);
lista.scenario=repmat([{'LHC_inj_450GeV_B1_2016'},{'LHC_inj_TDI_hg3.8mm_450GeV_B1_2016'},{'LHC_inj_TDI_hg3.8mm_noCu_450GeV_B1_2016'},...
],1,1);
comment=['injTDI_failure_2016_'];
lista.subscenario=repmat([{'SD_vs_Qp_d0_plane_y_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.112m_oct_positive'}],1,3);
lista.color=hsv(length(lista.scenario));
replacestr='inj 450GeV';withstr='inj TDI open';
clean_val=-15;

% % 
% % 2015 injection with TDI measured
% lista.DataDir=[repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,1),...
%     repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII_TDI_measured/Results/'}],1,2)];
% lista.scenario=([{'LHC_inj_450GeV_B1_2015'},...
%     {'LHC_inj_450GeV_B1_2015_TDI2_5.0mm'},...
% {'LHC_inj_450GeV_B1_2015_TDI8_5.0mm'}]);    
% comment=['injTDI_measured_'];
% % lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_y_M1_gaussian_eps2um_scaled_Nb1e11_scaled_sigmaz_0.112m_oct_positive'}],1,3);
% lista.subscenario=repmat([{'ReQ_vs_Qp_d0p02_planey_M1_Nb1.2e11_sigmaz_0.112m'}],1,3);
% lista.color=[[0 0 0];[0 0 1];[1 0 0]];
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII_TDI_measured/Results/';

% replacestr='inj 450GeV';withstr='inj TDI open';


% HLLHC and crabs
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/SepRate-60cm/Results/'}],1,4);
lista.scenario=repmat([{'HLLHC_60cm_7TeV_B1_2016'}],1,4);
comment=['HLLHCwithCC_zoomneg'];
lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_x_M1_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
    {'SD_vs_Qp_d0p02_plane_y_M1_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
     {'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
      {'SD_vs_Qp_d0p02_plane_y_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
      ],1,1);
lista.subscenario=repmat([{'RT_vs_Qp_d0p02_planex_M1_Nb2.2e11_sigmaz_0.081m'}
    {'RT_vs_Qp_d0p02_planey_M1_Nb2.2e11_sigmaz_0.081m'}
    {'RT_vs_Qp_d0p02_planex_M2748_Nb2.2e11_sigmaz_0.081m'}
    {'RT_vs_Qp_d0p02_planey_M2748_Nb2.2e11_sigmaz_0.081m'}
    ],1,1);
lista.color=hsv(length(lista.scenario));
replacestr='';withstr='';
clean_val=-15;


% 2016 injection
ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,4);
lista.scenario=[{'LHC_inj_450GeV_B1_2016'}
    {'LHC_inj_450GeV_B1_2016'}];
comment='MD_15042016';
lista.subscenario=repmat([{'RT_vs_Qp_d0_planex_M1_Nb1.2e11_sigmaz_0.112m'}
    {'RT_vs_Qp_d0_planey_M1_Nb1.2e11_sigmaz_0.112m'}
    ],1,1);
lista.color=hsv(length(lista.scenario));
replacestr='';withstr='';
clean_val=-15;

% HLLHC and crabs small scan
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/Results/'}, ...
    {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/Results/'}],1,1);
lista.scenario=repmat([{'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'}],1,2);
% lista.scenario=repmat([{'HL-LHC_15cm_7TeV_baseline_TCT5_B1'}],1,2);
comment=[''];
lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.1e11_sigmaz_0.081m_oct_negative'}
    {'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.1e11_sigmaz_0.081m_oct_negative'}
      ],1,1);
% lista.subscenario=repmat([{'RT_vs_Qp_d0p02_planex_M2748_Nb2.1e11_sigmaz_0.081m'},...
%      {'RT_vs_Qp_d0p02_planex_M2748_Nb2.1e11_sigmaz_0.081m'}
%         ],1,1);
lista.color=distinguishable_colors(length(lista.scenario));
replacestr='';withstr='';
clean_val=14;
% scenario='HL-LHC_15cm_7TeV_baseline_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
% scenario='HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1';

% HLLHC and crabs wide scan
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/Results/'}, ...
    {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/Results/'}],1,1);
lista.scenario=repmat([{'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},{'HLLHC_7TeV_DQW_20151001_IP1-IP5'}],1,1);
comment=['_forElias'];
lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
    {'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
      ],1,1);
lista.color=distinguishable_colors(length(lista.scenario));
replacestr='';withstr='';
clean_val=14;

mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/SepRate-60cm/';
scenario='HLLHC_60cm_7TeV_B1_2016';


% HLLHC and crabs vs betastar
lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/Results/'}, ...
    {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/SepRate-60cm/Results/'}],1,1);
lista.scenario=repmat([{'HLLHC_7TeV_DQW_20151001_IP1-IP5'},{'HLLHC_60cm_7TeV_B1_2016'}],1,1);
comment=['HL-LHC_15vs60cm'];
lista.subscenario=repmat([{'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
    {'SD_vs_Qp_d0p02_plane_x_M2748_gaussian_eps2.5um_Nb2.2e11_sigmaz_0.081m_oct_negative'}
      ],1,1);
lista.color=distinguishable_colors(length(lista.scenario));
replacestr='';withstr='';
clean_val=14;

% 2016 tight
% lista.scenario=[{'LHC_ft_6.5TeV_B1_2016'},...
%     {'LHC_50cm_tight_6.5TeV_B1_2016_TCL_out'},...
%     {'LHC_40cm_6.5TeV_B1_2016_TCL_out'}];
% lista.DataDir=repmat([{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/'}],1,length(lista.scenario));
% comment='overview_tight';
% lista.subscenario=repmat([{'RT_vs_Qp_d0p02_planex_M2748_Nb1.2e11_sigmaz_0.090m'}],1,length(lista.scenario));
% lista.color=hsv(length(lista.scenario));
% replacestr='';withstr='';
% leg_pos='northwest';
% clean_val=-20;



figure(1);
set(gcf,'visible',flagshow)
for kk=1:length(lista.scenario)
    L=dlmread([char(lista.DataDir(kk)),char(lista.scenario(kk)),'_',char(lista.subscenario(kk)),'.txt']);
%     ind=find(L(:,1)==clean_val);
%     L(ind,2)=mean([L(ind+1,2),L(ind-1,2)]);
    plot(L(:,1),L(:,2),'.-','linewidth',2,'color',lista.color(kk,:)); hold on;
end
hold off;

lista.subscenario=regexprep(lista.subscenario,'_vs_Qp','-vs-Qp');
lista.subscenario=regexprep(lista.subscenario,'sigmaz_','sigmaz-');
lista.subscenario=regexprep(lista.subscenario,'oct_','oct-');
lista.subscenario=regexprep(lista.subscenario,'plane_','plane-');

[lista.title,lista.legend]=get_title_legend(lista.scenario,lista.subscenario);

disp('convertig damper gain to turns')
for damp_name=[{'d0p005'},{'d0p01'},{'d0p02'},{'d0'}]
    damp_turn=1./eval(char(regexprep(damp_name,[{'d'},{'p'}],[{''},{'.'}])));
    lista.title=regexprep(lista.title,damp_name,['d=',num2str(damp_turn),' turns']);
    lista.legend=regexprep(lista.legend,damp_name,['d=',num2str(damp_turn),' turns']);
end

lista.legend=regexprep(lista.legend,replacestr,withstr);
legend(lista.legend,'location',leg_pos);
grid on

title(lista.title)

set(gcf,'position',[  287   105   879   547])


if strcmp(lista.subscenario{1}(1:8),'SD-vs-Qp')
    if max(L(:,2))>100
        ylim([0 300])
    else
        ylim([0 300])
    end
    xlim([-20 20 ])
    labelY='I_{oct} [A]';
    labelX='Q''';
elseif strcmp(lista.subscenario{1}(1:8),'RT-vs-Qp')
        if max(L(:,2))>50
%         ylim([0 1])
    else
%         ylim([0 10])
    end
%     xlim([-20 -2 ])
    labelY='Rise time [s]';
    labelX='Q''';
end

xlabel(labelX)
ylabel(labelY)

if flagsave
    
    name=[comment, regexprep(lista.title,' ','_')];
    s=hgexport('readstyle','PRSTAB'); s.Width='auto';set(gcf,'PaperType','A3')
    
    hgexport(gcf,'',s,'applystyle',true);
    
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    disp([ResultDir,name,'.png'])
end

%% Mum displacement

mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/';
ResultDir=[mainDir,'Results/']; system(['mkdir -p ',ResultDir]);
beams=1;
indQp=1;

plane='x';
scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
mum=dlmread([mainDir,scenario,'/','data_vs_Qp_all_HLLHC_7000GeV',scenario,'_2748b_d0p02_Nb2p1e11_converged_',plane,'_real.dat'],'',1,0);
Qp=mum(:,1);
Qre=mum(indQp,2:end);
m=round((Qre)/machine.Qs);
Qre=Qre-m*machine.Qs;
mum=dlmread([mainDir,scenario,'/','data_vs_Qp_all_HLLHC_7000GeV',scenario,'_2748b_d0p02_Nb2p1e11_converged_',plane,'_imag.dat'],'',1,0);
Qim=mum(indQp,2:end);

figure(3)
plot((Qre),-(Qim),'ok'); hold on;

mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/';
scenario='HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1';
mum=dlmread([mainDir,scenario,'/','data_vs_Qp_all_HLLHC_7000GeV',scenario,'_2748b_d0p02_Nb2p1e11_converged_',plane,'_real.dat'],'',1,0);
Qp=mum(:,1);
Qre=mum(indQp,2:end);
m=round((Qre)/machine.Qs);
Qre=Qre-m*machine.Qs;
mum=dlmread([mainDir,scenario,'/','data_vs_Qp_all_HLLHC_7000GeV',scenario,'_2748b_d0p02_Nb2p1e11_converged_',plane,'_imag.dat'],'',1,0);
Qim=mum(indQp,2:end);

figure(3)
plot((Qre),-(Qim),'or')

%% Intemit scenario plot
close all
flagsave=0;
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/';
mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/';
% mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/';
ResultDir=[mainDir,'Results/']; system(['mkdir -p ',ResultDir]);
collset='IP7-coatings';
beams=1;
polarity='neg';
damp_name='d0p02';
M=2748;
Qpmin=14; Qpmax=16;


if strcmp(collset,'5-TCSG');
    scenario_scan=[{'HL-LHC_15cm_7TeV_baseline_B1'},{'HL-LHC_15cm_7TeV_baseline_B1_5umTiN+MoC_5-TCSG'},{'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_5-TCSG'},{'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_5-TCSG'}];
    leg_str=[{'All TCSG.7 in CFC'},{'5 TCSG.7 in 5\mu TiN+MoC'},{'5 TCSG.7 in 5\mu Mo+MoC'},{'5 TCSG.7 in 5\mu Cu+MoC'}];
elseif strcmp(collset,'IP7');
    scenario_scan=[{'HL-LHC_15cm_7TeV_baseline_B1'},{'HL-LHC_15cm_7TeV_baseline_B1_5umTiN+MoC_IP7'},{'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_IP7'},{'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_IP7'}];
    leg_str=[{'All TCSG.7 in CFC'},{'All TCSG.7 in 5\mu TiN+MoC'},{'All TCSG.7 in 5\mu Mo+MoC'},{'All TCSG.7 in 5\mu Cu+MoC'}];
elseif strcmp(collset,'TCT5')
    scenario_scan=[{'HL-LHC_15cm_7TeV_baseline_TCT5_B1'}];
    leg_str=[{'baseline TCT5'}];
elseif strcmp(collset,'IP7-coatings')
    scenario_scan=[    
    {'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_baseline_TCT5_B1'}    ];
    leg_str=[{'TCSG.7 with 5\mum Mo coating on Mo-Gr'},{'TCSG.7 with 5\mum TiB2 coating on Mo-Gr'},{'TCSG.7 with 5\mum TiN coating on Mo-Gr'},{'All TCSGs in CFC'}];
elseif strcmp(collset,'IP7-coatings-old_WP')
    scenario_scan=[    
    {'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1'},
    {'HL-LHC_15cm_7TeV_baseline_TCT5_B1'}    ];
    leg_str=[{'TCSG.7 with 5\mum Mo coating on Mo-Gr'},{'TCSG.7 with 5\mum TiB2 coating on Mo-Gr'},{'TCSG.7 with 5\mum TiN coating on Mo-Gr'},{'All TCSGs in CFC'}];

else
    scenario_scan1=[{'HL-LHC_15cm_7TeV_baseline_B1'},{'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_IP7'},{'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_IP7'}];
    leg_str1=[{'All TCSG.7 in CFC'},{'All TCSG.7 in 5\mu Mo+MoC'},{'All TCSG.7 in 5\mu Cu+MoC'}];
    scenario_scan2=[{'HL-LHC_15cm_7TeV_baseline_B1'},{'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_5-TCSG'},{'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_5-TCSG'}];
    leg_str2=[{'All TCSG.7 in CFC'},{'5 TCSG.7 in 5\mu Mo+MoC'},{'5 TCSG.7 in 5\mu Cu+MoC'}];
    scenario_scan=[scenario_scan1,scenario_scan2];
    leg_str=[leg_str1,leg_str2];
end

leg_vec=[]; h_vec=[];
col_vec=distinguishable_colors(length(scenario_scan));
Qpmean=Qpmin/2+Qpmax/2;
Qperr=abs(Qpmin/2-Qpmax/2);
damp_turn=1./eval(char(regexprep(damp_name,[{'d'},{'p'}],[{''},{'.'}])));

for ii=1:length(scenario_scan)
    L=dlmread([mainDir,'/',char(scenario_scan(ii)),'/data_int_vs_emit_LHC_7000GeV',char(scenario_scan(ii)),'_',num2str(M),'b_',damp_name,'_Qp',num2str(Qpmin),'_',num2str(Qpmax),'_',polarity,'_oct_converged.dat'],'\t',1,0);
    eps_vec=L(:,1);
    Nb_vec=L(:,2);
    figure(23)
    h1=plot([eps_vec],[Nb_vec/1e11],'x-','color',col_vec(ii,:),'linewidth',2); hold on;
    h_vec=[h_vec,h1];
    leg_vec=[leg_vec,regexprep((scenario_scan(ii)),[{'baseline'},{'_'}],[{''},{' '}])];
end
xlim([0 5])
ylim([0 4])
grid on
hold off
xlabel(['\epsilon_n [mm mrad]'])
ylabel(['N_b [10^{11} ppb]'])
hplot1=legend(h_vec,leg_str,'location','southeast'); 
% hplot1=legend('TCSG.7 with 5\mum Mo coating on Mo-Gr','TCSG.7 with 5\mum TiB2 coating on Mo-Gr','TCSG.7 with 5\mum TiN coating on Mo-Gr','All TCSGs in CFC')
legend boxoff

 if strcmp(polarity,'neg')
    title(['M=',num2str(M),', d=',num2str(damp_turn),' turns, Q''=',num2str(Qpmean),'\pm',num2str(Qperr),', oct.sign: negative'])
 else
      title(['M=',num2str(M),', d=',num2str(damp_turn),' turns, Q''=',num2str(Qpmean),'\pm',num2str(Qperr),', oct.sign: positive'])
 end
s=hgexport('readstyle','PRSTAB');s.FixedFontSize='10';
hgexport(gcf,'',s,'applystyle',true);

if beams
% beams
hold on;
[~,~,clight,E0]=particle_param('proton');
HLLHC1=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
HLLHC2=HLLHC_param(E0,7000e9,'HL-LHC BCMS');
HLLHC3=HLLHC_param(E0,7000e9,'HL-LHC 8b+4e');
% figure
colbeam=['ok','xk','+k','dc'];
hb1=plot(HLLHC1.en,HLLHC1.Nb/1e11,'ok','markersize',6,'markerfacecolor','k'); hold on
hb2=plot(HLLHC2.en,HLLHC2.Nb/1e11,'xb','markersize',10,'markerfacecolor','b');
hb3=plot(HLLHC3.en,HLLHC3.Nb/1e11,'or','markersize',6,'markerfacecolor','r'); hold off

new_handle = copyobj(hplot1,gcf);
legend([hb1,hb2,hb3], [{'25ns'},{'BCMS'},{'8b+4e'}], 'Location','northwest'); legend boxoff;
addcomment='_beams';
%
else
    addcomment='_nobeams';
end


s=hgexport('readstyle','PRSTAB');s.FixedFontSize='10';
hgexport(gcf,'',s,'applystyle',true);
name=['HLLHC_baseline_TCT5_w-wo_scaling2012_oct_',polarity];


saveas(gcf, [ResultDir,name,'.fig'],'fig');
hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
disp([ResultDir,name,'.png'])

%% Intemit no scaling plot
flagsave=0;
flagshow='off';


mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/';
mainDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/';

scenario_scan=[
{'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},...
{'HL-LHC_15cm_7TeV_5umTiB2+MoC_IP7_TCT5_B1'},...
{'HL-LHC_15cm_7TeV_5umTiN+MoC_IP7_TCT5_B1'},...
{'HL-LHC_15cm_7TeV_baseline_TCT5_B1'}    ];
leg_str=[{'TCSG.7 with 5\mum Mo coating on Mo-Gr'},{'TCSG.7 with 5\mum TiB2 coating on Mo-Gr'},{'TCSG.7 with 5\mum TiN coating on Mo-Gr'},{'All TCSGs in CFC'}];

ResultDir=[mainDir,'Results/']; system(['mkdir -p ',ResultDir]);
% DataDir=[mainDir,scenario,'/'];
current_octF=550;
distribution='gaussian';
plane='x';
damp='0p02';
M='2748';

signoct='negative';
col_vec=distinguishable_colors(length(scenario_scan));



for ii=1:length(scenario_scan)

    scenario=char(scenario_scan(ii));
    int_vec=[];emit_vec=[];
    for Q_plot=[14:16]
        int_qp_vec=[]; emit_qp_vec=[];
        for Nb_val=[1e10, 1.1e11, 2.1e11, 3.1e11, 4.1e11];
            nametxt=[scenario,'_IE_Nb',num2str(Nb_val),'_Qp',num2str(Q_plot),'_d',damp,'_plane_',plane,'_M',M,'_',distribution,'_Ioct',num2str(current_octF),sprintf('_sigmaz_%.3fm',machine.sigmaz),'','_oct_',signoct,'.txt'];
            
            L=dlmread([ResultDir,nametxt]);
            disp([ResultDir,nametxt])
            int_qp_vec=[int_qp_vec,L(2)];
            emit_qp_vec=[emit_qp_vec,L(1)];
        end    
    
        int_vec=[int_vec;int_qp_vec];
        emit_vec=[emit_vec;emit_qp_vec];
    end
    
    int_vec=mean(int_vec,1);
    emit_vec=mean(emit_vec,1);
    figure(12)
    plot(emit_vec*1e6,int_vec/1e11,'x-','color',col_vec(ii,:),'linewidth',2); hold on;
    xlim([0 5])
    ylim([0 4])
    
    xlabel(['\epsilon_n [mm mrad]'])
    ylabel(['N_b [10^{11} ppb]'])
end
    
hplot1=legend(leg_str,'location','southeast'); 

[~,~,clight,E0]=particle_param('proton');
HLLHC1=HLLHC_param(E0,7000e9,'HL-LHC 25ns');
HLLHC2=HLLHC_param(E0,7000e9,'HL-LHC BCMS');
HLLHC3=HLLHC_param(E0,7000e9,'HL-LHC 8b+4e');
% figure
colbeam=['ok','xk','+k','dc'];
hb1=plot(HLLHC1.en,HLLHC1.Nb/1e11,'ok','markersize',6,'markerfacecolor','k'); hold on
hb2=plot(HLLHC2.en,HLLHC2.Nb/1e11,'xb','markersize',10,'markerfacecolor','b');
hb3=plot(HLLHC3.en,HLLHC3.Nb/1e11,'or','markersize',6,'markerfacecolor','r'); hold off

new_handle = copyobj(hplot1,gcf);
legend([hb1,hb2,hb3], [{'25ns'},{'BCMS'},{'8b+4e'}], 'Location','northeast'); legend boxoff;

if strcmp(polarity,'neg')
    title(['M=',num2str(M),', d=',num2str(damp_turn),' turns, Q''=',num2str(Qpmean),'\pm',num2str(Qperr),', oct.sign: negative'])
 else
      title(['M=',num2str(M),', d=',num2str(damp_turn),' turns, Q''=',num2str(Qpmean),'\pm',num2str(Qperr),', oct.sign: positive'])
end
grid on;

s=hgexport('readstyle','PRSTAB');s.FixedFontSize='10';
hgexport(gcf,'',s,'applystyle',true);
name=['HLLHC_baseline_TCT5_no_scaling2012_oct_',polarity];


saveas(gcf, [ResultDir,name,'.fig'],'fig');
hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
disp([ResultDir,name,'.png'])