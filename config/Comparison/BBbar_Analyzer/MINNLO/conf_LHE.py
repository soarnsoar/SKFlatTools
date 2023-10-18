dict_conf={
    "x_b_bbar_g":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DY","gbToZb/x_g/DY"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb_bbar/x_b/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[10**-4,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}","gluon"]
    },

    "log_x_b_bbar_g":{
        "xname":"log_{10}(x)",
        "yname":"events",
        "numelist":["gbToZb_b/logx_b/DY","gbToZb/logx_g/DY"],## paths of histograms 
        "color":[1,2,4],
        "deno":"gbToZb_bbar/logx_b/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}","gluon"],
        #"legend":"LT"
    },

    "x_b_bbar":{
        "xname":"x",
        "yname":"events",
        "numelist":["gbToZb_b/x_b/DY"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/x_b/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[10**-4,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}"]
    },

    "log_x_b_bbar":{
        "xname":"log_{10}x",
        "yname":"events",
        "numelist":["gbToZb_b/logx_b/DY"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_bbar/logx_b/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0],
        "names":["b","#bar{b}"],
        #"legend":"LT"
    },

    "Q2":{
        "xname":"Q^{2}",
        "yname":"events",
        "numelist":["gbToZb_bbar/Q2/DY"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/Q2/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        "rebin":[1.,3.,6.,9.,30.,60.,90.,300.,600.,900.,3000.,6000.,9000.,30000.],
        "names":["b event","#bar{b} event"],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0]
    },

    "logQ2":{
        "xname":"log_{10}(Q^{2})",
        "yname":"events",
        "numelist":["gbToZb_bbar/logQ2/DY"],## paths of histograms 
        "color":[2,4],
        "deno":"gbToZb_b/logQ2/DY",
        "setlogx":[False],
        "setlogy":[True,False],
        #"rebin":[1.,3.,6.,9.,30.,60.,90.,300.,600.,900.,3000.,6000.,9000.,30000.],
        "names":["b event","#bar{b} event"],
        #"rebin":[0,10**-3,3*10**-3,10**-2,3*10**-2,10**-1,3*10**-1,10**0]
        #"legend":"LT"
    },

}
