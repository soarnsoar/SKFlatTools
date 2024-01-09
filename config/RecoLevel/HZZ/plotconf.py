from collections import OrderedDict
from glob import glob
import os
_JHTOOL_MAINDIR = os.getenv('JHTOOL_MAINDIR')

plotconf=OrderedDict()
plotconf['inputpath']=_JHTOOL_MAINDIR+'/config/RecoLevel/HZZ/skflatoutput/combine3yr.root'
plotconf['lumi']='137'
plotconf['sqrtS']='13'
plotconf['doratio']=1
plotconf['outputdir']=_JHTOOL_MAINDIR+'/config/RecoLevel//HZZ/plots/'
#plotconf['rebin']={
#    '4lmass_final':2,
#    '4lmass':2,
#    'HCand_mass':2,
    
#}
plotconf['ignoreNegative']=True
