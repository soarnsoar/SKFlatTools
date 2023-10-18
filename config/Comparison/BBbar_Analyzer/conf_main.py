prefix=""
suffix=""

dict_conf={}


for prefix in ["ProtoType__","CutStudy__","NoCutOnMuon__","NoCutOnElectron__"]:
    for suffix in ["_Only1MuonInBmatjet","_AtLeast1MuonInBmatjet","_Only1ElectronInBmatjet","_AtLeast1ElectronInBmatjet"]:

        if "Muon" in prefix and "Electron" in suffix : continue
        if "Electron" in prefix and "Muon" in suffix : continue
        ##--[DONE]skip if prototype && electron channel(not added yet)
        #if "ProtoType" in prefix:
        #    if "Electron" in suffix:continue

        if "Muon"in suffix: 
            lep="muon"
            l="#mu"
            zll="ee"
            zllgreek="ee"
        else:
            lep="electron"
            l="e"        
            zll="mm"
            zllgreek="#mu#mu"

        dict_conf[prefix+lep+"_jet_chargesum_Zee"+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_"+zll+suffix+"/b"+lep+"_bjet_chargesum/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/b"+lep+"_bjet_chargesum/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }
        
        dict_conf[prefix+lep+"charge_Z"+zll+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_"+zll+suffix+"/b"+lep+"_charge/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/b"+lep+"_charge/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }
        
        dict_conf[prefix+"jetcharge_Z"+zll+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_"+zll+suffix+"/jet_charge/DYJets"],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/jet_charge/DYJets",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }

        

#ProtoType__bevt_ee/ptwrtbjet/DYJets
#muonn_ptwrtbjet
for prefix in ["ProtoType__"]:
    suffix="_Muon"
    dict_conf[prefix+"ptwrtbjet"+suffix]={
        "xname":"pT(#mu) w.r.t. jet diction ",
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
for suffix in ["_Muon","_Electron"]:
    if "Muon"in suffix: 
        lep="muon"
        l="#mu"
    else:
        lep="electron"
        l="e"
    dict_conf[prefix+lep+"_P_jetrestf"+suffix]={
        "xname":"pT("+l+") in jet restframe",
        "yname":"events",
        "numelist":[prefix+"bevt_ee"+suffix+"/"+lep+"n_P_jetrestf/DYJets"],## paths of histograms
        "color":[1,2,4],
        "deno":prefix+"bevt_ee"+suffix+"/"+lep+"p_P_jetrestf/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[l+"^{+}, b event in Z->ee",l+"^{-}, bevent in Z->ee"]
    }
    
    dict_conf[prefix+lep+"_dRbmatj"+suffix]={
        "xname":"dR("+l+",bmatjet)",
        "yname":"events",
        "numelist":[prefix+"bevt_ee"+suffix+"/"+lep+"n_dRbmatj/DYJets"],## paths of histograms
        "color":[1,2,4],
        "deno":prefix+"bevt_ee"+suffix+"/"+lep+"p_dRbmatj/DYJets",
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[l+"^{+}, b event in Z->ee",l+"^{-}, bevent in Z->ee"]
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
