#!/usr/bin/env python 
##====================
##For Comparison. Denominator0 numerator1,2,3...
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
DrawOption="E HIST"
DrawOptionLegend="BR"

class Drawer:
    def __init__(self,_hdict,_name):
        self.hdict=_hdict ##container of histogram-objects
        self.name=_name
        self.outputdir=""
        self.lumi=""
        self.sqrtS="13"
        self.legend=ROOT.TLegend(0,0,1,1) #TLegend (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        self.legend.SetBorderSize(1)
        self.legend.SetLineColor(1)
    def GetRatio1Line(self):
        #TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        x1=self.xbins[0]
        x2=self.xbins[-1]
        y1=1
        y2=1
        self.line1=ROOT.TLine(x1,y1,x2,y2)
        self.line1.SetLineStyle(2)

    def SetLumi(self,_lumi):
        self.lumi=_lumi
    def SetPlotConfig(self,_plotconf):
        self.plotconf=_plotconf
        self.xname=self.plotconf["xname"]
        self.hnames=self.plotconf["names"]

        ##--legend--##
        x1=0.7
        y1=0.7
        x2=0.95
        y2=0.85
        self.nhisto=1+len(self.plotconf["numelist"])
        this_option="RT"
        if "legend" in self.plotconf:
            this_option=self.plotconf["legend"]
        if "R" in this_option:
            self.legend.SetX1(x1)
            self.legend.SetX2(x2)
        if "L" in this_option:
            self.legend.SetX1(x1-0.5)
            self.legend.SetX2(x2-0.5)
        if "T" in this_option:
            self.legend.SetY1(y2-self.nhisto*0.05)
            self.legend.SetY2(y2)
        if "B" in this_option:
            self.legend.SetY1(1-y2)
            self.legend.SetY2(1-y2-self.nhisto*0.05)


        self.LoadHisto()
    def GetXBins(self,h):
        xbins=[]
        for i in range(1,h.GetXaxis().GetNbins()+2):
            _BinLowEdge=h.GetXaxis().GetBinLowEdge(i)
            xbins.append(_BinLowEdge)
        return np.array(xbins)
    def LoadHisto(self):
        self.deno=self.plotconf["deno"]
        self.h_deno = self.GetHistoByName(self.deno)
        self.h_deno.GetXaxis().SetTitle(self.xname)
        self.h_deno.SetTitle(self.hnames[0])
        ## --get xbin
        self.xbins=self.GetXBins(self.h_deno)
        self.numelist=self.plotconf["numelist"]
        self.h_numelist=[]
        for nume in self.numelist:
            self.h_numelist.append(self.GetHistoByName(nume).Clone())
        for i in range(len(self.numelist)):
            self.h_numelist[i].GetXaxis().SetTitle(self.xname)
            self.h_numelist[i].SetTitle(self.hnames[i+1])
        self.h_ratiolist=[]
        self.GetRatio1Line()
        self.Rebin()

    def Rebin(self):
        if not "rebin" in self.plotconf: return
        #print list(self.xbins)
        self.xbins=np.array(self.plotconf["rebin"])
        #print list(self.xbins)
        self.h_deno=self.h_deno.Rebin(len(self.xbins)-1,\
                                      self.h_deno.GetName()+"_new" ,\
                                      self.xbins)        
        for i in range(len(self.h_numelist)):
            self.h_numelist[i]=self.h_numelist[i].Rebin(len(self.xbins)-1,self.h_numelist[i].GetName()+"_new" ,self.xbins)        
        ##---Rescale by bin width
        for ib in range(1,len(self.xbins)+1):
            width_i=self.h_deno.GetBinWidth(ib)
            y_i=self.h_deno.GetBinContent(ib)
            e_i=self.h_deno.GetBinError(ib)
            y_f=self.h_deno.GetBinContent(ib)/width_i
            e_f=self.h_deno.GetBinError(ib)/width_i
            self.h_deno.SetBinContent(ib,y_f)
            self.h_deno.SetBinError(ib,e_f)
            ##for numerators
            for i in range(len(self.h_numelist)):
                y_i=self.h_numelist[i].GetBinContent(ib)
                e_i=self.h_numelist[i].GetBinError(ib)
                y_f=self.h_numelist[i].GetBinContent(ib)/width_i
                e_f=self.h_numelist[i].GetBinError(ib)/width_i
                self.h_numelist[i].SetBinContent(ib,y_f)
                self.h_numelist[i].SetBinError(ib,e_f)


    def GetHistoByName(self,_name):
        nameparse=_name.split("/")
        c, v, p = nameparse[0], nameparse[1], nameparse[2] 
        return self.hdict[c][v][p]
    def run(self):
        ##---------From TDR style ---------##
        tdrstyle.setTDRStyle()
        #change the CMS_lumi variables (see CMS_lumi.py)
        CMS_lumi.lumi_13TeV = self.lumi+" fb^{-1}"
        if self.lumi=="":CMS_lumi.lumi_13TeV=""
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
        
        canvas = ROOT.TCanvas(self.name+'__',self.name+'__',50,50,W,H)
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
        

        #self.h_deno.SetMarkerStyle(8)
        #self.h_deno.SetMarkerSize(0.5)
        self.h_deno.SetLineColor(self.plotconf['color'][0])
        self.h_deno.Draw(DrawOption)
        self.legend.AddEntry(self.h_deno)
        i_nume=0
        for h_nume in self.h_numelist:
            h_nume.SetLineColor(self.plotconf['color'][i_nume+1])
            h_nume.Draw(DrawOption+"sames")
            self.legend.AddEntry(h_nume)
            i_nume+=1
        self.legend.Draw(DrawOptionLegend)
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)
        canvas.cd()
        canvas.Update()
        canvas.RedrawAxis()

        os.system("mkdir -p "+self.outputdir)

        for setlogx in self.plotconf["setlogx"]:
            for setlogy in self.plotconf["setlogy"]:
                prefix="__"                
                if setlogy==True:prefix="logy_"+prefix
                if setlogx==True:prefix="logx_"+prefix
                if (not setlogy) and (not setlogx): prefix=""
                canvas.SetLogy(setlogy)
                canvas.SetLogx(setlogx)
                canvas.SaveAs(self.outputdir+'/'+prefix+self.name+".pdf")
                canvas.SetLogy(0)
                canvas.SetLogx(0)
        ## --normalized plots
        self.h_deno_norm=self.h_deno.Clone()
        self.h_deno_norm.Scale(1/self.h_deno_norm.Integral())
        self.h_deno_norm.Draw(DrawOption)
        self.h_numelist_norm=[]
        for h_nume in self.h_numelist:
            h_nume_norm=h_nume.Clone()
            h_nume_norm.Scale(1/h_nume_norm.Integral())
            self.h_numelist_norm.append(h_nume_norm.Clone())
        for h_nume_ratio in self.h_numelist_norm:
            h_nume_ratio.Draw(DrawOption+'sames')
        self.legend.Draw(DrawOptionLegend)

        for setlogx in self.plotconf["setlogx"]:
            for setlogy in self.plotconf["setlogy"]:
                prefix="__"
                if setlogy==True:prefix="logy_"+prefix
                if setlogx==True:prefix="logx_"+prefix
                if (not setlogy) and (not setlogx): prefix=""
                canvas.SetLogy(setlogy)
                canvas.SetLogx(setlogx)
                canvas.SaveAs(self.outputdir+'/'+prefix+self.name+"__norm.pdf")
                canvas.SetLogy(0)
                canvas.SetLogx(0)
        ##--[END]Normalize


        ##--ratioplot
        for h_nume in self.h_numelist:
            h_ratio=h_nume/self.h_deno
            self.h_ratiolist.append(h_ratio)
        ##
        pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        pad1.SetTopMargin(0.1)
        pad1.SetBottomMargin(0.0)
        pad1.SetGridx()
        pad1.Draw()
        pad1.cd()
        self.h_deno.Draw(DrawOption)
        for h_nume in self.h_numelist:
            h_nume.Draw(DrawOption+"sames")
        self.legend.Draw(DrawOptionLegend)
        canvas.cd()
        pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        pad2.SetTopMargin(0.02)
        pad2.SetBottomMargin(0.2)
        pad2.SetGridx()
        pad2.Draw()
        pad2.cd()
        ##TODO::handle this with input args
        for h_ratio in self.h_ratiolist:
            h_ratio.SetMinimum(0.5)        
            h_ratio.SetMaximum(1.5)
            h_ratio.GetYaxis().SetLabelSize(0.1)
            h_ratio.GetXaxis().SetLabelSize(0.1)
            h_ratio.GetYaxis().SetNdivisions(505)
            #self.h_ratio.GetXaxis().SetTitle(self.xtitle)
            h_ratio.GetXaxis().SetTitleOffset(1)
            h_ratio.GetXaxis().SetTitleSize(0.09)
            h_ratio.Draw(DrawOption+'sames')
        self.line1.Draw('sames')
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

        for setlogx in self.plotconf["setlogx"]:
            for setlogy in self.plotconf["setlogy"]:
                canvas.cd()
                canvas.Update()
                pad1.cd()
                #pad1.SetLogy()
                prefix="__"
                if setlogy==True:prefix="logy_"+prefix
                if setlogx==True:prefix="logx_"+prefix
                if (not setlogy) and (not setlogx): prefix=""
                pad1.SetLogy(setlogy)
                pad1.SetLogx(setlogx)
                pad2.cd()
                pad2.SetLogx(setlogx)
                canvas.cd()
                canvas.Update()
                canvas.SaveAs(self.outputdir+'/'+prefix+self.name+"_ratio.pdf")
                canvas.SetLogy(0)
                canvas.SetLogx(0)
        ##--normalzed
        ##--ratio_norm
        canvas.cd()
        canvas.Update()        
        pad1.cd()
        self.h_ratiolist_norm=[]
        for h_nume_norm in self.h_numelist_norm:
            h_nume_ratio = h_nume_norm.Clone()/self.h_deno_norm
            self.h_ratiolist_norm.append(h_nume_ratio.Clone())
        self.h_deno_norm.Draw(DrawOption)
        for h_nume_norm in self.h_numelist_norm:
            h_nume_norm.Draw(DrawOption+"sames")
        self.legend.Draw(DrawOptionLegend)
        canvas.cd()
        pad2.cd()
        for h_ratio_norm in self.h_ratiolist_norm:
            h_ratio_norm.SetMinimum(0.5)        
            h_ratio_norm.SetMaximum(1.5)
            h_ratio_norm.GetYaxis().SetLabelSize(0.1)
            h_ratio_norm.GetXaxis().SetLabelSize(0.1)
            h_ratio_norm.GetYaxis().SetNdivisions(505)
            #self.h_ratio_norm.GetXaxis().SetTitle(self.xtitle)
            h_ratio_norm.GetXaxis().SetTitleOffset(1)
            h_ratio_norm.GetXaxis().SetTitleSize(0.09)
            h_ratio_norm.Draw(DrawOption+'sames')
        self.line1.Draw(DrawOption+'sames')
        CMS_lumi.CMS_lumi(canvas, iPeriod, iPos)

        for setlogx in self.plotconf["setlogx"]:
            for setlogy in self.plotconf["setlogy"]:
                canvas.cd()
                canvas.Update()
                pad1.cd()
                #pad1.SetLogy()
                prefix="__"
                if setlogy==True:prefix="logy_"+prefix
                if setlogx==True:prefix="logx_"+prefix
                if (not setlogy) and (not setlogx): prefix=""
                pad1.SetLogy(setlogy)
                pad1.SetLogx(setlogx)
                pad2.cd()
                pad2.SetLogx(setlogx)
                canvas.cd()
                canvas.Update()
                canvas.SaveAs(self.outputdir+'/'+prefix+self.name+"_ratio__norm.pdf")
                canvas.SetLogy(0)
                canvas.SetLogx(0)

        del canvas

        print "[OUTPUT]--->",self.outputdir
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
    parser.add_argument('--outputdir', dest='outputdir',help='path to outputdir')
    parser.add_argument('--inputfile', dest='inputfile',help='path to inputfile')
    args = parser.parse_args()

    ##---Check input arguments--##
    if args.plot==None:
        print "[runPlotter]No --plot, need plot configuration"
        exit(1)
    if args.outputdir==None:
        print "[runPlotter]No --outputdir, need proc configuration"
        exit(1)
    if args.inputfile==None:
        print "[runPlotter]No --inputfile, need proc configuration"
        exit(1)
    ##---Get configuration, plotconf and procconf---##
    exec(open(args.plot))
    ##dict_conf


    p=Plotter()
    #flist=glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/DATA/*.root")+\
    #glob("/data6/Users/jhchoi/SKFlatOutput/Run2UltraLegacy_v3/MYOUTPUT/test/BasicTest/2017/*.root")
    hdict=p.GetHistFromFileList([args.inputfile])
    
    ##----Check Histogram List and Check xmin xmax----#
    for plot in dict_conf:
        print plot
        drawer=Drawer(hdict,plot)
        drawer.SetPlotConfig(dict_conf[plot])
        drawer.outputdir=args.outputdir
        drawer.run()
            
