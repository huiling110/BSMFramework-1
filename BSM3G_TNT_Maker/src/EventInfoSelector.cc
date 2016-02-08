#include "BSMFramework/BSM3G_TNT_Maker/interface/EventInfoSelector.h"
EventInfoSelector::EventInfoSelector(std::string name, TTree* tree, bool debug, const pset& iConfig, edm::ConsumesCollector && ic):
  baseTree(name,tree,debug)
{
  genEvtInfo_    = ic.consumes<GenEventInfoProduct>(edm::InputTag("generator"));
  rhopogHandle_  = ic.consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"));
  rhotthHandle_  = ic.consumes<double>(edm::InputTag("fixedGridRhoFastjetCentralNeutral"));
  metFilterBits_ = ic.consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("metFilterBits"));
  _is_data = iConfig.getParameter<bool>("is_data");
  if(debug) std::cout<<"in EventInfoSelector constructor"<<std::endl;
  SetBranches();
}
EventInfoSelector::~EventInfoSelector(){
  delete tree_;
}
void EventInfoSelector::Fill(const edm::Event& iEvent){
  Initialise();
  //Event quantities
  EVENT_event_     = iEvent.id().event();
  EVENT_run_       = iEvent.id().run();
  EVENT_lumiBlock_ = iEvent.id().luminosityBlock();
  EVENT_genWeight_ = 1;
  edm::Handle<GenEventInfoProduct> genEvtInfo;
  iEvent.getByToken(genEvtInfo_,genEvtInfo);
  if(!_is_data){
    EVENT_genWeight_ = genEvtInfo->weight();
  }
  edm::Handle<double> rhopogHandle;
  iEvent.getByToken(rhopogHandle_,rhopogHandle);
  double rhopog = *rhopogHandle;
  edm::Handle<double> rhotthHandle;
  iEvent.getByToken(rhotthHandle_,rhotthHandle);
  double rhotth = *rhotthHandle;
  EVENT_rhopog_ = rhopog;
  EVENT_rhotth_ = rhotth;
  //Event filters
  edm::Handle<edm::TriggerResults> metFilterBits;
  iEvent.getByToken(metFilterBits_, metFilterBits);
  const edm::TriggerNames &metNames = iEvent.triggerNames(*metFilterBits);
  for(unsigned int i = 0, n = metFilterBits->size(); i < n; ++i){ 
    if(metNames.triggerName(i)=="Flag_HBHENoiseFilter")                    Flag_HBHENoiseFilter                    = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_HBHENoiseIsoFilter")                 Flag_HBHENoiseIsoFilter                 = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_CSCTightHaloFilter")                 Flag_CSCTightHaloFilter                 = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_CSCTightHaloTrkMuUnvetoFilter")      Flag_CSCTightHaloTrkMuUnvetoFilter      = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_CSCTightHalo2015Filter")             Flag_CSCTightHalo2015Filter             = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_HcalStripHaloFilter")                Flag_HcalStripHaloFilter                = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_hcalLaserEventFilter")               Flag_hcalLaserEventFilter               = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_EcalDeadCellTriggerPrimitiveFilter") Flag_EcalDeadCellTriggerPrimitiveFilter = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_EcalDeadCellBoundaryEnergyFilter")   Flag_EcalDeadCellBoundaryEnergyFilter   = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_goodVertices")                       Flag_goodVertices                       = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_eeBadScFilter")                      Flag_eeBadScFilter                      = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_ecalLaserCorrFilter")                Flag_ecalLaserCorrFilter                = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_trkPOGFilters")                      Flag_trkPOGFilters                      = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_chargedHadronTrackResolutionFilter") Flag_chargedHadronTrackResolutionFilter = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_muonBadTrackFilter")                 Flag_muonBadTrackFilter                 = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_trkPOG_manystripclus53X")            Flag_trkPOG_manystripclus53X            = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_trkPOG_toomanystripclus53X")         Flag_trkPOG_toomanystripclus53X         = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_trkPOG_logErrorTooManyClusters")     Flag_trkPOG_logErrorTooManyClusters     = metFilterBits->accept(i);
    if(metNames.triggerName(i)=="Flag_METFilters")                         Flag_METFilters                         = metFilterBits->accept(i);
  } //loop over met filters
}
void EventInfoSelector::SetBranches(){
  if(debug_) std::cout<<"setting branches: calling AddBranch of baseTree"<<std::endl;
  //Event quantities
  AddBranch(&EVENT_event_     ,"EVENT_event");
  AddBranch(&EVENT_run_       ,"EVENT_run");
  AddBranch(&EVENT_lumiBlock_ ,"EVENT_lumiBlock");
  AddBranch(&EVENT_genWeight_ ,"EVENT_genWeight");
  AddBranch(&EVENT_rhopog_    ,"EVENT_rhopog");
  AddBranch(&EVENT_rhotth_    ,"EVENT_rhotth");
  //Event filters
  AddBranch(&Flag_HBHENoiseFilter                    ,"Flag_HBHENoiseFilter");
  AddBranch(&Flag_HBHENoiseIsoFilter                 ,"Flag_HBHENoiseIsoFilter");
  AddBranch(&Flag_CSCTightHaloFilter                 ,"Flag_CSCTightHaloFilter");
  AddBranch(&Flag_CSCTightHaloTrkMuUnvetoFilter      ,"Flag_CSCTightHaloTrkMuUnvetoFilter");
  AddBranch(&Flag_CSCTightHalo2015Filter             ,"Flag_CSCTightHalo2015Filter");
  AddBranch(&Flag_HcalStripHaloFilter                ,"Flag_HcalStripHaloFilter");
  AddBranch(&Flag_hcalLaserEventFilter               ,"Flag_hcalLaserEventFilter");
  AddBranch(&Flag_EcalDeadCellTriggerPrimitiveFilter ,"Flag_EcalDeadCellTriggerPrimitiveFilter");
  AddBranch(&Flag_EcalDeadCellBoundaryEnergyFilter   ,"Flag_EcalDeadCellBoundaryEnergyFilter");
  AddBranch(&Flag_goodVertices                       ,"Flag_goodVertices");
  AddBranch(&Flag_eeBadScFilter                      ,"Flag_eeBadScFilter");
  AddBranch(&Flag_ecalLaserCorrFilter                ,"Flag_ecalLaserCorrFilter");
  AddBranch(&Flag_trkPOGFilters                      ,"Flag_trkPOGFilters");
  AddBranch(&Flag_chargedHadronTrackResolutionFilter ,"Flag_chargedHadronTrackResolutionFilter");
  AddBranch(&Flag_muonBadTrackFilter                 ,"Flag_muonBadTrackFilter");
  AddBranch(&Flag_trkPOG_manystripclus53X            ,"Flag_trkPOG_manystripclus53X");
  AddBranch(&Flag_trkPOG_toomanystripclus53X         ,"Flag_trkPOG_toomanystripclus53X");
  AddBranch(&Flag_trkPOG_logErrorTooManyClusters     ,"Flag_trkPOG_logErrorTooManyClusters");
  AddBranch(&Flag_METFilters                         ,"Flag_METFilters");
}
void EventInfoSelector::Initialise(){
  //Event quantities
  EVENT_event_      = -9999;
  EVENT_run_        = -9999; 
  EVENT_lumiBlock_  = -9999;
  EVENT_genWeight_  = -9999;
  EVENT_rhopog_     = -9999;
  EVENT_rhotth_     = -9999; 
  //Event filters
  Flag_HBHENoiseFilter                    = -9999;
  Flag_HBHENoiseIsoFilter                 = -9999;
  Flag_CSCTightHaloFilter                 = -9999;
  Flag_CSCTightHaloTrkMuUnvetoFilter      = -9999;
  Flag_CSCTightHalo2015Filter             = -9999;
  Flag_HcalStripHaloFilter                = -9999;
  Flag_hcalLaserEventFilter               = -9999;
  Flag_EcalDeadCellTriggerPrimitiveFilter = -9999;
  Flag_EcalDeadCellBoundaryEnergyFilter   = -9999;
  Flag_goodVertices                       = -9999;
  Flag_eeBadScFilter                      = -9999;
  Flag_ecalLaserCorrFilter                = -9999;
  Flag_trkPOGFilters                      = -9999;
  Flag_chargedHadronTrackResolutionFilter = -9999;
  Flag_muonBadTrackFilter                 = -9999;
  Flag_trkPOG_manystripclus53X            = -9999;
  Flag_trkPOG_toomanystripclus53X         = -9999;
  Flag_trkPOG_logErrorTooManyClusters     = -9999;
  Flag_METFilters                         = -9999;
}
