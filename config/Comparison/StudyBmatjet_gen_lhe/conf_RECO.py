dict_conf={
    ##---pT of muon in Bjet.. utilize the Z->ee
    "muon_pt":{
        "xname":"pT(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_pt/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_pt/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["All #mu in Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },
    ##---pT of electron in Bjet.. utilize the Z->mm
    "electron_pt":{
        "xname":"pT(e)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_pt/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_pt/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["all e in Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu"]
    },


    ##--- charge of muon in Bjet for b event OR bbar ,Z->ee 
    "muon_charge_InBmatJet_ee":{
        "xname":"charge(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_bbar_ee/muon_charge/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"LeptonInBmatJet_b_ee/muon_charge/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["dR(#mu,Bmat.Jet)<0.4 in gb->Z->ee","dR(#mu,Bmat.Jet)<0.4 in g#bar{b}->Z->ee"]
    },
    ##---charge of electron in Bjet for b/bbar event , Z->mm
    "electron_charge_InBmatJet_ee":{
        "xname":"charge(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_bbar_mm/electron_charge/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"LeptonInBmatJet_b_mm/electron_charge/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["dR(e,Bmat.Jet)<0.4 in gb->Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in g#bar{b}->Z->#mu#mu"]
    },

    ##--dR(l,bj)
    "muon_dR_bmatj":{
        "xname":"#DeltaR(#mu, B-matched Jet)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_dR_bmatj/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_dR_bmatj/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->ee"]
    },

    "electron_dR_bmatj":{
        "xname":"#DeltaR(e, B-matched Jet)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_dR_bmatj/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_dR_bmatj/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu"]
    },

    ##--dxy
    "muon_dxy":{
        "xname":"dxy(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_dxy/DYJets","LeptonOutOfBmatJet_ee/muon_dxy/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_dxy/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->ee","dR(#mu,Bmat.Jet)>0.4 in Z->ee"]
    },

    "electron_dxy":{
        "xname":"dxy(e)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_dxy/DYJets","LeptonOutOfBmatJet_mm/electron_dxy/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_dxy/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)>0.4 in Z->#mu#mu",],

    },

    ##--dz
    "muon_dz":{
        "xname":"dz(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_dz/DYJets","LeptonOutOfBmatJet_ee/muon_dz/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_dz/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->ee","dR(#mu,Bmat.Jet)>0.4 in Z->ee"]
    },

    "electron_dz":{
        "xname":"dz(e)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_dz/DYJets","LeptonOutOfBmatJet_mm/electron_dz/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_dz/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)>0.4 in Z->#mu#mu"],
    },
    ##--reliso
    "muon_reliso":{
        "xname":"reliso(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_reliso/DYJets","LeptonOutOfBmatJet_ee/muon_reliso/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_reliso/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
         "names":["Z->ee","dR(#mu,Bmat.Jet)<0.4 in Z->ee","dR(#mu,Bmat.Jet)>0.4 in Z->ee"],
    },

    "electron_reliso":{
        "xname":"reliso(e)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_reliso/DYJets","LeptonOutOfBmatJet_mm/electron_reliso/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_reliso/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu","dR(e,Bmat.Jet)<0.4 in Z->#mu#mu","dR(e,Bmat.Jet)>0.4 in Z->#mu#mu"],
    },
    ##--ip3d
    "muon_ip3d":{
        "xname":"ip3d(#mu)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_ee/muon_ip3d/DYJets","LeptonOutOfBmatJet_ee/muon_ip3d/DYJets"],
        "color":[1,2,4],
        "deno":"Lepton_ee/muon_ip3d/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->ee",
                 "dR(#mu,Bmat.Jet)<0.4 in Z->ee",
                 "dR(#mu,Bmat.Jet)>0.4 in Z->ee",
             ]
    },

    "electron_ip3d":{
        "xname":"ip3d(e)",
        "yname":"events",
        "numelist":["LeptonInBmatJet_mm/electron_ip3d/DYJets","LeptonOutOfBmatJet_mm/electron_ip3d/DYJets",],
        "color":[1,2,4],
        "deno":"Lepton_mm/electron_ip3d/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Z->#mu#mu",
                 "dR(e,Bmat.Jet)<0.4 in Z->#mu#mu",
                 "dR(e,Bmat.Jet)>0.4 in Z->#mu#mu",
             ],
    },

    "dR_muon_BmatJet_bevent":{
        "xname":"dR(#mu,B-MatchedJet)",
        "yname":"events",
        "deno":"Lepton_b_ee_lepn/muon_dR_bmatj/DYJets",
        "numelist":["Lepton_b_ee_lepp/muon_dR_bmatj/DYJets",],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["#mu^{+}, bevent, Z->ee","#mu^{-}, bevent, Z->ee"]
    },

    "dR_muon_BmatJet_bbarevent":{
        "xname":"dR(#mu,B-MatchedJet)",
        "yname":"events",
        "deno":"Lepton_bbar_ee_lepn/muon_dR_bmatj/DYJets",
        "numelist":["Lepton_bbar_ee_lepp/muon_dR_bmatj/DYJets",],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["#mu^{+}, #bar{b}event, Z->ee","#mu^{-}, #bar{b}event, Z->ee"]
    },


    ##jet multiplicity
    "jet_chargedMultiplicity":{ ##   bmatjet b vs. bbar
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
        "names":["Not matched jets in Z->#mu#mu", "B-matched jet in b event, Z->#mu#mu", "B-matched jet in #bar{b} event, Z->#mu#mu"],
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
        "names":["Not matched jets in Z->ee", "B-matched jet,b event in Z->ee", "B-matched jet in #bar{b} event, Z->ee"],
    },
    ##
    "jet_muonEnergyFraction":{ ## all jet / bmatjet
        "xname":"jet_muonEnergyFraction",
        "yname":"events",
        "deno":"NotBmatJet_ee/jet_muonEnergyFraction/DYJets",
        "numelist":["BmatJet_ee/jet_muonEnergyFraction/DYJets",],
        "color":[1,2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["Not matched jets, Z->ee", "B-matched jet in b event, Z->ee", "B-matched jet in #bar{b} event, Z->ee"],
    },

    ##jet charge
    "jet_charge":{ ## all jet / bmatjet
        "xname":"jet_charge",
        "yname":"events",
        "deno":"BmatJet_b/jet_charge/DYJets",
        "numelist":["BmatJet_bbar/jet_charge/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet in b event", "B-matched jet in #bar{b} event"],
    },

    ##nmuon_lepp // nmuon_lepn in bevent, Z->ee

    "nmuons":{ ## all jet / bmatjet
        "xname":"# of #mu",
        "yname":"events",
        "deno":"LeptonInBmatJet_b_ee/nmuon_p/DYJets",
        "numelist":["LeptonInBmatJet_b_ee/nmuon_n/DYJets",
                    "LeptonOutOfBmatJet_b_ee/nmuon_p/DYJets",
                    "LeptonOutOfBmatJet_b_ee/nmuon_n/DYJets"],
        "color":[1,2,4,6],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[
            "#mu^{+},dR(#mu,Bmat.Jet)<0.4, bevent, Z->ee",
            "#mu^{-},dR(#mu,Bmat.Jet)<0.4 bevent, Z->ee",
            "#mu^{+},dR(#mu,Bmat.Jet)>0.4, bevent, Z->ee",
            "#mu^{-},dR(#mu,Bmat.Jet)>0.4 bevent, Z->ee",
             ]
    },

    "nelectrons":{ ## all jet / bmatjet
        "xname":"# of #mu",
        "yname":"events",
        "deno":"LeptonInBmatJet_b_mm/nelectron_p/DYJets",
        "numelist":["LeptonInBmatJet_b_mm/nelectron_n/DYJets",
                    "LeptonOutOfBmatJet_b_mm/nelectron_p/DYJets",
                    "LeptonOutOfBmatJet_b_mm/nelectron_n/DYJets"],
        "color":[1,2,4,6],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[
            "e^{+},dR(e,Bmat.Jet)<0.4, bevent, Z->#mu#mu",
            "e^{-},dR(e,Bmat.Jet)<0.4 bevent, Z->#mu#mu",
            "e^{+},dR(e,Bmat.Jet)>0.4, bevent, Z->#mu#mu",
            "e^{-},dR(e,Bmat.Jet)>0.4 bevent, Z->#mu#mu",
             ]
    },

    "nleptons":{ ## all jet / bmatjet
        "xname":"# of #mu",
        "yname":"events",
        "deno":"LeptonInBmatJet_b_mm/nlepton_p/DYJets",
        "numelist":["LeptonInBmatJet_b_mm/nlepton_n/DYJets",
                    "LeptonOutOfBmatJet_b_mm/nlepton_p/DYJets",
                    "LeptonOutOfBmatJet_b_mm/nlepton_n/DYJets"],
        "color":[1,2,4,6],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[
            "l^{+},dR(l,Bmat.Jet)<0.4, bevent",
            "l^{-},dR(l,Bmat.Jet)<0.4 bevent",
            "l^{+},dR(l,Bmat.Jet)>0.4, bevent",
            "l^{-},dR(l,Bmat.Jet)>0.4 bevent",
             ]
    },

    ##deepjet scores
    "DeepJet":{ ## all jet / bmatjet
        "xname":"DeepJet Score",
        "yname":"events",
        "deno":"BmatJet/jet_DeepJet/DYJets",
        "numelist":["NotBmatJet/jet_DeepJet/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet", "Not matched jet"],
    },

    "DeepJet_CvsL":{ ## all jet / bmatjet
        "xname":"DeepJet_CvsL Score",
        "yname":"events",
        "deno":"BmatJet/jet_DeepJet_CvsL/DYJets",
        "numelist":["NotBmatJet/jet_DeepJet_CvsL/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet", "Not matched jet"],
    },

    "DeepJet_CvsB":{ ## all jet / bmatjet
        "xname":"DeepJet_CvsB Score",
        "yname":"events",
        "deno":"BmatJet/jet_DeepJet_CvsB/DYJets",
        "numelist":["NotBmatJet/jet_DeepJet_CvsB/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet", "Not matched jet"],
    },

    ##--by b/bbar
    "DeepJet_bbar":{ ## all jet / bmatjet
        "xname":"DeepJet Score",
        "yname":"events",
        "deno":"BmatJet_b/jet_DeepJet/DYJets",
        "numelist":["BmatJet_bbar/jet_DeepJet/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet, b event", "B-matched jet, #bar{b} event"],
    },

    "DeepJet_CvsL_bbar":{ ## all jet / bmatjet
        "xname":"DeepJet_CvsL Score",
        "yname":"events",
        "deno":"BmatJet_b/jet_DeepJet_CvsL/DYJets",
        "numelist":["BmatJet_bbar/jet_DeepJet_CvsL/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet, b event", "B-matched jet, #bar{b} event"],
    },

    "DeepJet_CvsB_bbar":{ ## all jet / bmatjet
        "xname":"DeepJet_CvsB Score",
        "yname":"events",
        "deno":"BmatJet_b/jet_DeepJet_CvsB/DYJets",
        "numelist":["BmatJet_bbar/jet_DeepJet_CvsB/DYJets"],
        "color":[2,4],
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["B-matched jet, b event", "B-matched jet, #bar{b} event"],
    },
    


}
