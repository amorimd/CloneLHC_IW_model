clear all;
close all;


addpath(genpath('/afs/cern.ch/user/n/nbiancac/scratch0/Matlab-scripts/'));
% addpath(genpath('/home/nick/HDD/Work/Matlab-scripts'));
%%
[~,~,~,E0]=particle_param('proton');
IW2Dir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/IRIS/ImpedanceWake2D/';
CollDir='/afs/cern.ch/user/n/nbiancac/ln_delphi/PYTHON_codes_and_scripts/LHC_impedance_and_scripts/Coll_settings/';

flagsave=0;
flagshow='on';

% machine=LHC_param(E0,450e9,'Nominal LHC');
% DataDir=[ {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},...
% {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},...
%     ];
% name=[{'LHC_inj_450GeV_B1'},{'LHC_inj_TDI_hg5.7mm_450GeV_B1'},...
%     ];
% commentsave='LHC_inj_2015';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)
% plane=[{'y'},{'y'}];


% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/'}];
% name=[{'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},...
%       ];
% commentsave='baseline_TDR';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/baseline_TDR/Results/';
% mkdir(ResultDir)
% plane=[{''}];

% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'}];
% name=[{'HL-LHC_15cm_7TeV_baseline_TCT5_B1'},...
%       ];
% commentsave='baseline_CFC';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/Results/';
% mkdir(ResultDir)
% plane=[{'z'}];


% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'}];
% name=[
%     {'LHC_ft_6.5TeV_B1'}
%       {'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},...
%       ];
% commentsave='LHC-vs-HLLHC_Mo_IP7';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/Results/';
% mkdir(ResultDir)
% plane=[{'z'},{'z'}];

machine=LHC_param(E0,6.5e12,'Nominal LHC');
DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,3);
name=[{'LHC_ft_6.5TeV_B1_2016'},{'LHC_50cm_tight_6.5TeV_B1_2016_TCL_out'},{'LHC_40cm_6.5TeV_B1_2016_TCL_out'}];
commentsave='overview_tight';
ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
mkdir(ResultDir)
plane=repmat({'y'},1,3);
typeimp=repmat({'dip'},1,3);

% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,1);
% name=[{'LHC_ft_6.5TeV_B1_2016'}];
% commentsave='ft';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)
% plane=repmat({'y'},1,1);
% typeimp=repmat({'dip'},1,1);

% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,2);
% name=[{'LHC_ft_6.5TeV_B1_2015'},{'LHC_50cm_relaxed_6.5TeV_B1_2016_TCL_out'}];
% commentsave='overview_relaxed';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)
% plane=repmat({'x'},1,2);
% typeimp=repmat({'dip'},1,2);

% 
% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/'},1,1);
% name=[...,
%   {'HL-LHC_15cm_7TeV_baseline_B1'}];
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umCu+MoC_5-TCSG'},...
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umMo+MoC_5-TCSG'},...
%     {'HL-LHC_15cm_7TeV_baseline_B1_5umTiN+MoC_5-TCSG'}];
% commentsave='postLS2';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/Results/';
% mkdir(ResultDir)
% plane=repmat({'y'},1,4);
% typeimp=repmat({'dip'},1,4);

% bug
% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/'},{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'}];
% name=[...,
%   {'LHC_60cm_4TeV_2012_B1'},{'LHC_60cm_4TeV_2012_B1'}];
% commentsave='postLS2';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/Results/';
% mkdir(ResultDir)
% plane=repmat({'y'},1,2);
% typeimp=repmat({'dip'},1,2);


% % HLLHC 15cm vs LHC 2016 40cm
% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/'}];
% name=[{'LHC_40cm_6.5TeV_B1_2016_TCL_out'},{'HL-LHC_15cm_7TeV_baseline_B1'}];
% commentsave='LHC40cm_vs_HLLHC15cm';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/postLS2/Results/';
% mkdir(ResultDir)
% plane=repmat({'y'},1,2);
% typeimp=repmat({'dip'},1,2);


% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,4);
% 
% 
% commentsave='afterLS2';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)
% plane=repmat({'x'},1,4);
% typeimp=repmat({'dip'},1,4);

machine=LHC_param(E0,6.5e12,'Nominal LHC');
DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,2);
name=repmat({'LHC_ft_6.5TeV_B1_2016'},1,2);
commentsave='LHC_ft-x_vs_y';
ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
mkdir(ResultDir)
plane=[{'y'},{'x'}];
typeimp=repmat({'dip'},1,2);

% machine=LHC_param(E0,450e9,'Nominal LHC');
% DataDir=repmat({'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},1,2);
% name=[{'LHC_inj_450GeV_B1_2016'},{'LHC_inj_TDI_hg3.8mm_450GeV_B1_2016'}];
% commentsave='LHC_inj_TDI-3.8mm_2016';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/Results/';
% mkdir(ResultDir)
% plane=[{'y'},{'y'}];
% typeimp=repmat({'dip'},1,2);

% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD/'}];
% name=[
%     {'LHC_ft_6.5TeV_B1'},{'LHC_ft_6.5TeV_B1_4290_TCSG_IP7_6.5s'},...
%       ];
% commentsave='LHC_MD_4290';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD/Results/';
% mkdir(ResultDir)
% plane=[{'y'},{'y'}];
% typeimp=[{'dip'},{'dip'}];

% 
% machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/RunII/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%     
%     ];
%  name=[{'LHC_ft_6.5TeV_B1'},...
%       {'HL-LHC_15cm_7TeV_baseline_TCT5_B1'},...
%       
%       ];
% commentsave='HLLHC_vs_LHC';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/Results/';
% mkdir(ResultDir)
% plane=[{'y'},{'y'}];
% typeimp=[{'dip'},{'dip'}];


% machine=HLLHC_param(E0,7e12,'Nominal LHC');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'}];
% name=[
%       {'HL-LHC_15cm_7TeV_baseline_B1'},...
%       {'HL-LHC_15cm_7TeV_MoC_B1'},...
%       {'HL-LHC_15cm_7TeV_Mo_B1'},...
%       {'HL-LHC_15cm_7TeV_5umMo+MoC_B1'},...
%       ];
% commentsave='Mo_baseline_and_5um_coat';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/Results/';
% mkdir(ResultDir)

% machine=HLLHC_param(E0,7e12,'Nominal LHC');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%       {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/'}];
% name=[
%       {'HL-LHC_15cm_7TeV_baseline_B1'},...
%       {'HL-LHC_15cm_7TeV_MoC_B1'},...
%       {'HL-LHC_15cm_7TeV_Mo_B1'},...
%       ];
% commentsave='baseline-Mo-MoC';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/HLLHC_Mo-MoC-CFC_scenario/Results/';
% mkdir(ResultDir)

% machine=LHC_param(E0,6.5e12,'Nominal LHC');
% DataDir=[{'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD_4290/'},...
%     {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD_4290/'},...
% ];
% name=[
% {'LHC_ft_6.5TeV_B1_4290_TCSG_IP7_6.5s'},...
% {'LHC_ft_6.5TeV_B1_4291_TCSG_IP7_20s'},...      
%       ];
% plane=[{'x'},{'x'}];
% commentsave='MD_4291';
% ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/LHC/MD_4290/Results/';
% mkdir(ResultDir)


machine=HLLHC_param(E0,7e12,'HL-LHC 25ns');
DataDir=[    {'/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings_DQW-IP15/'}];
name=[
{'HL-LHC_15cm_7TeV_5umMo+MoC_IP7_TCT5_B1'},... 
            ];
commentsave='';
ResultDir='/afs/cern.ch/user/n/nbiancac/ln_work/scratch0/DELPHI_results/HLLHC/IP7-coatings/Results/';
mkdir(ResultDir)
plane=repmat([{'y'}],1,1);
typeimp=repmat([{'dip'}],1,1);

lista={};
lista.DataDir=[];
lista.scenario=[];
lista.plane=plane;
lista.typeimp=typeimp;
for ii=1:length(DataDir)
    lista.DataDir=[lista.DataDir,{strjoin([DataDir(ii),name(ii),'/'],'')}];
    lista.scenario=[lista.scenario,name(ii)];
end


%% Impedance plot absolute
flagshow='on';
lista.legend=regexprep(lista.scenario,[{'_'},{'baseline'}],[{' '},{''}]);
lista.color=[{'r'},{'k'},{'b'},{'m'},{'c'},{'y'}];
min_yax=0.4;max_yax=1.5;



lista.freq=[]; lista.Z=[];
lista.Zeff=[];lista.kick=[];lista.omegashift=[]; lista.ts=[];

type={'Total'};

for kk=1:length(lista.DataDir)
    
    imp=['Z',char(lista.plane(kk)),char(lista.typeimp(kk))];
    disp(lista.scenario{kk})
    L=dir([char(lista.DataDir(kk)),imp,'_',type{1},'*.dat']);
    L=dlmread([char(lista.DataDir(kk)),L.name],'',1,0); 
    [freq,Zre,Zim]=deal(L(:,1),L(:,2),L(:,3));
    lista.freq=[lista.freq,{freq}];
    lista.Z=[lista.Z,{(Zre+1i*Zim)}];
end

freq_all=[];
for kk=1:length(lista.DataDir)
   freq_all=[freq_all;cell2mat(lista.freq(kk))];
end

lista.freq_all=[];    lista.Z_all=[];
for kk=1:length(lista.DataDir)
   lista.freq_all=[lista.freq_all,sort(unique(freq_all))];
   lista.Z_all=[lista.Z_all,interp1(cell2mat(lista.freq(kk)),cell2mat(lista.Z(kk)),sort(unique(freq_all)))];
end

leg_vec=[];
figure(1);
set(gcf,'visible',flagshow)
for kk=1:length(lista.DataDir)
    imp=['Z',char(lista.plane(kk)),char(lista.typeimp(kk))];
    loglog(lista.freq_all(:,kk),real(lista.Z_all(:,kk)),'-','color',char(lista.color(kk)),'linewidth',2); hold on;
    loglog(lista.freq_all(:,kk),imag(lista.Z_all(:,kk)),'--','color',char(lista.color(kk)),'linewidth',2); hold on;
    leg_vec=[leg_vec,{[char(imp),' ',char(lista.legend(kk)),' Real']},{[char(imp),' ',char(lista.legend(kk)),' Imag']}];
end
title(regexprep(char(type),'_','-'))
hold off;
xlabel('f [Hz]');

if strcmp(imp,'Zlong') 
    ylabel([char(imp), ' \Omega']);
    ylim([1e-5 1e7])
else
    ylabel(['Z \Omega/m']);
    ylim([1e6 1e11])
end
xlim([1e2 1e10])
set(gca,'xtick',10.^[-2:2:15])
legend(leg_vec,'location','best')
set(gca,'Ygrid','on')
set(gca,'Yminorgrid','off')

set(gcf,'position',[ 150         228        1065         375])
set(legend,'position',[ 0.5548    0.2547    0.3770    0.6717]);
set(gca,'position',[ 0.1300    0.1227    0.4062    0.8023]);

if flagsave
    name=[imp,'_',char(type),'_',commentsave];
    disp(ResultDir)
    disp(name)
    s=hgexport('readstyle','PRSTAB-10pt');s.width='auto'; set(gcf,'PaperType','A3')
    hgexport(gcf,'',s,'applystyle',true);
    saveas(gcf, [ResultDir,name,'.fig'],'fig');
    hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
    hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
end

disp(lista);

if length(lista.scenario)>1
    leg_vec=[];
    ref=1;
    subset=[1:ref-1,ref+1:length(lista.DataDir)];
    for kk=subset
        figure(2);
        set(gcf,'visible',flagshow)
        semilogx(lista.freq_all(:,kk),real(lista.Z_all(:,kk))./real(lista.Z_all(:,ref)),'-','color',char(lista.color(kk)),'linewidth',2); hold on;
        semilogx(lista.freq_all(:,kk),imag(lista.Z_all(:,kk))./imag(lista.Z_all(:,ref)),'--','color',char(lista.color(kk)),'linewidth',2); hold on;
        imp=['Z',char(lista.plane(kk)),char(lista.typeimp(kk))];
        leg_vec=[leg_vec,{[imp,' ',char(lista.legend(kk)),' Real']},{[imp,' ',char(lista.legend(kk)),' Imag']}];
    end
    hold off;
    title([regexprep(char(type),'_','-'),' ratio to reference: ',char(lista.legend(ref))]);
    
    ylim([min_yax max_yax])
    xlim([1e2 1e10])
    set(gca,'xtick',10.^[-2:2:15]); set(gca,'ygrid','on')
    set(gca,'ytick',[min_yax:0.1:max_yax])
    legend(leg_vec,'location','bestoutside')
    xlabel('f [Hz]'); 
    ylabel(['Z/Z^{ref}']);
    set(gcf,'position',[ 150         228        1065         375])

    commentsave2=[commentsave,'-ratio'];
    if flagsave
        name=[imp,'_',char(type),'_',commentsave2];
        disp(ResultDir)
        disp(name)
        s=hgexport('readstyle','PRSTAB-10pt');s.width='auto';        set(gcf,'PaperType','A3')
        hgexport(gcf,'',s,'applystyle',true);
        saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    end
end


%%  Z vs f percent
close all

machine.Nb=1e11;
flagsave=1;

type_imp_HLLHC=[
{'Tapers-triplets'},...
{'BPM-triplets'},...
{'Pumping-holes-rest'},...
{'Pumping-holes-triplets'},...
{'RF-CMS-ALICE-LHCb'},...
{'Other-BB'},...
{'Geom-coll'},...
{'RW-coll'},...
{'RW-beam-screen'},...
{'RW-warmpipe'},...
{'RF-CMS-ATLAS-ALICE-LHCb'},...
{'Crab-cavities'}
];
type_imp=type_imp_HLLHC;

flagshow='on';
lista.color=distinguishable_colors(length(type_imp));
Nsample=1;

part='real';
plane='x';

if plane=='z'; plane=''; typeimp='long'; end
if plane=='x'; typeimp='dip'; end
if plane=='y'; typeimp='dip'; end

Zeff=[];ts=[];
for imp=[{['Z',plane,typeimp]}]
    for kk=1:length(lista.DataDir)
    close all
    lista.freq=[]; lista.Z=[];
    lista.freq_all=[]; lista.Z_all=[]; 
    lista.freq_all=[];
    lista.leg_vec=[];
    
    type={'Total'};
    imp=['Z',plane,char(typeimp)];
    L=dir([char(lista.DataDir(kk)),imp,'_',char(type),'*.dat']);
    L=dlmread([char(lista.DataDir(kk)),L.name],'',1,0); 
    [freq,Zre,Zim]=deal(L(:,1),L(:,2),L(:,3));
    lista.freq_tot={freq};
    lista.Z_tot={(Zre+1i*Zim)};
    
    
    for type=type_imp
        
        L=dir([char(lista.DataDir(kk)),imp,'_',type{1},'*B1.dat']);

        if ~isempty(L)
            disp(L.name)
            L=dlmread([char(lista.DataDir(kk)),L.name],'',1,0); 

            [freq,Zre,Zim]=deal(L(:,1),L(:,2),L(:,3));
            
            Z=interp1(freq,Zre+1i*Zim,lista.freq_tot{1},'linear','extrap');
            
            lista.Z=[lista.Z,{Z}];
            lista.leg_vec=[lista.leg_vec,{[char(type)]}];

        else
            warning('no file '); 
        end
    end

    

    
    h1_vec=[];
    offset_imp_low=zeros(size((lista.Z_tot{1})));
    for ii=1:size(lista.Z,2)
       if strcmp(part,'real')
           offset_imp_top=offset_imp_low+real(lista.Z{ii})./real(lista.Z_tot{1});
       elseif strcmp(part,'imag')
           offset_imp_top=offset_imp_low+imag(lista.Z{ii})./imag(lista.Z_tot{1});
           
       end
       
    offset_imp_top(isinf(offset_imp_top))=1e99;
    offset_imp_top(isnan(offset_imp_top))=0;
       
% figure()
% plot(offset_imp_low); hold on
% plot(offset_imp_top)

       figure(1);
       set(gcf,'visible',flagshow)
       lista.color(ii,:)
       h1=semilogx(lista.freq_tot{1},offset_imp_top,'-','color',lista.color(ii,:),'linewidth',5); hold on;
       h2=fill([lista.freq_tot{1};flipud(lista.freq_tot{1})],[offset_imp_low;flipud(offset_imp_top)],lista.color(ii,:),'edgecolor',lista.color(ii,:));
       offset_imp_low=offset_imp_top;
       h1_vec=[h1_vec,h1];

    end
    
    xlim([1e3 1e10])
    ylim([0 1])
    xlabel('Frequency [Hz]')
    set(gca,'xtick',[10.^[2:10]])
    set(gca,'ytick',[0:0.2:1])
    
    h_line=vline([10.^[2:10]],':k'); for h=h_line; set(h,'color',[.5,.5,.5]); end
    v_line=hline([0.2:0.2:0.8],':k'); for v=v_line; set(v,'color',[.5,.5,.5]); end
    if strcmp(part,'imag'); part_txt='Im'; else part_txt='Re'; end;
    ylabel(char([part_txt,'(',char(imp),') / ',part_txt,'(',char(imp),'^{tot})']))
    legend(h1_vec,lista.leg_vec,'location','best')
    box on;
    grid on;
    set(gcf,'position',[ 150         228        1065         375])
    set(legend,'position',[   0.5729    0.2831    0.2487    0.6417]);
    set(gca,'position',[ 0.1300    0.1227    0.4062    0.8023]);
    title(regexprep(char(lista.scenario(kk)),{'/','_'},{'',' '}))
    
    
    if flagsave
        name=[char(imp),'_',part,'_percent_',regexprep(char(lista.scenario(kk)),'/','')];
        disp(name)
        s=hgexport('readstyle','PRSTAB');s.FixedFontSize='12';s.width='auto'; set(gcf,'PaperType','A3')
        hgexport(gcf,'',s,'applystyle',true);
%      saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
%         hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    end
    
    end %scenarios
end %impedance 

%% Heating by elements


part='real';
plane='z';

if plane=='z'; plane=''; end

for imp=[{['Z',plane,'long']}]
    for kk=1:length(lista.DataDir)
    close all
    lista.freq=[]; lista.Z=[];
    lista.freq_all=[]; lista.Z_all=[]; 
    lista.Zeff=[]; lista.freq_all=[];
    lista.leg_vec=[];
    lista.powerloss=[];
    for type=type_imp
        
        L=dir([char(lista.DataDir(kk)),imp{1},'_',type{1},'*B1.dat']);
        if ~isempty(L)
            L=dlmread([char(lista.DataDir(kk)),L.name],'',1,0); 
            [freq,Zre,Zim]=deal(L(:,1),L(:,2),L(:,3));
            lista.freq=[lista.freq,{freq}];
            lista.Z=[lista.Z,{(Zre+1i*Zim)}];
            lista.freq_all=sort(unique([lista.freq_all;freq]));
            lista.leg_vec=[lista.leg_vec,{[char(type)]}];
            lista.powerloss=[lista.powerloss,power_loss(freq,Zre,machine)];
        end
    end

    for col_ind=1:length(lista.Z)
        lista.Z_all=[lista.Z_all,interp1(cell2mat(lista.freq(col_ind)),cell2mat(lista.Z(col_ind)),lista.freq_all,'linear','extrap')];
    end
        lista.Z_tot=sum(lista.Z_all,2);
    

    h1_vec=[];
    offset_imp_low=zeros(size((lista.Z_tot)));
    for ii=1:size(lista.Z_all,2)
       if strcmp(part,'real')
           offset_imp_top=offset_imp_low+real(lista.Z_all(:,ii))./real(lista.Z_tot);
       elseif strcmp(part,'imag')
           offset_imp_top=offset_imp_low+imag(lista.Z_all(:,ii))./imag(lista.Z_tot);
       end
       figure(1);
       set(gcf,'visible',flagshow)
       sample=1:Nsample:length(lista.freq_all);
       h1=semilogx(lista.freq_all(sample),offset_imp_top(sample),'-','color',lista.color(ii,:),'linewidth',5); hold on;
       h2=fill([lista.freq_all(sample);flipud(lista.freq_all(sample))],[offset_imp_low(sample);flipud(offset_imp_top(sample))],lista.color(ii,:),'edgecolor','k');
       offset_imp_low=offset_imp_top;
       h1_vec=[h1_vec,h1];
    end
    xlim([1e3 1e10])
    ylim([0 1])
    xlabel('Frequency [Hz]')
    set(gca,'xtick',[10.^[2:10]])
    set(gca,'ytick',[0:0.2:1])
    h_line=vline([10.^[2:10]],':k'); for h=h_line; set(h,'color',[.5,.5,.5]); end
    v_line=hline([0.2:0.2:0.8],':k'); for v=v_line; set(v,'color',[.5,.5,.5]); end
    if strcmp(part,'imag'); part_txt='Im'; else part_txt='Re'; end;
    ylabel(char([part_txt,'(',char(imp),') / ',part_txt,'(',char(imp),'^{tot})']))
    legend(h1_vec,lista.leg_vec,'location','best')
    box on;
    grid on;
    set(gcf,'position',[ 150         228        1065         375])
    set(legend,'position',[   0.5729    0.2831    0.2487    0.6417]);
    set(gca,'position',[ 0.1300    0.1227    0.4062    0.8023]);
    title(regexprep(char(lista.scenario(kk)),{'/','_'},{'',' '}))
    if flagsave
        name=[char(imp),'_',part,'_percent_',regexprep(char(lista.scenario(kk)),'/','')];
        disp(name)
        s=hgexport('readstyle','PRSTAB');s.FixedFontSize='12';s.width='auto'; set(gcf,'PaperType','A3')
        hgexport(gcf,'',s,'applystyle',true);
%         saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
%         hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    end
    
    end %scenarios
end %impedance

      figure(2)
      Y=1:length(lista.powerloss);
      X=lista.powerloss;
      stairs(lista.powerloss,1:length(lista.powerloss),'-k','linewidth',2);
      set(gca,'ytick',(1:length(lista.powerloss))-0.5)
      set(gca,'yticklabel',lista.leg_vec)
      xlabel('Power loss [W]')
      for kk=1:length(Y)-1
        h=line([0 X(kk+1)],[.5+kk .5+kk]);
      set(h,'linestyle',':','color','k')
      end
      h=vline(0:500:3000,'-'); hold on;
      set(h,'color',[0.5 0.5 0.5])

%% LHC scenarios tune shift element by element
machine.Nb=1e11;

for ss=1%:length(lista.scenario)

type_imp_HLLHC=[
    {'Total'},...
    {'Tapers-triplets'},...
    {'BPM-triplets'},...
    {'Pumping-holes-rest'},...
    {'Pumping-holes-triplets'},...
    {'RF-CMS-ALICE-LHCb'},...
    {'Other-BB'},...
    {'Geom-coll'},...
    {'RW-coll'},...
    {'RW-beam-screen'},...
    {'RW-warmpipe'},...
    {'RF-CMS-ATLAS-ALICE-LHCb'},...
    {'Crab-cavities'}
];
element=type_imp_HLLHC;

% type_imp_LHC=[
% {'Total'},...
% {'Tapers-triplets'},...
% {'BPM-triplets'},...
% {'Pumping-holes'},...
% {'RF-CMS-ALICE-LHCb'},...
% {'Other-BB'},...
% {'Geom-coll'},...
% {'RW-coll'},...
% {'RW-beam-screen'},...
% {'RW-warmpipe'}];
% element=type_imp_LHC;

[coll_names,gaps,betx,bety,sigma]=read_coll_file([CollDir,char(lista.scenario{ss}),'.txt'],'all','unique');
lista.indcoll{ss}=length(element)+[1:length(coll_names)];

for ii=1:length(coll_names)
    element=[element,coll_names(ii)];
end
    
lista.element{ss}=element;

for plane=[{'x'},{'y'}]
    plane=char(plane);
for typeimp=[{'dip'}];
        typeimp=char(typeimp);

        ts_vec=[]; rt_vec=[]; Zeff_vec=[]; kick_vec=[]; omegashift_vec=[];
        machine.M=1;
        m=0;nx=0;

            for ii=1%:length(lista.element{ss})
                namefile=[]; letto=[];
                try namefile=[char(lista.DataDir(ss)),'Z',plane,typeimp,'_',char(lista.element{ss}{ii}),'_RW','.dat'];
                    letto=dlmread(namefile,'',1,0);
                    disp(namefile);
                catch 'Not a RW'; 
                end
                try namefile=[char(lista.DataDir(ss)),'Z',plane,typeimp,'_',char(lista.element{ss}{ii}),'_',char(lista.scenario{ss}),'.dat']; 
                    letto=dlmread(namefile,'',1,0);
                    disp(namefile);
                catch 'Not a file in scenario'; 
                end
                
                if ~isempty(letto)
                    Qp=0;
                    disp(['TS calculation: M=',num2str(machine.M),', Nb=',num2str(machine.Nb/1e11),'e11, Qp=',num2str(Qp)]);
                    machine.chromax=Qp/machine.Qx;
                    machine.chromay=Qp/machine.Qy;
                    [Zeff_vec(ii),kick_vec(ii),omegashift_vec(ii),mat]=Zt_eff(letto(:,1),letto(:,2)+1i*letto(:,3),machine,m,nx,'Sinusoidal','proton',char(plane),'h_range',1e-3);
                    ts_vec(ii)=omegashift_vec(ii)/machine.omega0;
                    
                    Qp=-5;
                    disp(['RT calculation: M=',num2str(machine.M),', Nb=',num2str(machine.Nb/1e11),'e11, Qp=',num2str(Qp)]);
                    machine.chromax=Qp/machine.Qx;
                    machine.chromay=Qp/machine.Qy;
                    [~,~,omegashift,~]=Zt_eff(letto(:,1),letto(:,2)+1i*letto(:,3),machine,m,nx,'Sinusoidal','proton',char(plane),'h_range',1e-3);
                    rt_vec(ii)=-1/(imag(omegashift));
                    
                    
                else
                    Zeff_vec(ii)=0;kick_vec(ii)=0;omegashift_vec(ii)=0;rt_vec(ii)=0;
                    disp([plane,typeimp,' component not present'])
                end
            end
            
            eval(['lista.ts',plane,typeimp,'(ss,:)=ts_vec;']);
            eval(['lista.rt',plane,typeimp,'(ss,:)=rt_vec;']);
            eval(['lista.Zeff',plane,typeimp,'(ss,:)=Zeff_vec;']);
            eval(['lista.kick',plane,typeimp,'(ss,:)=kick_vec;']);
            eval(['lista.omegashift',plane,typeimp,'(ss,:)=omegashift_vec;']);
            
end
end

end % scenario

%% Tune shifts by collimators
flagsave=0;


for ss=1:length(lista.scenario)
    name=['Collimators_',commentsave,'_',char(lista.scenario{ss})];
    index_elements=cell2mat(lista.indcoll(ss));
pause

%     name=['Allthemachine_',commentsave,'_',char(lista.scenario{ss})];
%     index_elements=setdiff(1:length(element),lista.indcoll{ss});

%     close all
    
    names=lista.element{ss}(index_elements);
    
      figure(2)
      set(gcf,'visible','on')
      Y=[0:length(names)];
      X=[0,-real(lista.tsxdip(ss,index_elements)+lista.tsxquad(ss,index_elements))]*1e5;
      h1=stairs(X,Y,'-k','linewidth',2); hold on;
      for kk=(0.5:(length(X)))
        h=line([0 X(kk+.5)],[kk-1 kk-1]);
      set(h,'linestyle',':','color','k')
      end
      
      X=[0,-real(lista.tsydip(ss,index_elements)+lista.tsyquad(ss,index_elements))]*1e5;
      h2=stairs(X,Y,'-r','linewidth',2); hold off;

      set(gca,'ytick',0.5:(length(X)-1))
      set(gca,'yticklabel',names)

      xlabel(['Total tune shift [10^{-5}]'])
      for kk=(0.5:(length(X)))
        h=line([0 X(kk+.5)],[kk-1 kk-1]);
      set(h,'linestyle',':','color','r')
      end
      h=vline(0:1:5,'-'); hold on;
      set(h,'color',[0.5 0.5 0.5])
    legend_vec=[{'\DeltaQ_x'},{'\DeltaQ_y'}];
      legend([h1,h2],legend_vec)
    set(gcf,'position',[ 774     1   512   661]);

    ylim([min(Y) max(Y)])
    % title('Tune shift from CFC collimators - HL-LHC 7 TeV ')
    if flagsave==1
        s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12';
        hgexport(gcf,'',s,'applystyle',true);
    %     saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,'TS_',name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,'TS_',name,'.png'],s,'Format','png');
        hgexport(gcf, [ResultDir,'TS_',name,'.jpg'],s,'Format','jpeg');
        disp([ResultDir,'TS_',name,'.pdf'])
    end


     figure(3)
     set(gcf,'visible',flagshow)
      Y=[0:length(names)];
      X=[0,1./(lista.rtxdip(ss,index_elements)+lista.rtxquad(ss,index_elements))];
      X(X==Inf)=-1;
      h1=stairs(X,Y,'-k','linewidth',2); hold on;
      X=[0,1./(lista.rtydip(ss,index_elements)+lista.rtyquad(ss,index_elements))];
      X(X==Inf)=-1;
      h2=stairs(X,Y,'-r','linewidth',2); hold off;

      set(gca,'ytick',0.5:(length(X)-1))
      set(gca,'yticklabel',names)

      xlabel(['Growth rate [s^{-1}]'])
      for kk=(0.5:(length(X)))
        h=line([0 X(kk+.5)],[kk-1 kk-1]);
      set(h,'linestyle',':','color','k')
      end
    %   h=vline(0:1:5,'-'); hold on;
      set(h,'color',[0.5 0.5 0.5])
    legend_vec=[{'\tau_x'},{'\tau_y'}];
      legend([h1,h2],legend_vec)
    set(gcf,'position',[ 774     1   512   661]);

    xlim([0 0.2])
    ylim([min(Y) max(Y)])

    if flagsave==1
        s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12';
        hgexport(gcf,'',s,'applystyle',true);
    %     saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,'GR_',name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,'GR_',name,'.png'],s,'Format','png');
        disp([ResultDir,'GR_',name,'.pdf'])
    end
end

%% Tune shifts by collimator families

for ss=1:length(lista.scenario)
    lista.collfamily{ss}=[{'Total'},{'RW-beam-screen'},{'Tapers-triplets'},...
{'BPM-triplets'},...
{'Pumping-holes'},...
{'RF-CMS-ALICE-LHCb'},...
{'Other-BB'},...
{'Geom-coll'},...
{'RW-coll'},...
{'RW-warmpipe'},{'TCT'},{'TCP'},{'TCSG.*3'},{'TCSG.*7'},{'TCL'},{'TCSP'},{'TDI'},{'TCDQ'}];

    lista.indcollfamily{ss}=[];
    for ii=1:length(lista.collfamily{ss})
        lista.indcollfamily{ss}{ii}=~cellfun(@isempty,regexp(element,lista.collfamily{ss}(ii)));
    end
end

for ss=1:length(lista.scenario)
%      close all
     X=[0];
     Y=[0:length(lista.collfamily{ss})];
     for nn=1:length(lista.collfamily{ss})
         index=lista.indcollfamily{ss}{nn};
         tsxdip=lista.tsxdip(ss,index);
         tsxquad=lista.tsxquad(ss,index);
         
         X=[X,-real(sum(tsxdip)+sum(tsxquad))*1e4];
     end
   
      figure(2)
      set(gcf,'visible','on')
      h1=stairs(X,Y,'-k','linewidth',2); hold on;
      for kk=(0.5:(length(X)))
          h=line([0 X(kk+.5)],[kk-1 kk-1]);
          set(h,'linestyle',':','color','k')
      end
      title(lista.scenario(ss))
      X=[0];
     Y=[0:length(lista.collfamily{ss})];
     for nn=1:length(lista.collfamily{ss})
         index=lista.indcollfamily{ss}{nn};
         tsydip=lista.tsydip(ss,index);
         tsyquad=lista.tsyquad(ss,index);
         X=[X,-real(sum(tsydip)+sum(tsyquad))*1e4];
     end
     
      h2=stairs(X,Y,'-r','linewidth',2); hold on;

      set(gca,'ytick',0.5:(length(X)-1))
      set(gca,'yticklabel',(lista.collfamily{ss}))

      xlabel(['Total tune shift [10^{-4}]'])
      for kk=(0.5:(length(X)))
        h=line([0 X(kk+.5)],[kk-1 kk-1]);
      set(h,'linestyle',':','color','r')
      end
      h=vline(0:1:5,'-'); hold on;
      set(h,'color',[0.5 0.5 0.5])
    legend_vec=[{'\DeltaQ_x'},{'\DeltaQ_y'}];
      legend([h1,h2],legend_vec)
    set(gcf,'position',[ 774     1   512   661]); hold off;
%     xlim([0 3])
    name=['CollimatorsFamily_TS_',commentsave,'_',char(lista.scenario{ss})];
    ylim([min(Y) max(Y)])
 
    if flagsave==1
        s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12';
        hgexport(gcf,'',s,'applystyle',true);
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
        hgexport(gcf, [ResultDir,name,'.jpg'],s,'Format','jpeg');
        disp([ResultDir,name,'.pdf'])
    end


%      figure(3)
%      set(gcf,'visible',flagshow)
%       Y=[0:length(names)];
%       X=[0,1./(lista.rtxdip(ss,cell2mat(lista.indcoll(ss)))+lista.rtxquad(ss,cell2mat(lista.indcoll(ss))))];
%       X(X==Inf)=-1;
%       h1=stairs(X,Y,'-k','linewidth',2); hold on;
%       X=[0,1./(lista.rtydip(ss,cell2mat(lista.indcoll(ss)))+lista.rtyquad(ss,cell2mat(lista.indcoll(ss))))];
%       X(X==Inf)=-1;
%       h2=stairs(X,Y,'-r','linewidth',2); hold off;
% 
%       set(gca,'ytick',0.5:(length(X)-1))
%       set(gca,'yticklabel',names)
% 
%       xlabel(['Growth rate [s^{-1}]'])
%       for kk=(0.5:(length(X)))
%         h=line([0 X(kk+.5)],[kk-1 kk-1]);
%       set(h,'linestyle',':','color','k')
%       end
%     %   h=vline(0:1:5,'-'); hold on;
%       set(h,'color',[0.5 0.5 0.5])
%     legend_vec=[{'\tau_x'},{'\tau_y'}];
%       legend([h1,h2],legend_vec)
%     set(gcf,'position',[ 774     1   512   661]);
% 
%     name=['Collimators_GR_',commentsave,'_',char(lista.scenario{ss})];
%     xlim([0 0.2])
%     ylim([min(Y) max(Y)])
% 
%     if flagsave==1
%         s=hgexport('readstyle','PRSTAB'); s.FixedFontSize='12';
%         hgexport(gcf,'',s,'applystyle',true);
%     %     saveas(gcf, [ResultDir,name,'.fig'],'fig');
%         hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
%         hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
%         disp([ResultDir,name,'.pdf'])
%     end
end

%% Compare wake models 
close all

for imp=[{'Wxdip'},{'Wxquad'},{'Wydip'},{'Wyquad'}]
    
    lista.freq=[]; lista.Z=[];
    type={'Allthemachine'};%{'Allthemachine'}

    flagsave=1;

    for kk=1:length(lista.DataDir)
        L=dir([char(lista.DataDir(kk)),imp{1},'_',type{1},'*.dat']);
        L.name
        L=dlmread([char(lista.DataDir(kk)),L.name],'',1,0); 
        [freq,Zre,Zim]=deal(L(:,1),L(:,2),L(:,3));
        lista.freq=[lista.freq,{freq}];
        lista.Z=[lista.Z,{Zre+1i*Zim}];
    end

    freq_all=[];
    for kk=1:length(lista.DataDir)
       freq_all=[freq_all;cell2mat(lista.freq(kk))];
    end

    lista.freq_all=[];
    lista.Z_all=[];
    for kk=1:length(lista.DataDir)
       lista.freq_all=[lista.freq_all,sort(unique(freq_all))];
       lista.Z_all=[lista.Z_all,interp1(cell2mat(lista.freq(kk)),cell2mat(lista.Z(kk)),sort(unique(freq_all)))];
    end


    leg_vec=[];
    for kk=1:length(lista.DataDir)
        figure(1);
        semilogx(lista.freq_all(:,kk),(lista.Z_all(:,kk)),'-','color',char(lista.color(kk)),'linewidth',2); hold on;
        leg_vec=[leg_vec,{[char(lista.legend(kk))]}];
    end
    title(regexprep(char(type),'_','-'))
    hold off;
    % ylim([1e-3 1e11])
    % xlim([1e-2 1e15])
    % set(gca,'xtick',10.^[-2:2:15])
    legend(leg_vec,'location','best')
    xlabel('z [m]'); 
    ylabel([char(imp), ' V/mC']);

    if flagsave
        name=[char(imp),'_',char(type),'_',commentsave];
        s=hgexport('readstyle','PRSTAB-10pt');
        hgexport(gcf,'',s,'applystyle',true);
        saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    end

    leg_vec=[];
    ref=1;
    subset=[1:ref-1,ref+1:length(lista.DataDir)];
    for kk=subset
        figure(2);
        semilogx(lista.freq_all(:,kk),(lista.Z_all(:,kk))./(lista.Z_all(:,ref)),'-','color',char(lista.color(kk)),'linewidth',2); hold on;
        leg_vec=[leg_vec,{[char(lista.legend(kk))]}];
    end
    hold off;
    title([regexprep(char(type),'_','-'),' ratio to reference: ',char(lista.legend(ref))]);
    ylim([-5 5])
    % xlim([1e-2 1e15])
    % set(gca,'xtick',10.^[-2:2:15])
    legend(leg_vec,'location','best')
    xlabel('z [m]'); 
    ylabel([char(imp), '/',char(imp),'^{ref}']);

    commentsave2=[commentsave,'-ratio'];
    if flagsave
        name=[char(imp),'_',char(type),'_',commentsave];
        s=hgexport('readstyle','PRSTAB-10pt');
        hgexport(gcf,'',s,'applystyle',true);
        saveas(gcf, [ResultDir,name,'.fig'],'fig');
        hgexport(gcf, [ResultDir,name,'.pdf'],s,'Format','pdf');
        hgexport(gcf, [ResultDir,name,'.png'],s,'Format','png');
    end
    
end % Wake type
