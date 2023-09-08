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
        return _mydict
if __name__ == '__main__':
    p=Plotter()
    
