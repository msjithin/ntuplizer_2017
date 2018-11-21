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
  'sPho_dataset1': '/SinglePhoton/Run2017B-31Mar2018-v1/MINIAOD',
  'sPho_dataset2': '/SinglePhoton/Run2017C-31Mar2018-v1/MINIAOD',
  'sPho_dataset3': '/SinglePhoton/Run2017D-31Mar2018-v1/MINIAOD',
  'sPho_dataset4': '/SinglePhoton/Run2017E-31Mar2018-v1/MINIAOD',
  'sPho_dataset5': '/SinglePhoton/Run2017F-31Mar2018-v1/MINIAOD',
  
  'sEle_dataset1': '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD',
  'sEle_dataset2': '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD',
  'sEle_dataset3': '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD',
  'sEle_dataset4': '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD',
  'sEle_dataset5': '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD',
  'sMu_dataset1': '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
  'sMu_dataset2': '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
  'sMu_dataset3': '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
  'sMu_dataset4': '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
  'sMu_dataset5': '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',
  'Tau_dataset1': '/Tau/Run2017B-31Mar2018-v1/MINIAOD',
  'Tau_dataset2': '/Tau/Run2017C-31Mar2018-v1/MINIAOD',
  'Tau_dataset3': '/Tau/Run2017D-31Mar2018-v1/MINIAOD',
  'Tau_dataset4': '/Tau/Run2017E-31Mar2018-v1/MINIAOD',
  'Tau_dataset5': '/Tau/Run2017F-31Mar2018-v1/MINIAOD',

  'Embedded_MuTau_2017B': '/EmbeddingRun2017B/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
  'Embedded_MuTau_2017B': '/EmbeddingRun2017C/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
  'Embedded_MuTau_2017C' : '/EmbeddingRun2017D/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
  'Embedded_MuTau_2017D' : '/EmbeddingRun2017E/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',
  'Embedded_MuTau_2017E' : ' /EmbeddingRun2017F/MuTauFinalState-inputDoubleMu_94X_miniAOD-v2/USER',

}

config.section_('General')


name = 'MonoHiggs_Tau_2017_dataset_correctditautrigger'
config.General.workArea = 'crab_'+name
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('Site')
config.Site.storageSite = 'T2_US_Wisconsin'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'run_data2017_94X.py'
#config.JobType.psetName = 'run_data_80X.py'
config.JobType.outputFiles = ['ggtree_data.root']
#config.JobType.inputFiles = ['Summer16_23Sep2016AllV4_DATA.db','Summer16_23Sep2016BCDV4_DATA_L2Relative_AK8PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L3Absolute_AK8PFchs.txt','Summer16_23Sep2016BCDV4_DATA_L2L3Residual_AK8PFchs.txt']


config.section_('Data') 
#config.Data.inputDBS = 'global'
config.Data.publication = False
config.Data.splitting = 'LumiBased'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
#Already submitted:
#listOfSamples = ['sMu_dataset1']
#listOfSamples = ['sPho_dataset1', 'sPho_dataset2','sPho_dataset3','sPho_dataset4','sPho_dataset5']

listOfSamples = ['Tau_dataset1','Tau_dataset2','Tau_dataset3','Tau_dataset4','Tau_dataset5']
#listOfSamples = ['sMu_dataset1', 'sMu_dataset2','sMu_dataset3','sMu_dataset4','sMu_dataset5','Tau_dataset1','Tau_dataset2','Tau_dataset3','Tau_dataset4','Tau_dataset5', 'sEle_dataset1','sEle_dataset2','sEle_dataset3','sEle_dataset4','sEle_dataset5']
#listOfSamples = ['sMu_dataset1', 'sMu_dataset2','sMu_dataset3','sMu_dataset4','sMu_dataset5','Tau_dataset1','Tau_dataset2','Tau_dataset4','Tau_dataset5', 'sEle_dataset1','sEle_dataset2','sEle_dataset3','sEle_dataset4','sEle_dataset5']
#listOfSamples = ['Tau_dataset4','Tau_dataset5', 'sEle_dataset1','sEle_dataset2','sEle_dataset3','sEle_dataset4','sEle_dataset5']
#listOfSamples = ['Tau_dataset3']
for sample in listOfSamples:  
  config.General.requestName = sample
  config.Data.inputDataset = dataset[sample]
  config.Data.unitsPerJob = 15
  config.Data.totalUnits = -1
  config.Data.outLFNDirBase = '/store/user/jmadhusu/'+name
  submit(config)
