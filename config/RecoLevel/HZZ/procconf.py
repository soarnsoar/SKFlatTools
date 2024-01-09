from collections import OrderedDict

procconf=OrderedDict()




procconf['EW']={
    'procs':['WZ_pythia','WW_pythia'],
    #'color':100, ##Red
    'color':2, ##Red
    'name':'EW',
}


procconf['V+jets']={
    'procs':['DYJets','WJets_Sherpa'],
    #'procs':['WJets_Sherpa'],
    #'color':79, ##Green
    'color':3, ##Green
    'name':'V+jets',
}

procconf['gg->ZZ^{*},Z#gamma^{*}']={
    'procs':['GluGluToZZto2e2mu',
             'GluGluToZZto4mu',
             'GluGluToZZto4e',],
    #'color':79, ##Green
    'color':5, ##Green
    'name':'gg->ZZ^{*},Z#gamma^{*}',
}

procconf['q#bar{q}->ZZ^{*},Z#gamma^{*}']={
    'procs':['ZZTo4L_powheg','ZGToLLG'],
    #'color':79, ##Green
    'color':4, ##Green
    'name':'q#bar{q}->ZZ^{*},Z#gamma^{*}',
}


procconf['H(125)']={
    'procs':['GluGluHToZZTo4L'],
    'color':6, ##Green
    'name':'H(125)',
}





procconf['Data']={
    'procs':['Data'], ##proc names in histo
    'name':'Data',
    'isData':1,
}

##--TODO : Need isSig
