dict_conf={
    "nb_in_Bhad_all":{
        "xname":"#of bquark in B hadron(-Bottomness)",
        "yname":"events",
        "numelist":["gbToZb_b/Bhad_nb/DYJets","gbToZb_bbar/Bhad_nb/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb/Bhad_nb/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["all","b event","#bar{b} event"]
    },

    "nb_in_Bhad":{
        "xname":"#of bquark in B hadron(-Bottomness)",
        "yname":"events",
        "numelist":["gbToZb_bbar/Bhad_nb/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/Bhad_nb/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b event","#bar{b} event"]
    },


}
