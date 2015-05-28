'''
Created on 08 May 2015

@author: Douglas Burns

CSV

'''

from __future__ import division#divide now does float

import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1F, TCanvas, TLegend, TLatex, kRed, kBlue
import math

if __name__ == '__main__':

	input_file = "../../data/GenJetDiff.root"
	GenJetPtDiffHist = TH1F("Difference in Gen Jet and Reco Jet Pt","Difference in Gen Jet and Reco Jet P_{t}", 300, 0, 300)
	GenJetEtaDiffHist = TH1F("Difference in Gen Jet and Reco Jet Eta","Difference in Gen Jet and Reco Jet Eta", 100, -5, 5)
	
	Tree = "likelihood/CSV"
	Chain = TChain(Tree)
	Chain.Add(input_file)
	Chain.SetBranchStatus("*",1)

	for event in Chain:
		GenJetPt = event.__getattr__("genJetPt")
		GenJetEta = event.__getattr__("genJetEta")
		JetPt = event.__getattr__("JetPt")
		JetEta = event.__getattr__("JetEta")

		PtDiff = GenJetPt - JetPt
		EtaDiff = GenJetEta - JetEta

		GenJetPtDiffHist.Fill((PtDiff))
		GenJetEtaDiffHist.Fill((EtaDiff))

	file = TFile("../output/GenJetDiffs.root", "RECREATE")

	Canvas1 = TCanvas("PtDiff","PtDiff", 0, 0, 800, 600)
	GenJetPtDiffHist.Draw()
	Canvas1.Update()
	Canvas1.SaveAs("../output/PtDiff.png")

	Canvas2 = TCanvas("EtaDiff","EtaDiff", 0, 0, 800, 600)
	GenJetEtaDiffHist.Draw()
	Canvas2.Update()
	Canvas2.SaveAs("../output/EtaDiff.png")

	GenJetPtDiffHist.Write()
	GenJetEtaDiffHist.Write()

