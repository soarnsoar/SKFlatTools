prefix=""
suffix=""

dict_conf={}

cutversion="v1p0"
samplename="DY"
for prefix in ["ProtoType__","CutStudy__","NoCutOnLepton__"]:
    for suffix in ["__Only1MuonInBmatjet__"+cutversion,"__AtLeast1MuonInBmatjet__"+cutversion,"__Only1ElectronInBmatjet__"+cutversion,"__AtLeast1ElectronInBmatjet__"+cutversion]:
        if "NoCutOnLepton" in prefix or "ProtoType" in prefix:
            suffix=suffix.rstrip("__"+cutversion)
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
            "numelist":[prefix+"bbar_"+zll+suffix+"/b"+lep+"_bjet_chargesum/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/b"+lep+"_bjet_chargesum/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }
        
        dict_conf[prefix+lep+"charge_Z"+zll+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_"+zll+suffix+"/b"+lep+"_charge/"+samplename+""],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/b"+lep+"_charge/"+samplename+"",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }
        
        dict_conf[prefix+"jetcharge_Z"+zll+suffix]={
            "xname":"Reco. Charge",
            "yname":"events",
            "numelist":[prefix+"bbar_"+zll+suffix+"/jet_charge/"+samplename+""],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+suffix+"/jet_charge/"+samplename+"",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":["b event in Z->"+zllgreek,"#bar{b} event in Z->"+zllgreek]
        }

        

#ProtoType__bevt_ee/ptwrtbjet/"+samplename+"


prefix="ProtoType__"

dict_suffix={
    "Muon":{
        "zll":"ee",
        "zllgreek":"ee",
        "lep":"muon",
        "l":"#mu",
        "Lep":"Muon"
    },
    "Electron":{
        "zll":"mm",
        "zllgreek":"#mu#mu",
        "lep":"electron",
        "l":"e",
        "Lep":"Electron"
    }
}
for suffix in dict_suffix:
    l=dict_suffix[suffix]["l"]
    lep=dict_suffix[suffix]["lep"]
    zll=dict_suffix[suffix]["zll"]
    dict_conf[prefix+"ptwrtbjet_"+suffix]={
        "xname":"pT("+l+") w.r.t. jet diction ",
        "yname":"events",
        "numelist":[prefix+"bevt_"+zll+"_"+suffix+"Minus/"+lep+"_ptwrtbjet/"+samplename],## paths of histograms
        "color":[1,2,4],
        "deno":prefix+"bevt_"+zll+"_"+suffix+"Plus/"+lep+"_ptwrtbjet/"+samplename,
        "setlogx":[False,True],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":[l+"^{+}, b event in Z->"+zllgreek,l+"^{-}, bevent in Z->"+zllgreek]
    }
    
prefix="CutStudy__"
for suffix in dict_suffix:
    l=dict_suffix[suffix]["l"]
    lep=dict_suffix[suffix]["lep"]
    zll=dict_suffix[suffix]["zll"]
    Lep=dict_suffix[suffix]["Lep"]
    for addcut in ["","__dR0p4","__Pjetrest__0p7_3","__dR0p4","__"+cutversion]:
        dict_conf[prefix+"_P_jetrestf_"+suffix+addcut]={
            "xname":"P("+l+") in jet restframe",
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_P_jetrestf/"+samplename+""],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_P_jetrestf/"+samplename+"",
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":[l+"^{+}, b event in Z->"+zllgreek+"",l+"^{-}, bevent in Z->"+zllgreek+""]
        }
        
        dict_conf[prefix+lep+"_dRbmatj_"+suffix+addcut]={
            "xname":"dR("+l+",bmatjet)",
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_dRbmatj/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_dRbmatj/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
        }

        ##muon_ip3d
        x="ip3d"
        xtitle="ip3d"
        dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
            "xname":xtitle,
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
        }
        ##nsip3d
        x="nsip3d"
        xtitle="nsip3d"
        dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
            "xname":xtitle,
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            "rebin":[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10],
            "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
        }
        ##logreliso
        x="logreliso"
        xtitle="log(reliso)"
        dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
            "xname":xtitle,
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
        }


        ##logreltrkiso
        x="logreltrkiso"
        xtitle="log(reltrkiso)"
        dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
            "xname":xtitle,
            "yname":"events",
            "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
            "color":[1,2,4],
            "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
            "setlogx":[False,True],
            "setlogy":[True,False],
            #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
            "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
        }

        ##--only for electron
        if lep=="electron":
            x="logrelecalclusteriso"
            xtitle="log(rel_ecal_cluster_iso)"
            dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
                "xname":xtitle,
                "yname":"events",
                "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
                "color":[1,2,4],
                "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
                "setlogx":[False,True],
                "setlogy":[True,False],
                #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
                "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
            }

            x="IsGsfCtfScPixChargeConsistent"
            xtitle="IsGsfCtfScPixChargeConsistent"
            dict_conf[prefix+lep+"_"+x+"_"+suffix+addcut]={
                "xname":xtitle,
                "yname":"events",
                "numelist":[prefix+"bevt_"+zll+"_"+Lep+"Minus"+addcut+"/"+lep+"_"+x+"/"+samplename],## paths of histograms
                "color":[1,2,4],
                "deno":prefix+"bevt_"+zll+"_"+Lep+"Plus"+addcut+"/"+lep+"_"+x+"/"+samplename,
                "setlogx":[False,True],
                "setlogy":[True,False],
                #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
                "names":[l+"^{+}, b event in Z->"+zll+"",l+"^{-}, bevent in Z->"+zll+""]
            }

