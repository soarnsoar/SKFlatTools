import ROOT

class FileManager:
    def __init__(self):
        #=Open Histogram Files 
        #=and Get the histogram and return them in dictionary form
        self.dict_hist={}
        self.dict_file={}
    def SetDirPath(self, _dirpath):
        self.dirpath=_dirpath
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
            _f.cd(_cname)
            #>>Add this cut to dict
            if not _cname in self.dict_hist: self.dict_hist[_cname]={}
            for _vkey in ROOT.gDirectory.GetListOfKeys():
                _vname=_vkey.GetName()
                #>>Add this variable to dict
                if not _vname in self.dict_hist[_cname]: self.dict_hist[_cname][_vname]={}
                _cvpath=_cname+"/"+_vname
                _f.cd(_cvpath)
                for _hkey in ROOT.gDirectory.GetListOfKeys():
                    _hname=_hkey.GetName()
                    _hpath='/'.join([_cname,_vname,_hname])
                    _h=_f.Get(_hpath)
                    _h.SetDirectory(0)
                    self.dict_hist[_cname][_vname][_hname]=_h
        _f.Close()
    def ReturnHistDict(self):
        return self.dict_hist
if __name__ == '__main__':
    test=FileManager()
    test.SetDirPath("BaiscCut/ZCand_Mass")
    test.SetFileList(["/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/hists_6.root"])
    test.OpenHist()
    mydict=test.ReturnHistDict()
    #/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/BasicTest/2016preVFP/
    #/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test
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
