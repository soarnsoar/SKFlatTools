from collections import OrderedDict

procconf=OrderedDict()



#procconf['QCD']={
#    'procs':["QCD_bEnriched_HT100to200","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700#to1000","QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000"],
#    #'color':79, ##Green
#    'color':9, ##Green
#    'name':'QCD',
#}

#procconf['MultiBoson']={
#    'procs':['WWW','WWZ','WZZ','ZZZ','WWTo2L2Nu_powheg','WZ_pythia','ZZTo2L2Nu_powheg'], ##proc names in histo
#    #'color':79, ##Green
#    'color':8, ##Green
#    'name':'MultiV',
#}



#procconf['h125']={
#    'procs':['GluGluHToWWTo2L2Nu','VBFHToWWTo2L2Nu'], ##proc names in histo
#    #'color':79, ##Green
#    'color':7, ##Green
#    'name':'h125',
#}


procconf['WJets']={
    'procs':['WJets_MG'], ##proc names in histo
    #'color':79, ##Green
    'color':2, ##Green
    'name':'W+jets',
}

procconf['Top']={
    'procs':['TTLL_powheg','TTLJ_powheg','SingleTop_tch_antitop_Incl',\
             'SingleTop_tch_top_Incl',\
             'SingleTop_sch_Lep'], ##proc names in histo
    #'color':100, ##Red
    'color':3, ##Red
    'name':'Top',
}

procconf['DY_others']={
    'procs':['DY_others'], ##proc names in histo
    #'color':94, ##orange
    'color':4, ##orange
    'name':'DY_others',
}
procconf['DY_bbar']={
    'procs':['DY_bbar'], ##proc names in histo
    #'color':94, ##orange
    'color':5, ##orange
    'name':'g+b->Z+#bar{b}',
}

procconf['DY_bevt']={
    'procs':['DY_bevt'], ##proc names in histo
    #'color':94, ##orange
    'color':6, ##orange
    'name':'g+b->Z+b',
}

procconf['DY_bb']={
    'procs':['DY_bb'], ##proc names in histo
    #'color':94, ##orange
    'color':28, ##orange
    'name':'b+#bar{b}->Z+b/#bar{b}',
}


procconf['Data']={
    'procs':['Data'], ##proc names in histo
    'name':'Data',
    'isData':1,
}

##--TODO : Need isSig
