import ROOT
###-Intro
##---This python class reads root files containing histograms whose path are
## /<cutname>/<variablename>/<processname_suffix>
##---The class will have its own dictionary objects 
##   ->dict_hist[cut][variable][proc]==>histogram obj.
##   ->It will scan all histograms under <>/<>/<> paths
##-<Usage>-
##    fm=FileManager()
##    fm.SetDirPath("BaiscCut/ZCand_Mass")
##    fm.SetFileList(["/data6/Users/jhchoi/SKFlatRunlog/2023_09_07_163518__649621__BasicTest__Era2017__TAMSA1/SingleMuon_periodB/output/hists_14.root"])
##    fm.OpenHist()
##    mydict=fm.ReturnHistDict()



class FileManager:
    def __init__(self):
        #=Open Histogram Files 
        #=and Get the histogram and return them in dictionary form
        self.dict_hist={}
        self.dict_file={}
    def SetFileList(self, _filelist):
        for _path in _filelist:
            self.dict_file[_path]=None
    def OpenHist(self):
        for _path in self.dict_file:
            print "<<<<---Open File->",_path,"--->>>>"
            self.GetHistFromPath(_path)
    def GetHistFromPath(self,_path):
        ##---Scan all histograms
        _f=ROOT.TFile.Open(_path)
        for _ckey in _f.GetListOfKeys():
            _cname=_ckey.GetName()
            if not "TDirectory" in _ckey.GetClassName(): continue ##Check whether the path indicates dir
            _f.cd(_cname)
            #>>Add this cut to dict
            if not _cname in self.dict_hist: self.dict_hist[_cname]={}
            for _vkey in ROOT.gDirectory.GetListOfKeys():
                _vname=_vkey.GetName()
                if not "TDirectory" in _vkey.GetClassName():continue
                #>>Add this variable to dict
                if not _vname in self.dict_hist[_cname]: self.dict_hist[_cname][_vname]={}
                _cvpath=_cname+"/"+_vname
                _f.cd(_cvpath)
                for _hkey in ROOT.gDirectory.GetListOfKeys():
                    _hname=_hkey.GetName()
                    if not "TH" in _hkey.GetClassName() : continue
                    _hpath='/'.join([_cname,_vname,_hname])
                    _h=_f.Get(_hpath)
                    _h.SetDirectory(0)
                    self.dict_hist[_cname][_vname][_hname]=_h
        _f.Close()
    def ReturnHistDict(self):
        return self.dict_hist
if __name__ == '__main__':
    test=FileManager()
    test.SetFileList(["/data6/Users/jhchoi/SKFlatRunlog/2023_09_07_163518__649621__BasicTest__Era2017__TAMSA1/SingleMuon_periodB/output/hists_14.root"])
    test.OpenHist()
    mydict=test.ReturnHistDict()
    #/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/BasicTest/2016preVFP/
    #/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test
    #/data6/Users/jhchoi/SKFlatRunlog/2023_09_07_163518__649621__BasicTest__Era2017__TAMSA1/SingleMuon_periodB/output
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
