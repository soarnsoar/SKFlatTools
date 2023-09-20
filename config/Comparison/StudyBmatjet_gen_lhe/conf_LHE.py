dict_conf={
    "x_b_bbar_g":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DYJets","gbToZb/x_g/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb_bbar/x_b/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[10**-4,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}","gluon"]
    },

    "log_x_b_bbar_g":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/logx_b/DYJets","gbToZb/logx_g/DYJets"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb_bbar/logx_b/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}","gluon"]
    },

    "x_b_bbar":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/x_b/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[10**-4,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}"]
    },

    "log_x_b_bbar":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/logx_b/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/logx_b/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}"]
    },

    "Q2":{
        "xname":"Q^{2}",
        "yname":"events",
        "numelist":["gbToZb_bbar/Q2/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/Q2/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[1.,3.,6.,9.,30.,60.,90.,300.,600.,900.,3000.,6000.,9000.,30000.],
        "names":["b event","#bar{b} event"],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0]
    },

    "logQ2":{
        "xname":"Q^{2}",
        "yname":"events",
        "numelist":["gbToZb_bbar/logQ2/DYJets"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/logQ2/DYJets",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[1.,3.,6.,9.,30.,60.,90.,300.,600.,900.,3000.,6000.,9000.,30000.],
        "names":["b event","#bar{b} event"],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0]
    },

}
