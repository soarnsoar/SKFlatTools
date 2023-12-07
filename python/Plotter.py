from FileManager import FileManager

class Plotter:
    def __init__(self):
        ##-----Plotter_----##
        #print "Plotter"
        pass
    def GetHistFromFileList(self,_inputlist):
        _fm=FileManager()
        _fm.SetFileList(_inputlist)
        _fm.OpenHist()
        _mydict=_fm.ReturnHistDict()
        _mydict_short=_fm.ReturnHistDictShort()
        self._inputlist=_inputlist
        return _mydict,_mydict_short

    def GetHistPathFromFilePath(self,_inputpath):
        _fm=FileManager()
        #_fm.SetFileList(_inputlist)
        _fm.SetFilePath(_inputpath)
        _fm.OpenHist()
        _mydict=_fm.ReturnHistDict()
        _mydict_short=_fm.ReturnHistDictShort()
        self._inputpath=_inputpath
        return _mydict,_mydict_short
if __name__ == '__main__':
    p=Plotter()
    
