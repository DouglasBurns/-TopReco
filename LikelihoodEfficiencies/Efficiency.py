'''
Created on 08 May 2015

@author: Douglas Burns

Plots CSV, MW.vs.MT, Neutrino Chi Test.

'''
from __future__ import division
import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1F, TH2F, TCanvas, TPad, TAxis, TLegend, TLatex, kRed, kBlue, kGreen
import math

if __name__ == '__main__':


	########## 			SETUP 			##########
	gStyle.SetOptStat("")
	input_file = "../../data/tree_TTJet_5000pb_PFElectron_PFMuon_PF2PATJets_MET.root"

	inputTree = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/TopReco"
	Chain = TChain(inputTree)
	Chain.Add(input_file)

	Chain.SetBranchStatus("*",1)

	NumberEventsTotal = NumberEventsPassSelection = NumberEventsHaveRequisitePartons = NumberEventsMatchingBestSolution = 0


	for event in Chain:

		EventSolution = event.__getattr__("TypeofSolution")

		NumberEventsTotal += 1

		if (EventSolution == 1 or EventSolution == 2 or EventSolution == 3): 

			NumberEventsPassSelection += 1

		if (EventSolution == 1 or EventSolution == 2): 

			NumberEventsHaveRequisitePartons +=1

		if (EventSolution == 1): 

			NumberEventsMatchingBestSolution += 1

	print ("Number of Event Total : "), NumberEventsTotal
	print ("Number of Event Passing Selection : "), NumberEventsPassSelection
	print ("Number of Event Have Requisite Partons : "), NumberEventsHaveRequisitePartons
	print ("Number of Event that Match Best Solution : "), NumberEventsMatchingBestSolution

	print ("Efficiency wrt Event Selection : "), NumberEventsMatchingBestSolution/NumberEventsPassSelection
	print ("Efficiency wrt parton presence : "), NumberEventsMatchingBestSolution/NumberEventsHaveRequisitePartons