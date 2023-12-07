from collections import OrderedDict
from glob import glob
import os
_JHTOOL_MAINDIR = os.getenv('JHTOOL_MAINDIR')

plotconf=OrderedDict()
plotconf['inputpath']=_JHTOOL_MAINDIR+'/config/RecoLevel/BBbarReco/23_11/skflatoutput/combine.root'
plotconf['lumi']='41.5'
plotconf['sqrtS']='13'
plotconf['doratio']=1
plotconf['outputdir']=_JHTOOL_MAINDIR+'/config/RecoLevel/BBbarReco/23_11/plots_b_or_bbar/'
