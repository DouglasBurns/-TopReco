'''
Created on 08 May 2015

@author: Douglas Burns

Plots CSV, MW.vs.MT, Neutrino Chi Test.

'''

import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1F, TH2F, THStack, TCanvas, TPad, TAxis, TLegend, TLatex, kMagenta, kRed, kBlue, kGreen
import math

if __name__ == '__main__':


	########## 			SETUP 			##########
	gStyle.SetOptStat("")
	input_file = "../../data/tree_TTJet_5000pb_PFElectron_PFMuon_PF2PATJets_MET.root"
	
	HadronicTopPtHist_Correct = TH1F("HadronicTopPt_Correct","HadronicTopPt_Correct", 200, 0, 400)
	HadronicTopPtHist_Incorrect = TH1F("HadronicTopPt_Incorrect","HadronicTopPt_Incorrect", 200, 0, 400)
	HadronicTopPtHist_NotSemiLeptonic = TH1F("HadronicTopPt_NotSemiLeptonic","HadronicTopPt_NotSemiLeptonic", 200, 0, 400)
	HadronicTopPtHist_NotReconstructible = TH1F("HadronicTopPt_NotReconstructible","HadronicTopPt_NotReconstructible", 200, 0, 400)

	HadronicTopEtaHist_Correct = TH1F("HadronicTopEta_Correct","HadronicTopEta_Correct", 200, -5, 5)
	HadronicTopEtaHist_Incorrect = TH1F("HadronicTopEta_Incorrect","HadronicTopEta_Incorrect", 200, -5, 5)
	HadronicTopEtaHist_NotSemiLeptonic = TH1F("HadronicTopEta_NotSemiLeptonic","HadronicTopEta_NotSemiLeptonic", 200, -5, 5)
	HadronicTopEtaHist_NotReconstructible = TH1F("HadronicTopEta_NotReconstructible","HadronicTopEta_NotReconstructible", 200, -5, 5)

	HadronicTopEnergyHist_Correct = TH1F("HadronicTopEnergy_Correct","HadronicTopEnergy_Correct", 200, 0, 400)
	HadronicTopEnergyHist_Incorrect = TH1F("HadronicTopEnergy_Incorrect","HadronicTopEnergy_Incorrect", 200, 0, 400)
	HadronicTopEnergyHist_NotSemiLeptonic = TH1F("HadronicTopEnergy_NotSemiLeptonic","HadronicTopEnergy_NotSemiLeptonic", 200, 0, 400)
	HadronicTopEnergyHist_NotReconstructible = TH1F("HadronicTopEnergy_NotReconstructible","HadronicTopEnergy_NotReconstructible", 200, 0, 400)


	LeptonicTopPtHist_Correct = TH1F("LeptonicTopPt_Correct","LeptonicTopPt_Correct", 200, 0, 400)
	LeptonicTopPtHist_Incorrect = TH1F("LeptonicTopPt_Incorrect","LeptonicTopPt_Incorrect", 200, 0, 400)
	LeptonicTopPtHist_NotSemiLeptonic = TH1F("LeptonicTopPt_NotSemiLeptonic","LeptonicTopPt_NotSemiLeptonic", 200, 0, 400)
	LeptonicTopPtHist_NotReconstructible = TH1F("LeptonicTopPt_NotReconstructible","LeptonicTopPt_NotReconstructible", 200, 0, 400)

	LeptonicTopEtaHist_Correct = TH1F("LeptonicTopEta_Correct","LeptonicTopEta_Correct", 200, -5, 5)
	LeptonicTopEtaHist_Incorrect = TH1F("LeptonicTopEta_Incorrect","LeptonicTopEta_Incorrect", 200, -5, 5)
	LeptonicTopEtaHist_NotSemiLeptonic = TH1F("LeptonicTopEta_NotSemiLeptonic","LeptonicTopEta_NotSemiLeptonic", 200, -5, 5)
	LeptonicTopEtaHist_NotReconstructible = TH1F("LeptonicTopEta_NotReconstructible","LeptonicTopEta_NotReconstructible", 200, -5, 5)

	LeptonicTopEnergyHist_Correct = TH1F("LeptonicTopEnergy_Correct","LeptonicTopEnergy_Correct", 200, 0, 400)
	LeptonicTopEnergyHist_Incorrect = TH1F("LeptonicTopEnergy_Incorrect","LeptonicTopEnergy_Incorrect", 200, 0, 400)
	LeptonicTopEnergyHist_NotSemiLeptonic = TH1F("LeptonicTopEnergy_NotSemiLeptonic","LeptonicTopEnergy_NotSemiLeptonic", 200, 0, 400)
	LeptonicTopEnergyHist_NotReconstructible = TH1F("LeptonicTopEnergy_NotReconstructible","LeptonicTopEnergy_NotReconstructible", 200, 0, 400)


	Tree = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/TopReco"
	Chain = TChain(Tree)
	Chain.Add(input_file)


	Chain.SetBranchStatus("*",1)


	########## 			FILL HISTOGRAMS 		##########

	for event in Chain:

		HadronicTopPt = event.__getattr__("HadronicTop_Pt")
		HadronicTopEta = event.__getattr__("HadronicTop_Eta")
		HadronicTopEnergy = event.__getattr__("HadronicTop_Energy")
		HadronicTopMass = event.__getattr__("HadronicTop_Mass")

		LeptonicTopPt = event.__getattr__("LeptonicTop_Pt")
		LeptonicTopEta = event.__getattr__("LeptonicTop_Eta")
		LeptonicTopEnergy = event.__getattr__("LeptonicTop_Energy")
		LeptonicTopMass = event.__getattr__("LeptonicTop_Mass")

		TypeofSolution = event.__getattr__("TypeofSolution")

		if (TypeofSolution == 1):#Correct = 1
			HadronicTopPtHist_Correct.Fill(HadronicTopPt)
			HadronicTopEtaHist_Correct.Fill(HadronicTopEta)
			HadronicTopEnergyHist_Correct.Fill(HadronicTopEnergy)
			LeptonicTopPtHist_Correct.Fill(LeptonicTopPt)
			LeptonicTopEtaHist_Correct.Fill(LeptonicTopEta)
			LeptonicTopEnergyHist_Correct.Fill(LeptonicTopEnergy)

		if (TypeofSolution == 2):#Reconstruction Chose Wrong Combination = 2
			HadronicTopPtHist_Incorrect.Fill(HadronicTopPt)
			HadronicTopEtaHist_Incorrect.Fill(HadronicTopEta)
			HadronicTopEnergyHist_Incorrect.Fill(HadronicTopEnergy)
			LeptonicTopPtHist_Incorrect.Fill(LeptonicTopPt)
			LeptonicTopEtaHist_Incorrect.Fill(LeptonicTopEta)
			LeptonicTopEnergyHist_Incorrect.Fill(LeptonicTopEnergy)

		if (TypeofSolution == 3):#Event does not have all partons present = 3
			HadronicTopPtHist_NotReconstructible.Fill(HadronicTopPt)
			HadronicTopEtaHist_NotReconstructible.Fill(HadronicTopEta)
			HadronicTopEnergyHist_NotReconstructible.Fill(HadronicTopEnergy)
			LeptonicTopPtHist_NotReconstructible.Fill(LeptonicTopPt)
			LeptonicTopEtaHist_NotReconstructible.Fill(LeptonicTopEta)
			LeptonicTopEnergyHist_NotReconstructible.Fill(LeptonicTopEnergy)

		if (TypeofSolution == 4):#Event is not semiLeptonic = 4
			HadronicTopPtHist_NotSemiLeptonic.Fill(HadronicTopPt)
			HadronicTopEtaHist_NotSemiLeptonic.Fill(HadronicTopEta)
			HadronicTopEnergyHist_NotSemiLeptonic.Fill(HadronicTopEnergy)
			LeptonicTopPtHist_NotSemiLeptonic.Fill(LeptonicTopPt)
			LeptonicTopEtaHist_NotSemiLeptonic.Fill(LeptonicTopEta)
			LeptonicTopEnergyHist_NotSemiLeptonic.Fill(LeptonicTopEnergy)

	########## 				NORMALISING 			##########

	# integral = LightJetCSVHist.Integral()
	# LightJetCSVHist.Scale(1/integral)

	########## 				PLOTTING Part1				##########


	file = TFile("TopDistributions.root", "RECREATE")


	########## 			Hadronic Top Pt 			##########

	HadronicTopPtCanvas = TCanvas("HadronicTopPt","HadronicTopPt", 0, 0, 800, 600)
	HadronicTopPtleg = TLegend(0.5,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	HadronicTopPtleg.SetFillColor(0)
	HadronicTopPtleg.SetLineColor(0)

	HadronicTopPtStack = THStack("Hadronic Top Pt","Hadronic Top Pt")

	HadronicTopPtHist_NotSemiLeptonic.SetFillColor(kMagenta)
	HadronicTopPtleg.AddEntry(HadronicTopPtHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	HadronicTopPtStack.Add(HadronicTopPtHist_NotSemiLeptonic)

	HadronicTopPtHist_NotReconstructible.SetFillColor(kGreen)
	HadronicTopPtleg.AddEntry(HadronicTopPtHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	HadronicTopPtStack.Add(HadronicTopPtHist_NotReconstructible)

	HadronicTopPtHist_Incorrect.SetFillColor(kRed)
	HadronicTopPtleg.AddEntry(HadronicTopPtHist_Incorrect, "TTbar Wrong Reco" ,"f")
	HadronicTopPtStack.Add(HadronicTopPtHist_Incorrect)

	HadronicTopPtHist_Correct.SetFillColor(kBlue)
	HadronicTopPtleg.AddEntry(HadronicTopPtHist_Correct, "TTbar Right Reco" ,"f")
	HadronicTopPtStack.Add(HadronicTopPtHist_Correct)

	HadronicTopPtStack.Draw()
	HadronicTopPtleg.Draw()
	HadronicTopPtCanvas.Update()
	HadronicTopPtCanvas.SaveAs("plots/HadronicTopPt.png")

	HadronicTopPtStack.Write()
	HadronicTopPtHist_Correct.Write()
	HadronicTopPtHist_Incorrect.Write()
	HadronicTopPtHist_NotReconstructible.Write()
	HadronicTopPtHist_NotSemiLeptonic.Write()


	########## 			Hadronic Top Eta 			##########

	HadronicTopEtaCanvas = TCanvas("HadronicTopEta","HadronicTopEta", 0, 0, 800, 600)
	HadronicTopEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	HadronicTopEtaleg.SetFillColor(0)
	HadronicTopEtaleg.SetLineColor(0)

	HadronicTopEtaStack = THStack("Hadronic Top Eta","Hadronic Top Eta")

	HadronicTopEtaHist_NotSemiLeptonic.SetFillColor(kMagenta)
	HadronicTopEtaleg.AddEntry(HadronicTopEtaHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	HadronicTopEtaStack.Add(HadronicTopEtaHist_NotSemiLeptonic)

	HadronicTopEtaHist_NotReconstructible.SetFillColor(kGreen)
	HadronicTopEtaleg.AddEntry(HadronicTopEtaHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	HadronicTopEtaStack.Add(HadronicTopEtaHist_NotReconstructible)

	HadronicTopEtaHist_Incorrect.SetFillColor(kRed)
	HadronicTopEtaleg.AddEntry(HadronicTopEtaHist_Incorrect, "TTbar Wrong Reco" ,"f")
	HadronicTopEtaStack.Add(HadronicTopEtaHist_Incorrect)

	HadronicTopEtaHist_Correct.SetFillColor(kBlue)
	HadronicTopEtaleg.AddEntry(HadronicTopEtaHist_Correct, "TTbar Right Reco" ,"f")
	HadronicTopEtaStack.Add(HadronicTopEtaHist_Correct)

	HadronicTopEtaStack.Draw()
	HadronicTopEtaleg.Draw()
	HadronicTopEtaCanvas.Update()
	HadronicTopEtaCanvas.SaveAs("plots/HadronicTopEta.png")

	HadronicTopEtaStack.Write()
	HadronicTopEtaHist_Correct.Write()
	HadronicTopEtaHist_Incorrect.Write()
	HadronicTopEtaHist_NotReconstructible.Write()
	HadronicTopEtaHist_NotSemiLeptonic.Write()


	########## 			Hadronic Top Energy 			##########

	HadronicTopEnergyCanvas = TCanvas("HadronicTopEnergy","HadronicTopEnergy", 0, 0, 800, 600)
	HadronicTopEnergyleg = TLegend(0.15,0.65,0.45,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	HadronicTopEnergyleg.SetFillColor(0)
	HadronicTopEnergyleg.SetLineColor(0)

	HadronicTopEnergyStack = THStack("Hadronic Top Energy","Hadronic Top Energy")

	HadronicTopEnergyHist_NotSemiLeptonic.SetFillColor(kMagenta)
	HadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	HadronicTopEnergyStack.Add(HadronicTopEnergyHist_NotSemiLeptonic)

	HadronicTopEnergyHist_NotReconstructible.SetFillColor(kGreen)
	HadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	HadronicTopEnergyStack.Add(HadronicTopEnergyHist_NotReconstructible)

	HadronicTopEnergyHist_Incorrect.SetFillColor(kRed)
	HadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_Incorrect, "TTbar Wrong Reco" ,"f")
	HadronicTopEnergyStack.Add(HadronicTopEnergyHist_Incorrect)

	HadronicTopEnergyHist_Correct.SetFillColor(kBlue)
	HadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_Correct, "TTbar Right Reco" ,"f")
	HadronicTopEnergyStack.Add(HadronicTopEnergyHist_Correct)

	HadronicTopEnergyStack.Draw()
	HadronicTopEnergyleg.Draw()
	HadronicTopEnergyCanvas.Update()
	HadronicTopEnergyCanvas.SaveAs("plots/HadronicTopEnergy.png")

	HadronicTopEnergyStack.Write()
	HadronicTopEnergyHist_Correct.Write()
	HadronicTopEnergyHist_Incorrect.Write()
	HadronicTopEnergyHist_NotReconstructible.Write()
	HadronicTopEnergyHist_NotSemiLeptonic.Write()


########## 			Leptonic Top Pt 			##########

	LeptonicTopPtCanvas = TCanvas("LeptonicTopPt","LeptonicTopPt", 0, 0, 800, 600)
	LeptonicTopPtleg = TLegend(0.5,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	LeptonicTopPtleg.SetFillColor(0)
	LeptonicTopPtleg.SetLineColor(0)

	LeptonicTopPtStack = THStack("Leptonic Top Pt","Leptonic Top Pt")

	LeptonicTopPtHist_NotSemiLeptonic.SetFillColor(kMagenta)
	LeptonicTopPtleg.AddEntry(LeptonicTopPtHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	LeptonicTopPtStack.Add(LeptonicTopPtHist_NotSemiLeptonic)

	LeptonicTopPtHist_NotReconstructible.SetFillColor(kGreen)
	LeptonicTopPtleg.AddEntry(LeptonicTopPtHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	LeptonicTopPtStack.Add(LeptonicTopPtHist_NotReconstructible)

	LeptonicTopPtHist_Incorrect.SetFillColor(kRed)
	LeptonicTopPtleg.AddEntry(LeptonicTopPtHist_Incorrect, "TTbar Wrong Reco" ,"f")
	LeptonicTopPtStack.Add(LeptonicTopPtHist_Incorrect)

	LeptonicTopPtHist_Correct.SetFillColor(kBlue)
	LeptonicTopPtleg.AddEntry(LeptonicTopPtHist_Correct, "TTbar Right Reco" ,"f")
	LeptonicTopPtStack.Add(LeptonicTopPtHist_Correct)

	LeptonicTopPtStack.Draw()
	LeptonicTopPtleg.Draw()
	LeptonicTopPtCanvas.Update()
	LeptonicTopPtCanvas.SaveAs("plots/LeptonicTopPt.png")

	LeptonicTopPtStack.Write()
	LeptonicTopPtHist_Correct.Write()
	LeptonicTopPtHist_Incorrect.Write()
	LeptonicTopPtHist_NotReconstructible.Write()
	LeptonicTopPtHist_NotSemiLeptonic.Write()


	########## 			Leptonic Top Eta 			##########

	LeptonicTopEtaCanvas = TCanvas("LeptonicTopEta","LeptonicTopEta", 0, 0, 800, 600)
	LeptonicTopEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	LeptonicTopEtaleg.SetFillColor(0)
	LeptonicTopEtaleg.SetLineColor(0)

	LeptonicTopEtaStack = THStack("Leptonic Top Eta","Leptonic Top Eta")

	LeptonicTopEtaHist_NotSemiLeptonic.SetFillColor(kMagenta)
	LeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	LeptonicTopEtaStack.Add(LeptonicTopEtaHist_NotSemiLeptonic)

	LeptonicTopEtaHist_NotReconstructible.SetFillColor(kGreen)
	LeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	LeptonicTopEtaStack.Add(LeptonicTopEtaHist_NotReconstructible)

	LeptonicTopEtaHist_Incorrect.SetFillColor(kRed)
	LeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_Incorrect, "TTbar Wrong Reco" ,"f")
	LeptonicTopEtaStack.Add(LeptonicTopEtaHist_Incorrect)

	LeptonicTopEtaHist_Correct.SetFillColor(kBlue)
	LeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_Correct, "TTbar Right Reco" ,"f")
	LeptonicTopEtaStack.Add(LeptonicTopEtaHist_Correct)

	LeptonicTopEtaStack.Draw()
	LeptonicTopEtaleg.Draw()
	LeptonicTopEtaCanvas.Update()
	LeptonicTopEtaCanvas.SaveAs("plots/LeptonicTopEta.png")

	LeptonicTopEtaStack.Write()
	LeptonicTopEtaHist_Correct.Write()
	LeptonicTopEtaHist_Incorrect.Write()
	LeptonicTopEtaHist_NotReconstructible.Write()
	LeptonicTopEtaHist_NotSemiLeptonic.Write()


	########## 			Leptonic Top Energy 			##########

	LeptonicTopEnergyCanvas = TCanvas("LeptonicTopEnergy","LeptonicTopEnergy", 0, 0, 800, 600)
	LeptonicTopEnergyleg = TLegend(0.15,0.65,0.45,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	LeptonicTopEnergyleg.SetFillColor(0)
	LeptonicTopEnergyleg.SetLineColor(0)

	LeptonicTopEnergyStack = THStack("Leptonic Top Energy","Leptonic Top Energy")

	LeptonicTopEnergyHist_NotSemiLeptonic.SetFillColor(kMagenta)
	LeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	LeptonicTopEnergyStack.Add(LeptonicTopEnergyHist_NotSemiLeptonic)

	LeptonicTopEnergyHist_NotReconstructible.SetFillColor(kGreen)
	LeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	LeptonicTopEnergyStack.Add(LeptonicTopEnergyHist_NotReconstructible)

	LeptonicTopEnergyHist_Incorrect.SetFillColor(kRed)
	LeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_Incorrect, "TTbar Wrong Reco" ,"f")
	LeptonicTopEnergyStack.Add(LeptonicTopEnergyHist_Incorrect)

	LeptonicTopEnergyHist_Correct.SetFillColor(kBlue)
	LeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_Correct, "TTbar Right Reco" ,"f")
	LeptonicTopEnergyStack.Add(LeptonicTopEnergyHist_Correct)

	LeptonicTopEnergyStack.Draw()
	LeptonicTopEnergyleg.Draw()
	LeptonicTopEnergyCanvas.Update()
	LeptonicTopEnergyCanvas.SaveAs("plots/LeptonicTopEnergy.png")

	LeptonicTopEnergyStack.Write()
	LeptonicTopEnergyHist_Correct.Write()
	LeptonicTopEnergyHist_Incorrect.Write()
	LeptonicTopEnergyHist_NotReconstructible.Write()
	LeptonicTopEnergyHist_NotSemiLeptonic.Write()


	##########			PLOTS SUPERIMPOSED			##########

	########## 				NORMALISING 			##########

	integral = HadronicTopPtHist_Correct.Integral()
	HadronicTopPtHist_Correct.Scale(1/integral)
	integral = HadronicTopEtaHist_Correct.Integral()
	HadronicTopEtaHist_Correct.Scale(1/integral)
	integral = HadronicTopEnergyHist_Correct.Integral()
	HadronicTopEnergyHist_Correct.Scale(1/integral)
	integral = LeptonicTopPtHist_Correct.Integral()
	LeptonicTopPtHist_Correct.Scale(1/integral)
	integral = LeptonicTopEtaHist_Correct.Integral()
	LeptonicTopEtaHist_Correct.Scale(1/integral)
	integral = LeptonicTopEnergyHist_Correct.Integral()
	LeptonicTopEnergyHist_Correct.Scale(1/integral)

	integral = HadronicTopPtHist_Incorrect.Integral()
	HadronicTopPtHist_Incorrect.Scale(1/integral)
	integral = HadronicTopEtaHist_Incorrect.Integral()
	HadronicTopEtaHist_Incorrect.Scale(1/integral)
	integral = HadronicTopEnergyHist_Incorrect.Integral()
	HadronicTopEnergyHist_Incorrect.Scale(1/integral)
	integral = LeptonicTopPtHist_Incorrect.Integral()
	LeptonicTopPtHist_Incorrect.Scale(1/integral)
	integral = LeptonicTopEtaHist_Incorrect.Integral()
	LeptonicTopEtaHist_Incorrect.Scale(1/integral)
	integral = LeptonicTopEnergyHist_Incorrect.Integral()
	LeptonicTopEnergyHist_Incorrect.Scale(1/integral)

	integral = HadronicTopPtHist_NotReconstructible.Integral()
	HadronicTopPtHist_NotReconstructible.Scale(1/integral)
	integral = HadronicTopEtaHist_NotReconstructible.Integral()
	HadronicTopEtaHist_NotReconstructible.Scale(1/integral)
	integral = HadronicTopEnergyHist_NotReconstructible.Integral()
	HadronicTopEnergyHist_NotReconstructible.Scale(1/integral)
	integral = LeptonicTopPtHist_NotReconstructible.Integral()
	LeptonicTopPtHist_NotReconstructible.Scale(1/integral)
	integral = LeptonicTopEtaHist_NotReconstructible.Integral()
	LeptonicTopEtaHist_NotReconstructible.Scale(1/integral)
	integral = LeptonicTopEnergyHist_NotReconstructible.Integral()
	LeptonicTopEnergyHist_NotReconstructible.Scale(1/integral)

	integral = HadronicTopPtHist_NotSemiLeptonic.Integral()
	HadronicTopPtHist_NotSemiLeptonic.Scale(1/integral)
	integral = HadronicTopEtaHist_NotSemiLeptonic.Integral()
	HadronicTopEtaHist_NotSemiLeptonic.Scale(1/integral)
	integral = HadronicTopEnergyHist_NotSemiLeptonic.Integral()
	HadronicTopEnergyHist_NotSemiLeptonic.Scale(1/integral)
	integral = LeptonicTopPtHist_NotSemiLeptonic.Integral()
	LeptonicTopPtHist_NotSemiLeptonic.Scale(1/integral)
	integral = LeptonicTopEtaHist_NotSemiLeptonic.Integral()
	LeptonicTopEtaHist_NotSemiLeptonic.Scale(1/integral)
	integral = LeptonicTopEnergyHist_NotSemiLeptonic.Integral()
	LeptonicTopEnergyHist_NotSemiLeptonic.Scale(1/integral)


	########## 			Hadronic Top Pt 			##########

	NormalisedHadronicTopPtCanvas = TCanvas("NormalisedHadronicTopPt","NormalisedHadronicTopPt", 0, 0, 800, 600)
	NormalisedHadronicTopPtleg = TLegend(0.5,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedHadronicTopPtleg.SetFillColor(0)
	NormalisedHadronicTopPtleg.SetLineColor(0)


	HadronicTopPtHist_NotSemiLeptonic.SetLineColor(kMagenta)
	HadronicTopPtHist_NotReconstructible.SetLineColor(kGreen)
	HadronicTopPtHist_Incorrect.SetLineColor(kRed)
	HadronicTopPtHist_Correct.SetLineColor(kBlue)
	HadronicTopPtHist_NotSemiLeptonic.SetFillColor(0)
	HadronicTopPtHist_NotReconstructible.SetFillColor(0)
	HadronicTopPtHist_Incorrect.SetFillColor(0)
	HadronicTopPtHist_Correct.SetFillColor(0)

	HadronicTopPtHist_Incorrect.Draw("")
	HadronicTopPtHist_NotReconstructible.Draw("same")
	HadronicTopPtHist_NotSemiLeptonic.Draw("same")
	HadronicTopPtHist_Correct.Draw("same")

	NormalisedHadronicTopPtleg.AddEntry(HadronicTopPtHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedHadronicTopPtleg.AddEntry(HadronicTopPtHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedHadronicTopPtleg.AddEntry(HadronicTopPtHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedHadronicTopPtleg.AddEntry(HadronicTopPtHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedHadronicTopPtleg.Draw()
	NormalisedHadronicTopPtCanvas.Update()
	NormalisedHadronicTopPtCanvas.SaveAs("plots/NormalisedHadronicTopPt.png")


	########## 			Hadronic Top Eta 			##########

	NormalisedHadronicTopEtaCanvas = TCanvas("NormalisedHadronicTopEta","NormalisedHadronicTopEta", 0, 0, 800, 600)
	NormalisedHadronicTopEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedHadronicTopEtaleg.SetFillColor(0)
	NormalisedHadronicTopEtaleg.SetLineColor(0)


	HadronicTopEtaHist_NotSemiLeptonic.SetLineColor(kMagenta)
	HadronicTopEtaHist_NotReconstructible.SetLineColor(kGreen)
	HadronicTopEtaHist_Incorrect.SetLineColor(kRed)
	HadronicTopEtaHist_Correct.SetLineColor(kBlue)
	HadronicTopEtaHist_NotSemiLeptonic.SetFillColor(0)
	HadronicTopEtaHist_NotReconstructible.SetFillColor(0)
	HadronicTopEtaHist_Incorrect.SetFillColor(0)
	HadronicTopEtaHist_Correct.SetFillColor(0)

	HadronicTopEtaHist_Correct.Draw("")
	HadronicTopEtaHist_Incorrect.Draw("same")
	HadronicTopEtaHist_NotReconstructible.Draw("same")
	HadronicTopEtaHist_NotSemiLeptonic.Draw("same")

	NormalisedHadronicTopEtaleg.AddEntry(HadronicTopEtaHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedHadronicTopEtaleg.AddEntry(HadronicTopEtaHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedHadronicTopEtaleg.AddEntry(HadronicTopEtaHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedHadronicTopEtaleg.AddEntry(HadronicTopEtaHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedHadronicTopEtaleg.Draw()
	NormalisedHadronicTopEtaCanvas.Update()
	NormalisedHadronicTopEtaCanvas.SaveAs("plots/NormalisedHadronicTopEta.png")


########## 			Hadronic Top Energy 			##########

	NormalisedHadronicTopEnergyCanvas = TCanvas("NormalisedHadronicTopEnergy","NormalisedHadronicTopEnergy", 0, 0, 800, 600)
	NormalisedHadronicTopEnergyleg = TLegend(0.15,0.65,0.45,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedHadronicTopEnergyleg.SetFillColor(0)
	NormalisedHadronicTopEnergyleg.SetLineColor(0)


	HadronicTopEnergyHist_NotSemiLeptonic.SetLineColor(kMagenta)
	HadronicTopEnergyHist_NotReconstructible.SetLineColor(kGreen)
	HadronicTopEnergyHist_Incorrect.SetLineColor(kRed)
	HadronicTopEnergyHist_Correct.SetLineColor(kBlue)
	HadronicTopEnergyHist_NotSemiLeptonic.SetFillColor(0)
	HadronicTopEnergyHist_NotReconstructible.SetFillColor(0)
	HadronicTopEnergyHist_Incorrect.SetFillColor(0)
	HadronicTopEnergyHist_Correct.SetFillColor(0)

	HadronicTopEnergyHist_Incorrect.Draw("")
	HadronicTopEnergyHist_NotSemiLeptonic.Draw("same")
	HadronicTopEnergyHist_NotReconstructible.Draw("same")
	HadronicTopEnergyHist_Correct.Draw("same")

	NormalisedHadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedHadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedHadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedHadronicTopEnergyleg.AddEntry(HadronicTopEnergyHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedHadronicTopEnergyleg.Draw()
	NormalisedHadronicTopEnergyCanvas.Update()
	NormalisedHadronicTopEnergyCanvas.SaveAs("plots/NormalisedHadronicTopEnergy.png")


	########## 			Leptonic Top Pt 			##########

	NormalisedLeptonicTopPtCanvas = TCanvas("NormalisedLeptonicTopPt","NormalisedLeptonicTopPt", 0, 0, 800, 600)
	NormalisedLeptonicTopPtleg = TLegend(0.5,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedLeptonicTopPtleg.SetFillColor(0)
	NormalisedLeptonicTopPtleg.SetLineColor(0)


	LeptonicTopPtHist_NotSemiLeptonic.SetLineColor(kMagenta)
	LeptonicTopPtHist_NotReconstructible.SetLineColor(kGreen)
	LeptonicTopPtHist_Incorrect.SetLineColor(kRed)
	LeptonicTopPtHist_Correct.SetLineColor(kBlue)
	LeptonicTopPtHist_NotSemiLeptonic.SetFillColor(0)
	LeptonicTopPtHist_NotReconstructible.SetFillColor(0)
	LeptonicTopPtHist_Incorrect.SetFillColor(0)
	LeptonicTopPtHist_Correct.SetFillColor(0)

	LeptonicTopPtHist_Incorrect.Draw("")
	LeptonicTopPtHist_NotReconstructible.Draw("same")
	LeptonicTopPtHist_NotSemiLeptonic.Draw("same")
	LeptonicTopPtHist_Correct.Draw("same")

	NormalisedLeptonicTopPtleg.AddEntry(LeptonicTopPtHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedLeptonicTopPtleg.AddEntry(LeptonicTopPtHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedLeptonicTopPtleg.AddEntry(LeptonicTopPtHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedLeptonicTopPtleg.AddEntry(LeptonicTopPtHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedLeptonicTopPtleg.Draw()
	NormalisedLeptonicTopPtCanvas.Update()
	NormalisedLeptonicTopPtCanvas.SaveAs("plots/NormalisedLeptonicTopPt.png")


	########## 			Leptonic Top Eta 			##########

	NormalisedLeptonicTopEtaCanvas = TCanvas("NormalisedLeptonicTopEta","NormalisedLeptonicTopEta", 0, 0, 800, 600)
	NormalisedLeptonicTopEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedLeptonicTopEtaleg.SetFillColor(0)
	NormalisedLeptonicTopEtaleg.SetLineColor(0)


	LeptonicTopEtaHist_NotSemiLeptonic.SetLineColor(kMagenta)
	LeptonicTopEtaHist_NotReconstructible.SetLineColor(kGreen)
	LeptonicTopEtaHist_Incorrect.SetLineColor(kRed)
	LeptonicTopEtaHist_Correct.SetLineColor(kBlue)
	LeptonicTopEtaHist_NotSemiLeptonic.SetFillColor(0)
	LeptonicTopEtaHist_NotReconstructible.SetFillColor(0)
	LeptonicTopEtaHist_Incorrect.SetFillColor(0)
	LeptonicTopEtaHist_Correct.SetFillColor(0)

	LeptonicTopEtaHist_Correct.Draw("")
	LeptonicTopEtaHist_Incorrect.Draw("same")
	LeptonicTopEtaHist_NotReconstructible.Draw("same")
	LeptonicTopEtaHist_NotSemiLeptonic.Draw("same")

	NormalisedLeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedLeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedLeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedLeptonicTopEtaleg.AddEntry(LeptonicTopEtaHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedLeptonicTopEtaleg.Draw()
	NormalisedLeptonicTopEtaCanvas.Update()
	NormalisedLeptonicTopEtaCanvas.SaveAs("plots/NormalisedLeptonicTopEta.png")


########## 			Leptonic Top Energy 			##########

	NormalisedLeptonicTopEnergyCanvas = TCanvas("NormalisedLeptonicTopEnergy","NormalisedLeptonicTopEnergy", 0, 0, 800, 600)
	NormalisedLeptonicTopEnergyleg = TLegend(0.15,0.65,0.45,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedLeptonicTopEnergyleg.SetFillColor(0)
	NormalisedLeptonicTopEnergyleg.SetLineColor(0)


	LeptonicTopEnergyHist_NotSemiLeptonic.SetLineColor(kMagenta)
	LeptonicTopEnergyHist_NotReconstructible.SetLineColor(kGreen)
	LeptonicTopEnergyHist_Incorrect.SetLineColor(kRed)
	LeptonicTopEnergyHist_Correct.SetLineColor(kBlue)
	LeptonicTopEnergyHist_NotSemiLeptonic.SetFillColor(0)
	LeptonicTopEnergyHist_NotReconstructible.SetFillColor(0)
	LeptonicTopEnergyHist_Incorrect.SetFillColor(0)
	LeptonicTopEnergyHist_Correct.SetFillColor(0)

	LeptonicTopEnergyHist_Incorrect.Draw("")
	LeptonicTopEnergyHist_NotSemiLeptonic.Draw("same")
	LeptonicTopEnergyHist_NotReconstructible.Draw("same")
	LeptonicTopEnergyHist_Correct.Draw("same")

	NormalisedLeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NormalisedLeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedLeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedLeptonicTopEnergyleg.AddEntry(LeptonicTopEnergyHist_Correct, "TTbar Right Reco" ,"le")

	NormalisedLeptonicTopEnergyleg.Draw()
	NormalisedLeptonicTopEnergyCanvas.Update()
	NormalisedLeptonicTopEnergyCanvas.SaveAs("plots/NormalisedLeptonicTopEnergy.png")

