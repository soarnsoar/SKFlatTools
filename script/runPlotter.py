#!/usr/bin/env python 
from Plotter import Plotter
from glob import glob
if __name__ == '__main__':
    p=Plotter()
    flist=glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/DATA/*.root")+\
    glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/*.root")
    p.GetHistFromFileList(flist)
    
