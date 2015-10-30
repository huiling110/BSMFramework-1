import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000 
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# NOTE: the pick the right global tag!
# for PHYS14 scenario PU20bx25: global tag is PHYS14_25_V1
# as a rule, find the global tag in the DAS under the Configs for given dataset
process.GlobalTag.globaltag = 'MCRUN2_74_V9::All'
#####
##   Dump gen particle list 
#####
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printGenParticleList = cms.EDAnalyzer("ParticleListDrawer",
 maxEventsToPrint = cms.untracked.int32(-1),
 printVertex = cms.untracked.bool(True),
 src = cms.InputTag("prunedGenParticles")
)
#####
##   Trigger
#####
#process.hltFilter = cms.EDFilter('HLTHighLevel',
# TriggerResultsTag = cms.InputTag('TriggerResults','','HLT'),
# HLTPaths          = cms.vstring(
#  'HLT_Ele32_eta2p1_WP75_Gsf_v*',
#  'HLT_IsoMu27_v*',
# ),
# eventSetupPathsKey = cms.string(''),
# andOr              = cms.bool(True), #---- True = OR, False = AND between the HLT paths
# throw              = cms.bool(False)
#)
#TTHbb
#####
##   Trigger
#####
process.hltFilter = cms.EDFilter('HLTHighLevel',
 TriggerResultsTag = cms.InputTag('TriggerResults','','HLT'),
 HLTPaths          = cms.vstring(
  'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*',
  'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*',
  'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*',
  'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*',
  'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*',
  'HLT_Ele27_eta2p1_WP85_Gsf_HT200_v*',
  'HLT_IsoMu24_eta2p1_v*',
 ),
 eventSetupPathsKey = cms.string(''),
 andOr              = cms.bool(True), #---- True = OR, False = AND between the HLT paths
 throw              = cms.bool(False)
)
#####
##   Input files
#####
#process.GlobalTag.globaltag = 'PHYS14_25_V2::All'
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      #TPrime b -> tZb (M=1.0TeV)
      #'/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1036477B-3A3A-E511-B6B8-002590593920.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1889D979-3A3A-E511-B60D-008CFA111294.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1A2EF284-DE39-E511-BEA8-0025905A611E.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/406B9572-3A3A-E511-8AD3-AC162DAB0B08.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/44642142-E239-E511-9301-001CC4A6DC20.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/44BA374E-143A-E511-AF1D-00259029E7FC.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/64128582-DE39-E511-B997-0025905A6090.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9A98F77E-3A3A-E511-846E-002590D9D89C.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A0CFE576-3A3A-E511-885B-002354EF3BDF.root','/store/mc/RunIISpring15DR74/TprimeBToTZ_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C4489C32-3A3A-E511-AE83-009C029C1160.root',
      #TTHbb
      #'/store/mc/RunIISpring15DR74/ttHTobb_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/141B9915-1F08-E511-B9FF-001E675A6AB3.root',
      #'/store/mc/RunIISpring15DR74/ttHTobb_M125_13TeV_powheg_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/1440BF72-A308-E511-9812-90B11C1453E1.root',
      #TT
      '/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/0AB045B5-BB0C-E511-81FD-0025905A60B8.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/0CB01C19-BB0C-E511-860B-0025905A60A8.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/0E389719-BB0C-E511-A233-0025905A60F2.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/10590823-AA0C-E511-A3BC-00259073E388.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/121AE819-BB0C-E511-AF99-0025905A60B8.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/185E830A-BD0C-E511-89B0-0025905A6136.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2895081D-BB0C-E511-8DD1-0025905A7786.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2C20CFB5-A90C-E511-A2F5-00259073E516.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/3224EC18-BB0C-E511-9161-0025905A6076.root',
      #'/store/mc/RunIISpring15DR74/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/34F08099-B40C-E511-AE64-002590CB0B5A.root'
      #DYJetsToLL
      #'/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root'
    ),
 skipEvents = cms.untracked.uint32(0)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )
#
# START ELECTRON ID SECTION
#
# Set up everything that is needed to compute electron IDs and
# add the ValueMaps with ID decisions into the event data stream
#
# Load tools and function definitions
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
process.load("RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cfi")
# overwrite a default parameter: for miniAOD, the collection name is a slimmed one
process.egmGsfElectronIDs.physicsObjectSrc = cms.InputTag('slimmedElectrons')
from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry
process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDs)
# Define which IDs we want to produce
# Each of these two example IDs contains all four standard
# cut-based ID working points (only two WP of the PU20bx25 are actually used here).
# define which IDs we want to produce
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_PHYS14_PU20bx25_V2_cff',
                 'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV51_cff']
#Add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
# Do not forget to add the egmGsfElectronIDSequence to the path,
# as in the example below!
#
# END ELECTRON ID SECTION
#

process.TFileService = cms.Service("TFileService",
fileName = cms.string("OutTree.root")
)

## JEC
from JetMETCorrections.Configuration.JetCorrectionServices_cff import *
process.ak4PFCHSL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK4PFchs'),
    srcRho      = cms.InputTag( 'fixedGridRhoFastjetAll' )
    )
process.ak4PFchsL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK4PFchs' )
process.ak4PFchsL3Absolute = ak4CaloL3Absolute.clone( algorithm = 'AK4PFchs' )
process.ak4PFchsL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring('ak4PFCHSL1Fastjet','ak4PFchsL2Relative','ak4PFchsL3Absolute')
)


###############
#### tt+X
###############
# Setting input particle collections to be used by the tools
genJetCollection = 'ak4GenJetsCustom'
genParticleCollection = 'prunedGenParticles'
genJetInputParticleCollection = 'packedGenParticles'
# Supplies PDG ID to real name resolution of MC particles
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
# Producing own jets for testing purposes
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.ak4GenJetsCustom = ak4GenJets.clone(
    src = genJetInputParticleCollection,
    rParam = cms.double(0.4),
    jetAlgorithm = cms.string("AntiKt")
)
# Ghost particle collection used for Hadron-Jet association 
# MUST use proper input particle collection
from PhysicsTools.JetMCAlgos.HadronAndPartonSelector_cfi import selectedHadronsAndPartons
process.selectedHadronsAndPartons = selectedHadronsAndPartons.clone(
    particles = genParticleCollection
)
# Input particle collection for matching to gen jets (partons + leptons) 
# MUST use use proper input jet collection: the jets to which hadrons should be associated
# rParam and jetAlgorithm MUST match those used for jets to be associated with hadrons
# More details on the tool: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideBTagMCTools#New_jet_flavour_definition
from PhysicsTools.JetMCAlgos.sequences.GenHFHadronMatching_cff import genJetFlavourPlusLeptonInfos
process.genJetFlavourPlusLeptonInfos = genJetFlavourPlusLeptonInfos.clone(
    jets = genJetCollection,
    rParam = cms.double(0.4),
    jetAlgorithm = cms.string("AntiKt")
)
# Plugin for analysing B hadrons
# MUST use the same particle collection as in selectedHadronsAndPartons
from PhysicsTools.JetMCAlgos.sequences.GenHFHadronMatching_cff import matchGenBHadron
process.matchGenBHadron = matchGenBHadron.clone(
    genParticles = genParticleCollection
)
# Plugin for analysing C hadrons
# MUST use the same particle collection as in selectedHadronsAndPartons
from PhysicsTools.JetMCAlgos.sequences.GenHFHadronMatching_cff import matchGenCHadron
process.matchGenCHadron = matchGenCHadron.clone(
    genParticles = genParticleCollection
)

process.TNT = cms.EDAnalyzer("BSM3G_TNT_Maker",
    # boolean variables
    debug_ = cms.bool(False),
    filleventinfo       = cms.bool(True),
    filltriggerinfo     = cms.bool(True),
    fillmuoninfo        = cms.bool(True),
    fillelectronpatinfo = cms.bool(True),
    filltauinfo         = cms.bool(False),
    fillgeninfo         = cms.bool(False),
    fillPVinfo          = cms.bool(False),
    filljetinfo         = cms.bool(True),
    filltthjetinfo      = cms.bool(False),
    fillBoostedJetinfo  = cms.bool(False),
    fillTopSubJetinfo   = cms.bool(False),
    fillBJetnessinfo    = cms.bool(True),
    fillMETinfo         = cms.bool(True),
    fillphotoninfo      = cms.bool(False),   
    fillBTagReweight    = cms.bool(False),
    fillgenHFCategoryinfo = cms.bool(True),

    # make a super tiny ntuple, only with a few branches?
    super_TNT  = cms.bool(False),
    # is data or MC?
    is_data     = cms.bool(False),
 
    # input tags 
    triggerResults      = cms.InputTag( 'TriggerResults', '', 'HLT' ),
    vertices            = cms.InputTag("offlineSlimmedPrimaryVertices"),
    muons               = cms.InputTag("slimmedMuons"),
    patElectrons        = cms.InputTag("slimmedElectrons"),
    taus                = cms.InputTag("slimmedTaus"),
    photons             = cms.InputTag("slimmedPhotons"),
    #jets                = cms.InputTag("selectedPatJetsAK8PFCHS"),
    jets                = cms.InputTag("slimmedJets"),
    fatjets             = cms.InputTag("slimmedJetsAK8"),
    topsubjets          = cms.InputTag("slimmedJetsCMSTopTagCHSPacked", "SubJets"),
    mets                = cms.InputTag("slimmedMETs"),
    bits                = cms.InputTag("TriggerResults","","HLT"),
    prescales           = cms.InputTag("patTrigger"),
    objects             = cms.InputTag("selectedPatTrigger"),  
    packedPFCandidates  = cms.InputTag("packedPFCandidates"), 
    electronVetoIdMap   = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-veto"),
    electronLooseIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-loose"),
    electronMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-medium"),
    electronTightIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-PHYS14-PU20bx25-V2-standalone-tight"),
    eleHEEPIdMap        = cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV51"),

    # muon cuts
    Muon_pt_min              = cms.double(10.),
    Muon_eta_max             = cms.double(2.5),
    vtx_ndof_min        = cms.int32(4),
    vtx_rho_max         = cms.int32(2),
    vtx_position_z_max  = cms.double(24.),

    # electron cuts
    patElectron_pt_min       = cms.double(10.),
    patElectron_eta_max      = cms.double(2.5),

    # tau cuts
    Tau_pt_min  = cms.double(0.),
    Tau_eta_max = cms.double(50.),

    # jet cuts
    Jet_pt_min   = cms.double(30.),

    # photon cuts 
    Photon_pt_min   = cms.double(5.0),
    Photon_eta_max  = cms.double(5.0),    

    # primary vertex cuts
    Pvtx_ndof_min   = cms.double(4.),
    Pvtx_vtx_max  = cms.double(24.),
    Pvtx_vtxdxy_max = cms.double(24.),
	
    #ttHFCategorization
    genJetPtMin = cms.double(20),
    genJetAbsEtaMax = cms.double(2.4),
    genJets = cms.InputTag("ak4GenJetsCustom"),
    genBHadJetIndex = cms.InputTag("matchGenBHadron", "genBHadJetIndex"),
    genBHadFlavour = cms.InputTag("matchGenBHadron", "genBHadFlavour"),
    genBHadFromTopWeakDecay = cms.InputTag("matchGenBHadron", "genBHadFromTopWeakDecay"),
    genBHadPlusMothers = cms.InputTag("matchGenBHadron", "genBHadPlusMothers"),
    genBHadPlusMothersIndices = cms.InputTag("matchGenBHadron", "genBHadPlusMothersIndices"),
    genBHadIndex = cms.InputTag("matchGenBHadron", "genBHadIndex"),
    genBHadLeptonHadronIndex = cms.InputTag("matchGenBHadron", "genBHadLeptonHadronIndex"),
    genBHadLeptonViaTau = cms.InputTag("matchGenBHadron", "genBHadLeptonViaTau"),
    genCHadJetIndex = cms.InputTag("matchGenCHadron", "genCHadJetIndex"),
    genCHadFlavour = cms.InputTag("matchGenCHadron", "genCHadFlavour"),
    genCHadFromTopWeakDecay = cms.InputTag("matchGenCHadron", "genCHadFromTopWeakDecay"),
    genCHadBHadronId = cms.InputTag("matchGenCHadron", "genCHadBHadronId"),
)

#process.p = cms.Path(process.printGenParticleList)
process.p = cms.Path(process.hltFilter*process.selectedHadronsAndPartons*process.ak4GenJetsCustom*process.genJetFlavourPlusLeptonInfos*process.matchGenCHadron*process.selectedHadronsAndPartons*process.genJetFlavourPlusLeptonInfos*process.matchGenBHadron*process.egmGsfElectronIDSequence * process.TNT)
#process.p = cms.Path(process.selectedHadronsAndPartons*process.ak4GenJetsCustom*process.genJetFlavourPlusLeptonInfos*process.matchGenCHadron*process.selectedHadronsAndPartons*process.genJetFlavourPlusLeptonInfos*process.matchGenBHadron*process.egmGsfElectronIDSequence * process.TNT)
#process.p = cms.Path(process.TNT)