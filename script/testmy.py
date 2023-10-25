from FileManager import FileManager
from glob import glob
import os
import ROOT
if __name__ == '__main__':
    #/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017
    main_outdir="/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/"
    os.system("mkdir -p plots/")
    f_mc=glob(main_outdir+"/*.root")
    f_data=glob(main_outdir+"/DATA/*.root")
    fm=FileManager()
    fm.SetFileList(f_mc+f_data)
    fm.OpenHist()
    mydict=fm.ReturnHistDict()
    idx=0
    for c in list(mydict):
        for v in list(mydict[c]):
            for h in list(mydict[c][v]):
                print "--histogram ",c,v,h
                can=ROOT.TCanvas()
                _h=mydict[c][v][h]
                _h.Draw()
                can.SaveAs("test"+str(idx)+".pdf")
                idx+=1
