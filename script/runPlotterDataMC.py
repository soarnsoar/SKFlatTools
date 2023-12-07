#!/usr/bin/env python 
##====================
##TODO : ratio pad / legend
##
##===================
from Plotter import Plotter
from glob import glob
import CMS_lumi, tdrstyle
import array
import ROOT
import argparse
import sys
import numpy as np
import os
from copy import deepcopy
from collections import OrderedDict
import os, psutil
process = psutil.Process()
print(process.memory_info().rss)  # in bytes 


class Drawer:
    def SetHistDict(self,_hdict):
        self.hdict=_hdict ##container of histogram-objects
    def SetProcDict(self,_pdict):
        self.pdict=_pdict ##process info
    def SetInputpath(self,_inputpath):
        self.inputpath=_inputpath
    def init(self,title,prefix,variablename):
        self.tfile=ROOT.TFile.Open(self.inputpath)
        self.ymin=sys.maxsize
        self.ymax=-sys.maxsize
        self.xbins=[]
        self.SetNames(title,prefix,variablename)
        self.SetSubprocs()
        self.DefineLegend()
        self.InitEmptyHists()
        self.CombineHist()
        self.SetMinMaxBins()
        self.GetRatio1Line()
        self.DefineLegend()

    def SetSubprocs(self):
        #procs
        self.subplist=[]
        for p in self.pdict:
            _subplist=self.pdict[p]['procs']
            self.subplist+=_subplist
        self.subplist=list(set(self.subplist))
    def InitEmptyHists(self):
        first=list(self.hdict)[0]
        self.hempty=self.tfile.Get(self.hdict[first]).Clone("empty")
        self.hempty.Reset()
        for subp in self.subplist:
            if not (subp in self.hdict):
                self.hdict[subp]=self.hempty.Clone()
    def DefineLegend(self):
        #TLegend (Double_t x1, Double_t y1, Double_t x2, Double_t y2, const char *header="", Option_t *option="brNDC")
        nproc=len(self.pdict)
        ncolomns=(nproc-1)/4 +1
        x1=0.35
        x2=0.35+0.2*ncolomns
        y1=0.65
        y2=0.85

        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetNColumns(ncolomns)
    def AddEntryLeg(self):
        for p in reversed(self.pdict):
            self.leg.AddEntry(self.chdict[p],p)
    def CombineHist(self):
        
        ##---Combine Histos
        self.chdict=OrderedDict()
        self.hmc=self.hempty.Clone("hmc")
        self.hdata=self.hempty.Clone("hdata")
        self.hratio=self.hempty.Clone("hratio")
        self.hstack=ROOT.THStack("hstack","hstack")

        for p in self.pdict:
            self.chdict[p]=self.hempty.Clone()
            for subp in self.pdict[p]['procs']: ## subp=TTLL TTLJ will be combined to TTtotal
                #print "self.tfile.Get(self.hdict[subp])",type(self.tfile.Get(self.hdict[subp]))

                if not "TH1D" in str(type(self.tfile.Get(self.hdict[subp]))) : continue
                self.chdict[p].Add(self.tfile.Get(self.hdict[subp]))
                
            #self.leg.AddEntry(self.chdict[p],p)
        ##---Stack Histos

        for p in self.pdict:
            ##--Set data histo
            if 'isData' in self.pdict[p]:
                if self.pdict[p]['isData']: 
                    self.hdata=self.chdict[p]
                    continue
            else:
                self.hmc.Add(self.chdict[p])
                self.chdict[p].SetFillColor(self.pdict[p]['color'])
                self.chdict[p].SetLineColor(self.pdict[p]['color'])
                self.chdict[p].SetMarkerColor(self.pdict[p]['color'])
                self.hstack.Add(self.chdict[p])







    def SetMinMaxBins(self):
        
        _id=0
        for p in self.chdict:
            if _id==0: 
                for i in range(1,self.chdict[p].GetXaxis().GetNbins()+2):
                    _BinLowEdge=self.chdict[p].GetXaxis().GetBinLowEdge(i)
                    self.xbins.append(_BinLowEdge)
            ymin_=self.chdict[p].GetMinimum()
            ymax_=self.chdict[p].GetMaximum()
            if ymin_<self.ymin:self.ymin=ymin_
            if ymax_>self.ymax:self.ymax=ymax_
            _id+=1
        
        
        for _h in [self.hmc,self.hdata]:
            ymin_=_h.GetMinimum()
            ymax_=_h.GetMaximum()
            if ymin_<self.ymin:self.ymin=ymin_
            if ymax_>self.ymax:self.ymax=ymax_
        self.xbins=np.array(self.xbins)
    def GetRatio1Line(self):
        #TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        x1=self.xbins[1]
        x2=self.xbins[-1]
        y1=1
        y2=1
        self.line1=ROOT.TLine(x1,y1,x2,y2)
        self.line1.SetLineStyle(2)
    def SetNames(self,title,prefix,xname,yname='Events'):
        self.title=title
        self.xname=xname
        self.yname=yname
        self.prefix=prefix
    def SetPlotConfig(self,_conf):
        self.plotconf=_conf
        self.outputdir=self.plotconf['outputdir']
        self.lumi=self.plotconf['lumi']
        self.sqrtS=self.plotconf['sqrtS']
        os.system('mkdir -p '+self.outputdir)
        os.system('mkdir -p '+self.outputdir+"/ratio/")
        os.system('mkdir -p '+self.outputdir+"/logy/")
        os.system('mkdir -p '+self.outputdir+"/ratio_logy/")

    def SetMaxY(self,coeff=2.):
        self.hdata.SetMaximum(self.ymax*coeff)
        self.hmc.SetMaximum(self.ymax*coeff)
        self.hstack.SetMaximum(self.ymax*coeff)
    def run(self):
        self.SetMaxY()
        ##---------From TDR style ---------##
        tdrstyle.setTDRStyle()
        #change the CMS_lumi variables (see CMS_lumi.py)
        CMS_lumi.lumi_13TeV = self.lumi+" fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = self.sqrtS # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
        iPos = 11
        CMS_lumi.relPosX    = 0.08
        if( iPos==0 ): CMS_lumi.relPosX = 0.12
        
        H_ref = 600; 
        W_ref = 800; 
        W = W_ref
        H  = H_ref
        # 
        # Simple example of macro: plot with CMS name and lumi text
        #  (this script does not pretend to work in all configurations)
        # iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
        # For instance: 
        #               iPeriod = 3 means: 7 TeV + 8 TeV
        #               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
        #               iPeriod = 0 means: free form (uses lumi_sqrtS)
        # Initiated by: Gautier Hamel de Monchenault (Saclay)
        # Translated in Python by: Joshua Hardenbrook (Princeton)
        # Updated by:   Dinko Ferencek (Rutgers)
        #
    
        iPeriod = 4
        
        # references for T, B, L, R
        T = 0.08*H_ref
        B = 0.12*H_ref 
        L = 0.12*W_ref
        R = 0.04*W_ref
        
        self.canvas = ROOT.TCanvas(self.prefix+'__'+self.xname,self.prefix+'__'+self.xname,50,50,W,H)
        self.canvas.SetFillColor(0)
        self.canvas.SetBorderMode(0)
        self.canvas.SetFrameFillStyle(0)
        self.canvas.SetFrameBorderMode(0)
        self.canvas.SetLeftMargin( L/W )
        self.canvas.SetRightMargin( R/W )
        self.canvas.SetTopMargin( T/H )
        self.canvas.SetBottomMargin( B/H )
        self.canvas.SetTickx(0)
        self.canvas.SetTicky(0)
        

        self.hdata.SetMarkerStyle(8)
        self.hdata.SetMarkerSize(0.5)
        
        self.hstack.Draw('hist')
        self.hdata.Draw('E1sames')
        self.AddEntryLeg()
        self.leg.Draw()
        CMS_lumi.CMS_lumi(self.canvas, iPeriod, iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
        self.canvas.SaveAs(self.outputdir+'/c__'+self.prefix+"__"+self.xname+".pdf")
        self.canvas.SetLogy()
        self.SetMaxY(1000)
        self.canvas.SaveAs(self.outputdir+'/logy/clogy__'+self.prefix+"__"+self.xname+".pdf")
        self.canvas.SetLogy(0)
        ##--ratioplot
        self.hratio=self.hdata.Clone("hratio")
        self.hratio.Divide(self.hmc)
        
        self.pad1=ROOT.TPad("self.pad1", "self.pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        self.pad1.SetTopMargin(0.1)
        self.pad1.SetBottomMargin(0.02)
        self.pad1.SetGridx()
        self.pad1.Draw()
        self.pad1.cd()
        self.hstack.Draw('hist')
        self.hdata.Draw('E1sames')
        self.leg.Draw()
        self.canvas.cd()
        self.pad2=ROOT.TPad("self.pad2", "self.pad2", 0, 0.0, 1, 0.3)
        self.pad2.SetTopMargin(0.02)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridx()
        self.pad2.Draw()
        self.pad2.cd()
        ##TODO::handle this with input args
        self.hratio.SetMinimum(0.5)        
        self.hratio.SetMaximum(1.5)
        self.hratio.GetYaxis().SetLabelSize(0.1)
        self.hratio.GetXaxis().SetLabelSize(0.1)
        self.hratio.GetYaxis().SetNdivisions(505)
        #self.hratio.GetXaxis().SetTitle(self.xtitle)
        self.hratio.GetXaxis().SetTitleOffset(1)
        self.hratio.GetXaxis().SetTitleSize(0.09)
        self.hratio.Draw('E1sames')
        self.line1.Draw('sames')
        #self.leg.Draw()
        CMS_lumi.CMS_lumi(self.canvas, iPeriod, iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.SetMaxY(2.)
        self.canvas.SaveAs(self.outputdir+'/ratio/cratio__'+self.prefix+"__"+self.xname+".pdf")
        self.pad1.cd()
        self.pad1.SetLogy()
        self.SetMaxY(1000)
        self.canvas.cd()
        self.canvas.Update()

        self.canvas.SaveAs(self.outputdir+'/ratio_logy/cratiology__'+self.prefix+"__"+self.xname+".pdf")
        #del self.canvas

        
    def reset(self):
        del self.hratio
        del self.line1
        del self.hdata
        del self.hmc
        del self.hstack
        del self.hdict
        del self.hempty
        del self.chdict
        del self.canvas
        del self.pad1
        del self.pad2
if __name__ == '__main__':
    print "start script",process.memory_info().rss  # in bytes
    parser = argparse.ArgumentParser(description='Plot configuration')
    ##---Example From SKFlat--##
    #parser.add_argument('-n', dest='NJobs', default=1, type=int)
    #parser.add_argument('-y', dest='Year', default="",help="deprecated. use -e")
    #parser.add_argument('--skim', dest='Skim', default="", help="ex) SkimTree_Dilepton")
    #parser.add_argument('--no_exec', action='store_true')
    #parser.add_argument('--reduction', dest='Reduction', default=1, type=float)
    ##---END---##
    ##--MY inputs--##
    parser.add_argument('--plot', dest='plot',help='path to plot conf')
    parser.add_argument('--proc', dest='proc',help='path to proc conf ')
    args = parser.parse_args()

    ##---Check input arguments--##
    if args.plot==None:
        print "[runPlotter]No --plot, need plot configuration"
        exit(1)
    if args.proc==None:
        print "[runPlotter]No --proc, need proc configuration"
        exit(1)
    ##---Get configuration, plotconf and procconf---##
    exec(open(args.plot))
    exec(open(args.proc))


    p=Plotter()
    #flist=glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/DATA/*.root")+\
    #glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/*.root")
    print "before get hist",process.memory_info().rss  # in bytes
    hdict,hdict_short=p.GetHistPathFromFilePath(plotconf['inputpath'])
    print "after get hist",process.memory_info().rss  # in bytes
    #outputdir=plotconf['outputdir']
    ##----Check Histogram List and Check xmin xmax----#
    xmin=sys.maxsize
    xmax=-sys.maxsize
    iplot=0
    drawer=Drawer()
    drawer.SetPlotConfig(plotconf)
    drawer.SetProcDict(procconf)
    drawer.SetInputpath(plotconf['inputpath'])    

    for iplot,v in enumerate(hdict_short):
        #if iplot>5:continue                                                                                                                              
        #if iplot!=11:continue
        print "2step histo structure"
        print "len(hdict_short)=",len(hdict_short)                                                                                                                            
        print iplot,v
        print(process.memory_info().rss)  # in bytes                                                                                                      
        #def SetHistDict(self,_hdict):                                                                                                                    
        #def SetProcDict(_pdict):                                                                                                                         
        #def init(title,prefix,variablename):
        #drawer=Drawer(hdict[c][v],procconf,'',c,v)                                                                                                       
        drawer.SetHistDict(hdict_short[v])
        drawer.init('',"all",v) ##title/prefix/variablename
        drawer.run()
        drawer.reset()

    for c in hdict:
        print c,
        print "len(hdict[c])=",len(hdict[c])

        for iplot,v in enumerate(hdict[c]):
            #if iplot>5:continue
            #if iplot!=11:continue
            print iplot,c,v
            print(process.memory_info().rss)  # in bytes
            #def SetHistDict(self,_hdict):
            #def SetProcDict(_pdict):
            #def init(title,prefix,variablename):
            
            #drawer=Drawer(hdict[c][v],procconf,'',c,v)
            drawer.SetHistDict(hdict[c][v])
            drawer.init('',c,v)
            drawer.run()
            drawer.reset()
            
