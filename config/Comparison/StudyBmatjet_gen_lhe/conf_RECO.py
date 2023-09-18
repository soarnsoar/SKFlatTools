dict_conf={
    "muon_pt":{
        "xname":"pT(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_pt/DYJets","InBmatJet_ee/muon_pt/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb/muon_pt/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["all","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },
    "electron_pt":{
        "xname":"pT(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_pt/DYJets","InBmatJet_ee/electron_pt/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb/electron_pt/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["all","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },


    ##--dR(l,bj)
    "muon_dR_bmatj":{
        "xname":"#DeltaR(#m,u B-matched Jet)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_dR_bmatj/DYJets","InBmatJet_ee/muon_dR_bmatj/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_ee/muon_dR_bmatj/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },
    "electron_dR_bmatj":{
        "xname":"#DeltaR(e, B-matched Jet)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_dR_bmatj/DYJets","InBmatJet_ee/electron_dR_bmatj/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_mm/electron_dR_bmatj/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"]
    },
    ##--dxy
    "muon_dxy":{
        "xname":"dxy(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_dxy/DYJets","InBmatJet_ee/muon_dxy/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_ee/muon_dxy/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_dxy":{
        "xname":"dxy(e)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_dxy/DYJets","InBmatJet_ee/electron_dxy/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_mm/electron_dxy/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"]

    },

    ##--dz
    "muon_dz":{
        "xname":"dz(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_dz/DYJets","InBmatJet_ee/muon_dz/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_ee/muon_dz/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_dz":{
        "xname":"dz(e)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_dz/DYJets","InBmatJet_ee/electron_dz/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_mm/electron_dz/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"]
    },
    ##--reliso
    "muon_reliso":{
        "xname":"reliso(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_reliso/DYJets","InBmatJet_ee/muon_reliso/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_ee/muon_reliso/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
         "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_reliso":{
        "xname":"reliso(e)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_reliso/DYJets","InBmatJet_ee/electron_reliso/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_mm/electron_reliso/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"]
    },
    ##--ip3d
    "muon_ip3d":{
        "xname":"ip3d(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_ip3d/DYJets","InBmatJet_ee/muon_ip3d/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_ee/muon_ip3d/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_ip3d":{
        "xname":"ip3d(e)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_ip3d/DYJets","InBmatJet_ee/electron_ip3d/DYJets"],
        "color":[1,2,4],
        "deno":"gbToZb_mm/electron_ip3d/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"] 
    },
    ##--charge of lepton
    "muon_charge":{
        "xname":"charge(#mu)",
        "yname":"events",
        "numelist":["InBmatJet_mm/muon_charge/DYJets","InBmatJet_ee/muon_charge/DYJets"],
        "color":[1,2,4],
        "deno":"InBmatJet/muon_charge/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["dR(#mu,Bmat.Jet)<0.4","dR(#mu,Bmat.Jet)<0.4 in Z->#mu#mu","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_charge":{
        "xname":"charge(e)",
        "yname":"events",
        "numelist":["InBmatJet_mm/electron_charge/DYJets","InBmatJet_ee/electron_charge/DYJets"],
        "color":[1,2,4],
        "deno":"InBmatJet/electron_charge/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["dR(e,Bmat.Jet)<0.4","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->ee"]
    },


    "nmuon":{
        "xname":"# of #mu",
        "yname":"events",
        "numelist":["gbToZb_mm/nmuon/DYJets",],
        "color":[2,4],
        "deno":"gbToZb_ee/nmuon/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","Z->#mu#mu"]
    },

    "nelectron":{
        "xname":"# of e",
        "yname":"events",
        "numelist":["gbToZb_mm/nelectron/DYJets",],
        "color":[2,4],
        "deno":"gbToZb_ee/nelectron/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","Z->#mu#mu"]
    },

    "dR":{
        "xname":"dR",
        "yname":"events",
        "deno":"BmatJet/dRToBhad/DYJets",
        "numelist":["BmatJet/dRToLHE/DYJets",],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["dR(B-MatchedJet, B hadron@GEN)","dR(B-MatchedJet, bquark@ME)"],
    },

    "ptratio":{
        "xname":"pT Ratio",
        "yname":"events",
        "deno":"BmatJet/ptratioToBhad/DYJets",
        "numelist":["BmatJet/ptratioToLHE/DYJets",],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-MatchedJetB/hadron@GEN","B-MatchedJet/bquark@ME"],
    },

    ##jet multiplicity
    "jet_chargedMultiplicity":{ ## all jet / bmatjet
        "xname":"jet_chargedMultiplicity",
        "yname":"events",
        "deno":"NotBmatJet/jet_chargedMultiplicity/DYJets",
        "numelist":["BmatJet_b/jet_chargedMultiplicity/DYJets","BmatJet_bbar/jet_chargedMultiplicity/DYJets"],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_neutralMultiplicity":{ ## all jet / bmatjet
        "xname":"jet_neutralMultiplicity",
        "yname":"events",
        "deno":"NotBmatJet/jet_neutralMultiplicity/DYJets",
        "numelist":["BmatJet_b/jet_neutralMultiplicity/DYJets","BmatJet_bbar/jet_neutralMultiplicity/DYJets"],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    ##
    "jet_chargedHadronEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_chargedHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet/jet_chargedHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b/jet_chargedHadronEnergyFraction/DYJets","BmatJet_bbar/jet_chargedHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    "jet_chargedHadronEnergyFraction_mm":{ ## all jet / bmatjet
        "xname":"jet_chargedHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_mm/jet_chargedHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b_mm/jet_chargedHadronEnergyFraction/DYJets","BmatJet_bbar_mm/jet_chargedHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    "jet_chargedHadronEnergyFraction_ee":{ ## all jet / bmatjet
        "xname":"jet_chargedHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_chargedHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b_ee/jet_chargedHadronEnergyFraction/DYJets","BmatJet_bbar_ee/jet_chargedHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    ##
    "jet_neutralHadronEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_neutralHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet/jet_neutralHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b/jet_neutralHadronEnergyFraction/DYJets","BmatJet_bbar/jet_neutralHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_neutralHadronEnergyFraction_mm":{ ## all jet / bmatjet
        "xname":"jet_neutralHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_mm/jet_neutralHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b_mm/jet_neutralHadronEnergyFraction/DYJets","BmatJet_bbar_mm/jet_neutralHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_neutralHadronEnergyFraction_ee":{ ## all jet / bmatjet
        "xname":"jet_neutralHadronEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_neutralHadronEnergyFraction/DYJets",
        "numelist":["BmatJet_b_ee/jet_neutralHadronEnergyFraction/DYJets","BmatJet_bbar_ee/jet_neutralHadronEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    ##
    "jet_neutralEmEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_neutralEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet/jet_neutralEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b/jet_neutralEmEnergyFraction/DYJets","BmatJet_bbar/jet_neutralEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_neutralEmEnergyFraction_mm":{ ## all jet / bmatjet
        "xname":"jet_neutralEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_mm/jet_neutralEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b_mm/jet_neutralEmEnergyFraction/DYJets","BmatJet_bbar_mm/jet_neutralEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_neutralEmEnergyFraction_ee":{ ## all jet / bmatjet
        "xname":"jet_neutralEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_neutralEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b_ee/jet_neutralEmEnergyFraction/DYJets","BmatJet_bbar_ee/jet_neutralEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    ##
    "jet_chargedEmEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_chargedEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet/jet_chargedEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b/jet_chargedEmEnergyFraction/DYJets","BmatJet_bbar/jet_chargedEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_chargedEmEnergyFraction_mm":{ ## all jet / bmatjet
        "xname":"jet_chargedEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_mm/jet_chargedEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b_mm/jet_chargedEmEnergyFraction/DYJets","BmatJet_bbar_mm/jet_chargedEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_chargedEmEnergyFraction_ee":{ ## all jet / bmatjet
        "xname":"jet_chargedEmEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_chargedEmEnergyFraction/DYJets",
        "numelist":["BmatJet_b_ee/jet_chargedEmEnergyFraction/DYJets","BmatJet_bbar_ee/jet_chargedEmEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    ##
    "jet_muonEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_muonEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet/jet_muonEnergyFraction/DYJets",
        "numelist":["BmatJet_b/jet_muonEnergyFraction/DYJets","BmatJet_bbar/jet_muonEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    "jet_muonEnergyFraction_mm":{ ## all jet / bmatjet
        "xname":"jet_muonEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_mm/jet_muonEnergyFraction/DYJets",
        "numelist":["BmatJet_b_mm/jet_muonEnergyFraction/DYJets","BmatJet_bbar_mm/jet_muonEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    "jet_muonEnergyFraction_ee":{ ## all jet / bmatjet
        "xname":"jet_muonEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_muonEnergyFraction/DYJets",
        "numelist":["BmatJet_b_ee/jet_muonEnergyFraction/DYJets","BmatJet_bbar_ee/jet_muonEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets", "B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },
    


}
