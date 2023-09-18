from Plotter import Plotter
import ROOT
import os
formats=['pdf','png']

#path="/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/B_In_LHE/2017/B_In_LHE_DYJets.root"
path="B_Info_Analyzer_DYJets.root"
p=Plotter()
hdict=p.GetHistFromFileList([path])
canvas=ROOT.TCanvas()
for c in hdict:
    for v in hdict[c]:
        vname=v
        print v
        #if "_B_" in v: 
        #    vname=v.replace("_B_","_Bmeson_")
        #elif v.endswith("_B"):
        #    vname=v.replace("_B","_Bmeson")
        #else:
        #    vname=v
        #print vname
        for p in hdict[c][v]:
            hdict[c][v][p].Draw()
            
            filename="__".join([c,vname,p] )
            
            for f in formats:
                os.system('mkdir -p '+f)
            for f in formats:
                canvas.SaveAs(f+'/'+filename+"."+f)
            for f in formats:
                canvas.SetLogx(1)
                canvas.SaveAs(f+'/'+"logx__"+filename+"."+f)
                canvas.SetLogx(0)
            for f in formats:
                canvas.SetLogy(1)
                canvas.SaveAs(f+'/'+"logy__"+filename+"."+f)
                canvas.SetLogy(0)
            for f in formats:
                canvas.SetLogx(1)
                canvas.SetLogy(1)
                canvas.SaveAs(f+'/'+"logxy__"+filename+"."+f)
                canvas.SetLogx(0)
                canvas.SetLogy(0)
