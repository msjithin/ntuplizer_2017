#multicrab
from WMCore.Configuration import Configuration
config = Configuration()
from CRABClient.UserUtilities import config
config = config() 
#if __name__ == '__main__':
from CRABAPI.RawCommand import crabCommand

def submit(config):
  res = crabCommand('submit', config = config)


dataset = {
  'DYJetsToLL_LO' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'DYJetsToLL_LOext' : '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'DYJetsToLL' : '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'DY1JetsToLL' : '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'DY2JetsToLL' : '/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'DY3JetsToLL' : '/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'DY4JetsToLL' : '/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'TTJets' : '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' ,  
  'TTTo2L2Nu_powheg' : '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' ,  
  'TTToHadronic_powheg' : '/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' ,  
  'TTToSemiLeptonic_powheg' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM' ,  
  'WJetsToLNu' : '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM' , 
  'WJetsToLNu_HT-100To200' : '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM' , 
  'WJetsToLNu_HT-200To400' : '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WJetsToLNu_HT-400To600' : '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WJetsToLNu_HT-600To80' : '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WJetsToLNu_HT-800To1200' : '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WJetsToLNu_HT-1200To2500' : '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WJetsToLNu_HT-2500ToInf' : '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM' , 
  'EWKWMinus2Jets_WToLNu' : '/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'EWKWPlus2Jets_WToLNu' : '/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'EWKZ2Jets_ZToLL' : '/EWKZ2Jets_ZToLL_M-50_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'EWKZ2Jets_ZToNuNu' : '/EWKZ2Jets_ZToNuNu_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'GluGluHToTauTau' : '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WpWpJJ_EWK-QCD' : '/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'VBFHToTauTau' : '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZHToTauTau' : '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WplusHToTauTau' : '/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WminusHToTauTau' : '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-100To200' : '/ZJetsToNuNu_HT-100To200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-200To400' : '/ZJetsToNuNu_HT-200To400_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-400To600' : '/ZJetsToNuNu_HT-400To600_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-600To800' : '/ZJetsToNuNu_HT-600To800_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-800To1200' : '/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-1200To2500' : '/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZJetsToNuNu_HT-2500ToInf' : '/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WZTo1L1Nu2Q' : '/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM' , 
  'WZTo2L2Q' : '/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WZTo3LNu' : '/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ST_tW_antitop' : '/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ST_tW_top' : '/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ST_t-channel_antitop' : '/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ST_t-channel_top' : '/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WWToLNuQQ' : '/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'WWTo2L2Nu' : '/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM' , 
  'ZZTo2L2Q' : '/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZZTo4L' : '/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM' , 
  'WWW' : '/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WWZ' : '/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'WZZ' : '/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' , 
  'ZZZ' : '/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM' 
  }



name = 'MonoHiggs_2017_12April_MC_LOSamples'
config.section_("General")
config.General.workArea = 'crab_'+name
config.General.transferOutputs = True
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['ggtree_mc.root'] 
config.section_("Data")

config.Data.publication = False
config.section_("Site")
config.section_("User")
config.section_("Debug")

config.Site.storageSite = 'T2_US_Wisconsin'

config.JobType.psetName = 'run_mc2017_94X.py'
#config.JobType.inputFiles = ['Fall17_17Nov2017_V4_MC.db','Fall17_17Nov2017_V4_MC_L2Relative_AK8PFchs.txt','Fall17_17Nov2017_V4_MC_L3Absolute_AK8PFchs.txt']
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'

listOfSamples = [  'DYJetsToLL_LO', 'DYJetsToLL_LOext', 'TTToSemiLeptonic_powheg', 'TTTo2L2Nu_powheg', 'TTToHadronic_powheg']
#listOfSamples = [ 'DYJetsToLL', 'DY1JetsToLL' ,  'DY2JetsToLL' ,  'DY3JetsToLL' ,  'DY4JetsToLL',  'TTJets' ,  'WJetsToLNu',  'WJetsToLNu_HT-100To200',  'WJetsToLNu_HT-200To400',  'WJetsToLNu_HT-400To600',  'WJetsToLNu_HT-600To80' ,  'WJetsToLNu_HT-800To1200',  'WJetsToLNu_HT-1200To2500',  'WJetsToLNu_HT-2500ToInf' ,  'EWKWMinus2Jets_WToLNu' ,  'EWKWPlus2Jets_WToLNu',  'EWKZ2Jets_ZToLL',  'EWKZ2Jets_ZToNuNu',  'GluGluHToTauTau',  'WpWpJJ_EWK-QCD',  'VBFHToTauTau' ,  'ZHToTauTau',  'WplusHToTauTau',  'WminusHToTauTau' ,  'ZJetsToNuNu_HT-100To200' ,  'ZJetsToNuNu_HT-200To400',  'ZJetsToNuNu_HT-400To600',  'ZJetsToNuNu_HT-600To800',  'ZJetsToNuNu_HT-800To1200' ,  'ZJetsToNuNu_HT-1200To2500',  'ZJetsToNuNu_HT-2500ToInf' ,'WZTo1L1Nu2Q',  'WZTo2L2Q' ,'WZTo3LNu' ,  'ST_tW_antitop',  'ST_tW_top' ,'ST_t-channel_antitop' ,'ST_t-channel_top',  'WWToLNuQQ' ,'WWTo2L2Nu' ,'ZZTo2L2Q' ,'ZZTo4L' ,  'WWW' ,'WWZ','WZZ' ,'ZZZ'  ]

for sample in listOfSamples:  
  config.General.requestName = sample
  config.Data.inputDataset = dataset[sample]
  config.Data.unitsPerJob = 1
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/gomber/'+name
  submit(config)
