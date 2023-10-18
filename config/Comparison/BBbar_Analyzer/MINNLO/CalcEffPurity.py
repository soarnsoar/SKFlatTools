#CutStudy__bevt_mm__AtLeast1ElectronInBmatjet__v1p0/belectron_charge/DY
import ROOT
tfile=ROOT.TFile.Open("BBbar_Analyzer_DY.root")
my_path={
    "b_mm_e_charge":"CutStudy__bevt_mm__AtLeast1ElectronInBmatjet__v1p0/belectron_charge/DY",
    "b_ee_m_charge":"CutStudy__bevt_ee__AtLeast1MuonInBmatjet__v1p0/bmuon_charge/DY",
    "bbar_mm_e_charge":"CutStudy__bbar_mm__AtLeast1ElectronInBmatjet__v1p0/belectron_charge/DY",
    "bbar_ee_m_charge":"CutStudy__bbar_ee__AtLeast1MuonInBmatjet__v1p0/bmuon_charge/DY",
}

proto_path={
    "b_mm_e_charge":"ProtoType__bevt_mm__AtLeast1ElectronInBmatjet/belectron_charge/DY",
    "b_ee_m_charge":"ProtoType__bevt_ee__AtLeast1MuonInBmatjet/bmuon_charge/DY",
    "bbar_mm_e_charge":"ProtoType__bbar_mm__AtLeast1ElectronInBmatjet/belectron_charge/DY",
    "bbar_ee_m_charge":"ProtoType__bbar_ee__AtLeast1MuonInBmatjet/bmuon_charge/DY",
}


jetcharge_path={
    "b_mm_e_charge":"NoCutOnLepton__bevt_mm__AtLeast1ElectronInBmatjet/jet_charge/DY",
    "b_ee_m_charge":"NoCutOnLepton__bevt_ee__AtLeast1MuonInBmatjet/jet_charge/DY",
    "bbar_mm_e_charge":"NoCutOnLepton__bbar_mm__AtLeast1ElectronInBmatjet/jet_charge/DY",
    "bbar_ee_m_charge":"NoCutOnLepton__bbar_ee__AtLeast1MuonInBmatjet/jet_charge/DY",
}

def GetEff(hpath,charge):
  h=tfile.Get(hpath)
  xbin0=h.FindBin(0)
  #print "must be zero->",h.GetBinLowEdge(xbin0)
  Nx=h.GetNbinsX()
  plus=h.Integral(xbin0,Nx)
  minus=h.Integral(0,xbin0-1)
  eff=minus/(plus+minus)
  if charge>0:
    eff=1.-eff

  return eff


def GetPurity(hpath1,hpath2,charge):
  h1=tfile.Get(hpath1)
  xbin0=h1.FindBin(0)
  #print "must be zero->",h.GetBinLowEdge(xbin0)
  Nx=h1.GetNbinsX()
  plus1=h1.Integral(xbin0,Nx)
  minus1=h1.Integral(0,xbin0-1)
  h2=tfile.Get(hpath2)
  plus2=h2.Integral(xbin0,Nx)
  minus2=h2.Integral(0,xbin0-1)
  
  if charge>0:
    purity=plus1/(plus1+plus2)
  else:
    purity=minus1/(minus1+minus2)


  return purity


##---Eff
for ch in ["b_mm_e_charge","b_ee_m_charge","bbar_mm_e_charge","bbar_ee_m_charge"]:
  print "--",ch,"--"
  charge=0
  if "bbar" in ch:
    charge=1
  else:
    charge=-1
  print "myeff=",GetEff(my_path[ch],charge)
  print "protoeff=",GetEff(proto_path[ch],charge)
  print "jetcharge_eff=",GetEff(jetcharge_path[ch],charge)

##---Purity
for ch in ["b_mm_e_charge","b_ee_m_charge","bbar_mm_e_charge","bbar_ee_m_charge"]:
  print "--",ch,"--"

  if "b_" in ch:
    ch_opp=ch.replace("b_","bbar_")
  else:
    ch_opp=ch.replace("bbar_","b_")
  charge=0
  if "bbar" in ch:
    charge=1
  else:
    charge=-1
  print "my purity=",GetPurity(my_path[ch],my_path[ch_opp],charge)
  print "proto purity=",GetPurity(proto_path[ch],proto_path[ch_opp],charge)
  print "jetcharge purity=",GetPurity(jetcharge_path[ch],jetcharge_path[ch_opp],charge)
