dict_conf={
    "x_b_bbar_g":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DYJets","gbToZb/x_g/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/x_b/DYJets",
        "setlogx":[True,False],
        "setlogy":[True,False],
        "rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}","gluon"]
    },

    "x_b_bbar":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/x_b/DYJets",
        "setlogx":[True,False],
        "setlogy":[True,False],
        "rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}"]
    },

    "Q":{
        "xname":"Q^{2}",
        "yname":"events",
        "numelist":["gbToZb_bbar/Q2/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/Q2/DYJets",
        "setlogx":[True,False],
        "setlogy":[True,False],
        "names":["b event","#bar{b} event"]
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0]
    },

}
