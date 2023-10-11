prefix=""
suffix=""

dict_conf={}


for prefix in ["ProtoType__","CutStudy__","NoCutOnMuon__"]:
    for suffix in ["_Only1MuonInBmatjet","_AtLeast1MuonInBmatjet"]:
        
        dict_conf[prefix+"muon_jet_chargesum_Zee"+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_ee"+suffix+"/bmuon_bjet_chargesum/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_ee"+suffix+"/bmuon_bjet_chargesum/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->ee","#bar{b} event in Z->ee"]
        }
        
        dict_conf[prefix+"muoncharge_Zee"+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_ee"+suffix+"/bmuon_charge/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_ee"+suffix+"/bmuon_charge/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->ee","#bar{b} event in Z->ee"]
        }
        
        dict_conf[prefix+"jetcharge_Zee"+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_ee"+suffix+"/jet_charge/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_ee"+suffix+"/jet_charge/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->ee","#bar{b} event in Z->ee"]
        }

        

#ProtoType__bevt_ee/ptwrtbjet/DYJets
#muonn_ptwrtbjet
prefix="ProtoType__"
suffix="_Muon"
dict_conf[prefix+"ptwrtbjet"+suffix]={
    "xname":"pT(#mu) in jet restframe",
    "yname":"events",
    "numelist":[prefix+"bevt_ee"+suffix+"/muonn_ptwrtbjet/DYJets"],## paths of histograms
    "color":[1,2,4],
    "deno":prefix+"bevt_ee"+suffix+"/muonp_ptwrtbjet/DYJets",
    "setlogx":[False,True],
    "setlogy":[True,False],
    #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
    "names":["#mu^{+}, b event in Z->ee","#mu^{-}, bevent in Z->ee"]
}

prefix="CutStudy__"
suffix="_Muon"
dict_conf[prefix+"muon_P_jetrestf"+suffix]={
    "xname":"pT(#mu) in jet restframe",
    "yname":"events",
    "numelist":[prefix+"bevt_ee"+suffix+"/muonn_P_jetrestf/DYJets"],## paths of histograms
    "color":[1,2,4],
    "deno":prefix+"bevt_ee"+suffix+"/muonp_P_jetrestf/DYJets",
    "setlogx":[False,True],
    "setlogy":[True,False],
    #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
    "names":["#mu^{+}, b event in Z->ee","#mu^{-}, bevent in Z->ee"]
}

dict_conf[prefix+"muon_dRbmatj"+suffix]={
    "xname":"dR(#mu,bmatjet)",
    "yname":"events",
    "numelist":[prefix+"bevt_ee"+suffix+"/muonn_dRbmatj/DYJets"],## paths of histograms
    "color":[1,2,4],
    "deno":prefix+"bevt_ee"+suffix+"/muonp_dRbmatj/DYJets",
    "setlogx":[False,True],
    "setlogy":[True,False],
    #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
    "names":["#mu^{+}, b event in Z->ee","#mu^{-}, bevent in Z->ee"]
}

suffix="_MuonPjetrestf_0p7_2p5"
#CutStudy__bevt_ee_MuonPjetrestf_0p7_2p5/muonn_dRbmatj
dict_conf[prefix+"muon_dRbmatj"+suffix]={
    "xname":"dR(#mu,bmatjet)",
    "yname":"events",
    "numelist":[prefix+"bevt_ee"+suffix+"/muonn_dRbmatj/DYJets"],## paths of histograms
    "color":[1,2,4],
    "deno":prefix+"bevt_ee"+suffix+"/muonp_dRbmatj/DYJets",
    "setlogx":[False,True],
    "setlogy":[True,False],
    #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
    "names":["#mu^{+}, b event in Z->ee","#mu^{-}, bevent in Z->ee"]
}


suffix="_MuonInBmatjet0p5"
dict_conf[prefix+"muon_P_jetrestf"+suffix]={
    "xname":"dR(#mu,bmatjet)",
    "yname":"events",
    "numelist":[prefix+"bevt_ee"+suffix+"/muonn_P_jetrestf/DYJets"],## paths of histograms
    "color":[1,2,4],
    "deno":prefix+"bevt_ee"+suffix+"/muonp_P_jetrestf/DYJets",
    "setlogx":[False,True],
    "setlogy":[True,False],
    #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
    "names":["#mu^{+}, b event in Z->ee","#mu^{-}, bevent in Z->ee"]
}
