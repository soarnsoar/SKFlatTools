import ROOT
from ctypes import c_double
from collections import OrderedDict 
import sys
_filepath=sys.argv[1]
#tfile=ROOT.TFile.Open("../skflatoutput/combine.root")    
tfile=ROOT.TFile.Open(_filepath)

def PositiveIntegral(h,scorecut):
    c_bin=h.FindBin(scorecut)
    N=h.GetNbinsX()
    return h.Integral(c_bin,N+2)
def NegativeIntegral(h,scorecut):
    c_bin=h.FindBin(-scorecut)
    N=h.GetNbinsX()
    return h.Integral(0,c_bin-1)

def CalcAsymUsingHist(hlist,scorecut):
    htotal=hlist[0].Clone()
    htotal.Reset()

    hpos=hlist[0].Clone()
    hpos.Reset()

    hneg=hlist[0].Clone()
    hneg.Reset()

    N=htotal.GetNbinsX()
    for _h in hlist:
        htotal.Add(_h)


    cutbin_pos=htotal.FindBin(scorecut)
    cutbin_neg=htotal.FindBin(-scorecut)
    #print "cutbin_pos=",cutbin_pos
    #print "cutbin_neg=",cutbin_neg
    for i in range(1,N+1):
        if (i < cutbin_pos) and (i >= cutbin_neg):
            #print 'skip',i
            continue
        if i >= cutbin_pos:
            hpos.SetBinContent(i,htotal.GetBinContent(i))
            hpos.SetBinError(i,htotal.GetBinError(i))
        if i < cutbin_neg:
            hneg.SetBinContent(i,htotal.GetBinContent(i))
            hneg.SetBinError(i,htotal.GetBinError(i))
    err_p=c_double(0)
    
    N_p=hpos.IntegralAndError(cutbin_pos,N+1,err_p)
    err_p=float(err_p.value)
    print 'N_p=',N_p
    #print 'err_p=',err_p
    N_p_up=N_p+err_p
    N_p_down=N_p-err_p
    
    err_n=c_double(0)
    N_n=hneg.IntegralAndError(0,cutbin_neg-1,err_n)
    err_n=float(err_n.value)
    print 'N_n=',N_n
    #print 'err_n=',err_n

    N_n_up=N_n+err_n
    N_n_down=N_n-err_n

    Asym=(N_p-N_n)/(N_p+N_n)

    Asym_up=max((N_p_up-N_n_up)/(N_p_up+N_n_up), (N_p_down-N_n_down)/(N_p_down+N_n_down))
    Asym_down=min((N_p_up-N_n_up)/(N_p_up+N_n_up), (N_p_down-N_n_down)/(N_p_down+N_n_down))

    return Asym,Asym_up,Asym_down
    
    
def GetAsym(c,v,up=1.1,scorecut=0):
    print c,v
    #v="BJetWeightedCharge"
    #c="BMuonChargeEvt"

    proclist=["DY_bbar","DY_bevt"]
    h_dict={}
    for p in proclist:
        h_dict[p]=tfile.Get(c+"/"+v+"/"+p)

    #Asym,Asym_up,Asym_down=CalcAsymUsingHist([h_dict["DY_bbar"],h_dict["DY_bevt"]],scorecut)

    h_dict["DY_bbar_up"]=h_dict["DY_bbar"].Clone()
    h_dict["DY_bbar_up"].Scale(1.1)

    h_dict["DY_bevt_up"]=h_dict["DY_bevt"].Clone()
    h_dict["DY_bevt_up"].Scale(1.1)

    Asym_dict=OrderedDict()
    Asym_dict['SM']=[0,0,0]
    Asym_dict['bbarUp']=[0,0,0]
    Asym_dict['bevtUp']=[0,0,0]
    
    Asym_dict['SM'][0],Asym_dict['SM'][1],Asym_dict['SM'][2]=CalcAsymUsingHist([h_dict["DY_bbar"],h_dict["DY_bevt"]],scorecut)
    Asym_dict['bbarUp'][0],Asym_dict['bbarUp'][1],Asym_dict['bbarUp'][2]=CalcAsymUsingHist([h_dict["DY_bbar_up"],h_dict["DY_bevt"]],scorecut)
    Asym_dict['bevtUp'][0],Asym_dict['bevtUp'][1],Asym_dict['bevtUp'][2]=CalcAsymUsingHist([h_dict["DY_bbar"],h_dict["DY_bevt_up"]],scorecut)


    for model in Asym_dict:
        print '---',model,'---'
        print Asym_dict[model][0],Asym_dict[model][1],Asym_dict[model][2]


    '''
    N_dict={}
    N_dict["positive"]=0
    N_dict["negative"]=0

    N_dict["positive_bbarUp"]=0
    N_dict["negative_bbarUp"]=0

    N_dict["positive_bevtUp"]=0
    N_dict["negative_bevtUp"]=0
    for p in proclist:
        print p,"pos",PositiveIntegral(h_dict[p],scorecut)
        print p,"neg",NegativeIntegral(h_dict[p],scorecut)
        N_dict["positive"]+=PositiveIntegral(h_dict[p],scorecut)
        N_dict["negative"]+=NegativeIntegral(h_dict[p],scorecut)


        
        if "DY_bbar" in p:
            N_dict["positive_bbarUp"]+=PositiveIntegral(h_dict[p],scorecut)*up
            N_dict["negative_bbarUp"]+=NegativeIntegral(h_dict[p],scorecut)*up
        else:
            N_dict["positive_bbarUp"]+=PositiveIntegral(h_dict[p],scorecut)
            N_dict["negative_bbarUp"]+=NegativeIntegral(h_dict[p],scorecut)

        if "DY_bevt" in p:
            N_dict["positive_bevtUp"]+=PositiveIntegral(h_dict[p],scorecut)*up
            N_dict["negative_bevtUp"]+=NegativeIntegral(h_dict[p],scorecut)*up
        else:
            N_dict["positive_bevtUp"]+=PositiveIntegral(h_dict[p],scorecut)
            N_dict["negative_bevtUp"]+=NegativeIntegral(h_dict[p],scorecut)


    Asym_dict=OrderedDict()
    Asym_dict["SM"]=(N_dict["positive"]-N_dict["negative"])/(N_dict["positive"]+N_dict["negative"])
    Asym_dict["bbarUp"]=(N_dict["positive_bbarUp"]-N_dict["negative_bbarUp"])/(N_dict["positive_bbarUp"]+N_dict["negative_bbarUp"])
    Asym_dict["bevtUp"]=(N_dict["positive_bevtUp"]-N_dict["negative_bevtUp"])/(N_dict["positive_bevtUp"]+N_dict["negative_bevtUp"])

    print "Asymm"
    for a in Asym_dict:
        print a,'=',Asym_dict[a]
    '''
if __name__ == '__main__':
    ##
    True
    
    dict_ParamSet=OrderedDict()

    dict_ParamSet["MuonRegion_MuonChargeWeighted"]=["BMuonChargeEvt","BJetWeightedCharge"]
    dict_ParamSet["MuonRegion_MuonCharge"]=["BMuonChargeEvt","bmuon_charge"]
    dict_ParamSet["MuonRegion_JetChargeRaw"]=["BMuonChargeEvt","bjet_charge"]

    dict_ParamSet["ElectronRegion_ElectronChargeWeighted"]=["BElectronChargeEvt","BJetWeightedCharge"]
    dict_ParamSet["ElectronRegion_ElectronChargeWeighted"]=["BElectronChargeEvt","belectron_charge"]
    dict_ParamSet["ElectronRegion_JetCharge"]=["BElectronChargeEvt","bjet_charge"]


    dict_ParamSet["JetRegion_JetChargeWeighted"]=["BJetChargeEvt","BJetWeightedCharge"]
    dict_ParamSet["JetRegion_JetChargeRaw"]=["BJetChargeEvt","bjet_charge"]


    dict_ParamSet["UntaggedEvt_JetCharge"]=["UntaggedEvt","bjet_charge"]

    dict_ParamSet["AllFinal_ChargeWeighted"]=["FinalSelection","BJetWeightedCharge"]
    dict_ParamSet["AllFinal_JetChargeRaw"]=["FinalSelection","bjet_charge"]

    cutlist=[0,0.3,0.5,0.6]
    for c in cutlist:
        print "[scorecut===",c,"]"
        for n in dict_ParamSet:
            print "====",n,"==="
            GetAsym(dict_ParamSet[n][0], dict_ParamSet[n][1],1.1,c)
