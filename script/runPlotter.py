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
from collections import OrderedDict

class Drawer:
    def __init__(self,_hdict, _pdict,title,prefix,variablename):
        self.hdict=_hdict ##container of histogram-objects
        self.pdict=_pdict ##process info
        self.ymin=sys.maxsize
        self.ymax=-sys.maxsize
        self.xbins=[]
        self.SetNames(title,prefix,variablename)
        self.CombineHist()
        self.SetMinMaxBins()
        self.GetRatio1Line()
    
    def CombineHist(self):
        ##---Combine Histos
        self.chdict=OrderedDict()
        for p in self.pdict:
            subidx=0
            for subp in self.pdict[p]['procs']: ## subp=TTLL TTLJ will be combined to TTtotal
                if subidx==0:
                    self.chdict[p]=self.hdict[subp].Clone()
                else:
                    self.chdict[p].Add(self.hdict[subp])
                subidx+=1

        ##---Stack Histos
        mcidx=0
        for p in self.pdict:
            ##--Set data histo
            if 'isData' in self.pdict[p]:
                if self.pdict[p]['isData']: 
                    self.hdata=self.chdict[p].Clone()
                    continue
            ##--Set MC histo MC
            if mcidx==0:
                print 'stack',p
                self.hmc=self.chdict[p].Clone()
                self.hstack=ROOT.THStack(self.prefix+'__'+self.xname,\
                                           self.prefix+'__'+self.xname)
                
                self.chdict[p].SetFillColor(self.pdict[p]['color'])
                self.hstack.Add(self.chdict[p])
            else:
                print 'stack',p
                self.hmc.Add(self.chdict[p])
                self.chdict[p].SetFillColor(self.pdict[p]['color'])
                self.hstack.Add(self.chdict[p])
            
            mcidx+=1





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
    def run(self):
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
        
        canvas = ROOT.TCanvas(self.prefix+'__'+self.xname,self.prefix+'__'+self.xname,50,50,W,H)
        canvas.SetFillColor(0)
        canvas.SetBorderMode(0)
        canvas.SetFrameFillStyle(0)
        canvas.SetFrameBorderMode(0)
        canvas.SetLeftMargin( L/W )
        canvas.SetRightMargin( R/W )
        canvas.SetTopMargin( T/H )
        canvas.SetBottomMargin( B/H )
        canvas.SetTickx(0)
        canvas.SetTicky(0)
        

        self.hdata.SetMarkerStyle(8)
        self.hdata.SetMarkerSize(0.5)
        
        self.hstack.Draw('hist')
        self.hdata.Draw('E1sames')

        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
        canvas.cd()
        canvas.Update()
        canvas.RedrawAxis()
        canvas.SaveAs(self.outputdir+'/'+self.prefix+self.xname+".pdf")
        canvas.SetLogy()
        canvas.SaveAs(self.outputdir+'/'+self.prefix+self.xname+"_log.pdf")
        canvas.SetLogy(0)
        ##--ratioplot
        self.hratio=self.hdata/self.hmc
        ##
        pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        pad1.SetTopMargin(0.1)
        pad1.SetBottomMargin(0.02)
        pad1.SetGridx()
        pad1.Draw()
        pad1.cd()
        self.hstack.Draw('hist')
        self.hdata.Draw('E1sames')
        
        canvas.cd()
        pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        pad2.SetTopMargin(0.02)
        pad2.SetBottomMargin(0.2)
        pad2.SetGridx()
        pad2.Draw()
        pad2.cd()
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
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
        canvas.cd()
        canvas.Update()
        canvas.SaveAs(self.outputdir+'/'+self.prefix+self.xname+"_ratio.pdf")
        pad1.cd()
        pad1.SetLogy()
        canvas.cd()
        canvas.Update()
        canvas.SaveAs(self.outputdir+'/'+self.prefix+self.xname+"_ratio_log.pdf")




        del canvas
if __name__ == '__main__':
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
    hdict=p.GetHistFromFileList(plotconf['filelist'])
    #outputdir=plotconf['outputdir']
    ##----Check Histogram List and Check xmin xmax----#
    xmin=sys.maxsize
    xmax=-sys.maxsize
    for c in hdict:
        for v in hdict[c]:
            #print c,v
            drawer=Drawer(hdict[c][v],procconf,'',c,v)
            #    def SetNames(self,title,prefix,xname,yname):
            drawer.SetPlotConfig(plotconf)
            drawer.run()
            
