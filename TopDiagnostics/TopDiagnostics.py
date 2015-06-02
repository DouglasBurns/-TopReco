'''
Created on 08 May 2015

@author: Douglas Burns

Plots CSV, MW.vs.MT, Neutrino Chi Test.

'''

import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1D, TH1F, TH2F, THStack, TCanvas, TPad, TAxis, TLegend, TLatex, kMagenta, kRed, kBlue, kGreen
import math

if __name__ == '__main__':


	########## 			SETUP 			##########
	gStyle.SetOptStat("")
	input_file = "../../data/tree_TTJet_5000pb_PFElectron_PFMuon_PF2PATJets_MET.root"
	
	Diff_TopPt_Hist_Correct = TH1D("Diff_TopPt_Correct","Diff_TopPt_Correct", 200, -90, 90)
	Diff_TopPt_Hist_Incorrect = TH1D("Diff_TopPt_Incorrect","Diff_TopPt_Incorrect", 200, -90, 90)
	# Diff_TopPt_Hist_NotSemiLeptonic = TH1D("Diff_TopPt_NotSemiLeptonic","Diff_TopPt_NotSemiLeptonic", 200, 0, 400)
	# Diff_TopPt_Hist_NotReconstructible = TH1D("Diff_TopPt_NotReconstructible","Diff_TopPt_NotReconstructible", 200, 0, 400)

	Diff_TopEta_Hist_Correct = TH1D("Diff_TopEta_Correct","Diff_TopEta_Correct", 200, -2, 2)
	Diff_TopEta_Hist_Incorrect = TH1D("Diff_TopEta_Incorrect","Diff_TopEta_Incorrect", 200, -2, 2)
	# Diff_TopEta_Hist_NotSemiLeptonic = TH1D("Diff_TopEta_NotSemiLeptonic","Diff_TopEta_NotSemiLeptonic", 200, -5, 5)
	# Diff_TopEta_Hist_NotReconstructible = TH1D("Diff_TopEta_NotReconstructible","Diff_TopEta_NotReconstructible", 200, -5, 5)

	Diff_TopEnergy_Hist_Correct = TH1D("Diff_TopEnergy_Correct","Diff_TopEnergy_Correct", 200, -150, 150)
	Diff_TopEnergy_Hist_Incorrect = TH1D("Diff_TopEnergy_Incorrect","Diff_TopEnergy_Incorrect", 200, -150, 150)
	# Diff_TopEnergy_Hist_NotSemiLeptonic = TH1D("Diff_TopEnergy_NotSemiLeptonic","Diff_TopEnergy_NotSemiLeptonic", 200, 0, 400)
	# Diff_TopEnergy_Hist_NotReconstructible = TH1D("Diff_TopEnergy_NotReconstructible","Diff_TopEnergy_NotReconstructible", 200, 0, 400)

	Diff_TopMass_Hist_Correct = TH1D("Diff_TopMass_Correct","Diff_TopMass_Correct", 200, -150, 150)
	Diff_TopMass_Hist_Incorrect = TH1D("Diff_TopMass_Incorrect","Diff_TopMass_Incorrect", 200, -150, 150)
	# Diff_TopMass_Hist_NotSemiLeptonic = TH1D("Diff_TopMass_NotSemiLeptonic","Diff_TopMass_NotSemiLeptonic", 200, 0, 400)
	# Diff_TopMass_Hist_NotReconstructible = TH1D("Diff_TopMass_NotReconstructible","Diff_TopMass_NotReconstructible", 200, 0, 400)

	Diff_WPt_Hist_Correct = TH1D("Diff_WPt_Correct","Diff_WPt_Correct", 200, -90, 90)
	Diff_WPt_Hist_Incorrect = TH1D("Diff_WPt_Incorrect","Diff_WPt_Incorrect", 200, -90, 90)
	# Diff_WPt_Hist_NotSemiLeptonic = TH1D("Diff_WPt_NotSemiLeptonic","Diff_WPt_NotSemiLeptonic", 200, 0, 400)
	# Diff_WPt_Hist_NotReconstructible = TH1D("Diff_WPt_NotReconstructible","Diff_WPt_NotReconstructible", 200, 0, 400)

	Diff_WEta_Hist_Correct = TH1D("Diff_WEta_Correct","Diff_WEta_Correct", 200, -2, 2)
	Diff_WEta_Hist_Incorrect = TH1D("Diff_WEta_Incorrect","Diff_WEta_Incorrect", 200, -2, 2)
	# Diff_WEta_Hist_NotSemiLeptonic = TH1D("Diff_WEta_NotSemiLeptonic","Diff_WEta_NotSemiLeptonic", 200, -5, 5)
	# Diff_WEta_Hist_NotReconstructible = TH1D("Diff_WEta_NotReconstructible","Diff_WEta_NotReconstructible", 200, -5, 5)

	Diff_WEnergy_Hist_Correct = TH1D("Diff_WEnergy_Correct","Diff_WEnergy_Correct", 200, -150, 150)
	Diff_WEnergy_Hist_Incorrect = TH1D("Diff_WEnergy_Incorrect","Diff_WEnergy_Incorrect", 200, -150, 150)
	# Diff_WEnergy_Hist_NotSemiLeptonic = TH1D("Diff_WEnergy_NotSemiLeptonic","Diff_WEnergy_NotSemiLeptonic", 200, 0, 400)
	# Diff_WEnergy_Hist_NotReconstructible = TH1D("Diff_WEnergy_NotReconstructible","Diff_WEnergy_NotReconstructible", 200, 0, 400)

	Diff_WMass_Hist_Correct = TH1D("Diff_WMass_Correct","Diff_WMass_Correct", 200, -150, 150)
	Diff_WMass_Hist_Incorrect = TH1D("Diff_WMass_Incorrect","Diff_WMass_Incorrect", 200, -150, 150)
	# Diff_WMass_Hist_NotSemiLeptonic = TH1D("Diff_WMass_NotSemiLeptonic","Diff_WMass_NotSemiLeptonic", 200, 0, 400)
	# Diff_WMass_Hist_NotReconstructible = TH1D("Diff_WMass_NotReconstructible","Diff_WMass_NotReconstructible", 200, 0, 400)
	
	Tree = "likelihood/Diagnostic"
	Tree_Solution = "likelihood/TopReco"

	# Tree_Solution = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/TopReco"

	Chain = TChain(Tree)
	Chain_Solution = TChain(Tree_Solution)
	Chain.Add(input_file)
	Chain_Solution.Add(input_file)
	Chain.AddFriend(Chain_Solution)
	Chain.SetBranchStatus("*",1)


	########## 			FILL HISTOGRAMS 		##########

	for event in Chain:

		Diff_TopPt = event.__getattr__("TopptDiff")
		Diff_TopEta = event.__getattr__("TopetaDiff")
		Diff_TopEnergy = event.__getattr__("TopenergyDiff")
		Diff_TopMass = event.__getattr__("TopmassDiff")

		Diff_WPt = event.__getattr__("WptDiff")
		Diff_WEta = event.__getattr__("WetaDiff")
		Diff_WEnergy = event.__getattr__("WenergyDiff")
		Diff_WMass = event.__getattr__("WmassDiff")

		# TypeofSolution = event.__getattr__("TypeofSolution")
		TypeofSolution = event.__getattr__("CorrectReconstruction")

		for index in range (0,len(TypeofSolution)):

			if (TypeofSolution[index] == 2):#Correct = 2
				Diff_TopPt_Hist_Correct.Fill(Diff_TopPt[index])
				Diff_TopEta_Hist_Correct.Fill(Diff_TopEta[index])
				Diff_TopEnergy_Hist_Correct.Fill(Diff_TopEnergy[index])
				Diff_TopMass_Hist_Correct.Fill(Diff_TopMass[index])
				Diff_WPt_Hist_Correct.Fill(Diff_WPt[index])
				Diff_WEta_Hist_Correct.Fill(Diff_WEta[index])
				Diff_WEnergy_Hist_Correct.Fill(Diff_WEnergy[index])
				Diff_WMass_Hist_Correct.Fill(Diff_WMass[index])

			if (TypeofSolution[index] == 0):#Reconstruction Chose Wrong Combination = 0
				Diff_TopPt_Hist_Incorrect.Fill(Diff_TopPt[index])
				Diff_TopEta_Hist_Incorrect.Fill(Diff_TopEta[index])
				Diff_TopEnergy_Hist_Incorrect.Fill(Diff_TopEnergy[index])
				Diff_TopMass_Hist_Incorrect.Fill(Diff_TopMass[index])
				Diff_WPt_Hist_Incorrect.Fill(Diff_WPt[index])
				Diff_WEta_Hist_Incorrect.Fill(Diff_WEta[index])
				Diff_WEnergy_Hist_Incorrect.Fill(Diff_WEnergy[index])
				Diff_WMass_Hist_Incorrect.Fill(Diff_WMass[index])

			# if (TypeofSolution == 3):#Event does not have all partons present = 3
				# Diff_TopPt_Hist_NotReconstructible.Fill(Diff_TopPt)
				# Diff_TopEta_Hist_NotReconstructible.Fill(Diff_TopEta)
				# Diff_TopEnergy_Hist_NotReconstructible.Fill(Diff_TopEnergy)
				# Diff_WPt_Hist_NotReconstructible.Fill(Diff_WPt)
				# Diff_WEta_Hist_NotReconstructible.Fill(Diff_WEta)
				# Diff_WEnergy_Hist_NotReconstructible.Fill(Diff_WEnergy)

			# if (TypeofSolution == 4):#Event is not semiLeptonic = 4
				# Diff_TopPt_Hist_NotSemiLeptonic.Fill(Diff_TopPt)
				# Diff_TopEta_Hist_NotSemiLeptonic.Fill(Diff_TopEta)
				# Diff_TopEnergy_Hist_NotSemiLeptonic.Fill(Diff_TopEnergy)
				# Diff_WPt_Hist_NotSemiLeptonic.Fill(Diff_WPt)
				# Diff_WEta_Hist_NotSemiLeptonic.Fill(Diff_WEta)
				# Diff_WEnergy_Hist_NotSemiLeptonic.Fill(Diff_WEnergy)

	########## 				NORMALISING 			##########

	# integral = LightJetCSVHist.Integral()
	# LightJetCSVHist.Scale(1/integral)

	########## 				PLOTTING Part1				##########


	file = TFile("TopDiagnostics.root", "RECREATE")


	########## 			Hadronic Top Pt Diff			##########

	Diff_TopPtCanvas = TCanvas("Diff_TopPt","Diff_TopPt", 0, 0, 800, 600)
	Diff_TopPtleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_TopPtleg.SetFillColor(0)
	Diff_TopPtleg.SetLineColor(0)

	Diff_TopPt_Stack = THStack("Diff_ Top Pt","Diff_ Top Pt")

	# Diff_TopPt_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_TopPtleg.AddEntry(Diff_TopPt_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_TopPt_Stack.Add(Diff_TopPt_Hist_NotSemiLeptonic)

	# Diff_TopPt_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_TopPtleg.AddEntry(Diff_TopPt_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_TopPt_Stack.Add(Diff_TopPt_Hist_NotReconstructible)

	Diff_TopPt_Hist_Incorrect.SetFillColor(kRed)
	Diff_TopPtleg.AddEntry(Diff_TopPt_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_TopPt_Stack.Add(Diff_TopPt_Hist_Incorrect)

	Diff_TopPt_Hist_Correct.SetFillColor(kBlue)
	Diff_TopPtleg.AddEntry(Diff_TopPt_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_TopPt_Stack.Add(Diff_TopPt_Hist_Correct)

	Diff_TopPt_Stack.Draw()
	Diff_TopPtleg.Draw()
	Diff_TopPtCanvas.Update()
	Diff_TopPtCanvas.SaveAs("plots/Diff_TopPt.png")

	Diff_TopPt_Stack.Write()
	Diff_TopPt_Hist_Correct.Write()
	Diff_TopPt_Hist_Incorrect.Write()
	# Diff_TopPt_Hist_NotReconstructible.Write()
	# Diff_TopPt_Hist_NotSemiLeptonic.Write()

	########## 			Hadronic Top Eta Diff			##########

	Diff_TopEtaCanvas = TCanvas("Diff_TopEta","Diff_TopEta", 0, 0, 800, 600)
	Diff_TopEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_TopEtaleg.SetFillColor(0)
	Diff_TopEtaleg.SetLineColor(0)

	Diff_TopEta_Stack = THStack("Diff_ Top Eta","Diff_ Top Eta")

	# Diff_TopEta_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_TopEtaleg.AddEntry(Diff_TopEta_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_TopEta_Stack.Add(Diff_TopEta_Hist_NotSemiLeptonic)

	# Diff_TopEta_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_TopEtaleg.AddEntry(Diff_TopEta_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_TopEta_Stack.Add(Diff_TopEta_Hist_NotReconstructible)

	Diff_TopEta_Hist_Incorrect.SetFillColor(kRed)
	Diff_TopEtaleg.AddEntry(Diff_TopEta_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_TopEta_Stack.Add(Diff_TopEta_Hist_Incorrect)

	Diff_TopEta_Hist_Correct.SetFillColor(kBlue)
	Diff_TopEtaleg.AddEntry(Diff_TopEta_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_TopEta_Stack.Add(Diff_TopEta_Hist_Correct)

	Diff_TopEta_Stack.Draw()
	Diff_TopEtaleg.Draw()
	Diff_TopEtaCanvas.Update()
	Diff_TopEtaCanvas.SaveAs("plots/Diff_TopEta.png")

	Diff_TopEta_Stack.Write()
	Diff_TopEta_Hist_Correct.Write()
	Diff_TopEta_Hist_Incorrect.Write()
	# Diff_TopEta_Hist_NotReconstructible.Write()
	# Diff_TopEta_Hist_NotSemiLeptonic.Write()

	########## 			Hadronic Top Energy Diff			##########

	Diff_TopEnergyCanvas = TCanvas("Diff_TopEnergy","Diff_TopEnergy", 0, 0, 800, 600)
	Diff_TopEnergyleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_TopEnergyleg.SetFillColor(0)
	Diff_TopEnergyleg.SetLineColor(0)

	Diff_TopEnergy_Stack = THStack("Diff_ Top Energy","Diff_ Top Energy")

	# Diff_TopEnergy_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_TopEnergy_Stack.Add(Diff_TopEnergy_Hist_NotSemiLeptonic)

	# Diff_TopEnergy_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_TopEnergy_Stack.Add(Diff_TopEnergy_Hist_NotReconstructible)

	Diff_TopEnergy_Hist_Incorrect.SetFillColor(kRed)
	Diff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_TopEnergy_Stack.Add(Diff_TopEnergy_Hist_Incorrect)

	Diff_TopEnergy_Hist_Correct.SetFillColor(kBlue)
	Diff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_TopEnergy_Stack.Add(Diff_TopEnergy_Hist_Correct)

	Diff_TopEnergy_Stack.Draw()
	Diff_TopEnergyleg.Draw()
	Diff_TopEnergyCanvas.Update()
	Diff_TopEnergyCanvas.SaveAs("plots/Diff_TopEnergy.png")

	Diff_TopEnergy_Stack.Write()
	Diff_TopEnergy_Hist_Correct.Write()
	Diff_TopEnergy_Hist_Incorrect.Write()
	# Diff_TopEnergy_Hist_NotReconstructible.Write()
	# Diff_TopEnergy_Hist_NotSemiLeptonic.Write()

		########## 			Hadronic Top Mass Diff			##########

	Diff_TopMassCanvas = TCanvas("Diff_TopMass","Diff_TopMass", 0, 0, 800, 600)
	Diff_TopMassleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_TopMassleg.SetFillColor(0)
	Diff_TopMassleg.SetLineColor(0)

	Diff_TopMass_Stack = THStack("Diff_ Top Mass","Diff_ Top Mass")

	# Diff_TopMass_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_TopMassleg.AddEntry(Diff_TopMass_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_TopMass_Stack.Add(Diff_TopMass_Hist_NotSemiLeptonic)

	# Diff_TopMass_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_TopMassleg.AddEntry(Diff_TopMass_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_TopMass_Stack.Add(Diff_TopMass_Hist_NotReconstructible)

	Diff_TopMass_Hist_Incorrect.SetFillColor(kRed)
	Diff_TopMassleg.AddEntry(Diff_TopMass_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_TopMass_Stack.Add(Diff_TopMass_Hist_Incorrect)

	Diff_TopMass_Hist_Correct.SetFillColor(kBlue)
	Diff_TopMassleg.AddEntry(Diff_TopMass_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_TopMass_Stack.Add(Diff_TopMass_Hist_Correct)

	Diff_TopMass_Stack.Draw()
	Diff_TopMassleg.Draw()
	Diff_TopMassCanvas.Update()
	Diff_TopMassCanvas.SaveAs("plots/Diff_TopMass.png")

	Diff_TopMass_Stack.Write()
	Diff_TopMass_Hist_Correct.Write()
	Diff_TopMass_Hist_Incorrect.Write()
	# Diff_TopMass_Hist_NotReconstructible.Write()
	# Diff_TopMass_Hist_NotSemiLeptonic.Write()

	########## 			Hadronic W Pt Diff			##########

	Diff_WPtCanvas = TCanvas("Diff_WPt","Diff_WPt", 0, 0, 800, 600)
	Diff_WPtleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_WPtleg.SetFillColor(0)
	Diff_WPtleg.SetLineColor(0)

	Diff_WPt_Stack = THStack("Diff_ W Pt","Diff_ W Pt")

	# Diff_WPt_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_WPtleg.AddEntry(Diff_WPt_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_WPt_Stack.Add(Diff_WPt_Hist_NotSemiLeptonic)

	# Diff_WPt_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_WPtleg.AddEntry(Diff_WPt_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_WPt_Stack.Add(Diff_WPt_Hist_NotReconstructible)

	Diff_WPt_Hist_Incorrect.SetFillColor(kRed)
	Diff_WPtleg.AddEntry(Diff_WPt_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_WPt_Stack.Add(Diff_WPt_Hist_Incorrect)

	Diff_WPt_Hist_Correct.SetFillColor(kBlue)
	Diff_WPtleg.AddEntry(Diff_WPt_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_WPt_Stack.Add(Diff_WPt_Hist_Correct)

	Diff_WPt_Stack.Draw()
	Diff_WPtleg.Draw()
	Diff_WPtCanvas.Update()
	Diff_WPtCanvas.SaveAs("plots/Diff_WPt.png")

	Diff_WPt_Stack.Write()
	Diff_WPt_Hist_Correct.Write()
	Diff_WPt_Hist_Incorrect.Write()
	# Diff_WPt_Hist_NotReconstructible.Write()
	# Diff_WPt_Hist_NotSemiLeptonic.Write()

	########## 			Hadronic W Eta Diff			##########

	Diff_WEtaCanvas = TCanvas("Diff_WEta","Diff_WEta", 0, 0, 800, 600)
	Diff_WEtaleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_WEtaleg.SetFillColor(0)
	Diff_WEtaleg.SetLineColor(0)

	Diff_WEta_Stack = THStack("Diff_ W Eta","Diff_ W Eta")

	# Diff_WEta_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_WEtaleg.AddEntry(Diff_WEta_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_WEta_Stack.Add(Diff_WEta_Hist_NotSemiLeptonic)

	# Diff_WEta_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_WEtaleg.AddEntry(Diff_WEta_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_WEta_Stack.Add(Diff_WEta_Hist_NotReconstructible)

	Diff_WEta_Hist_Incorrect.SetFillColor(kRed)
	Diff_WEtaleg.AddEntry(Diff_WEta_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_WEta_Stack.Add(Diff_WEta_Hist_Incorrect)

	Diff_WEta_Hist_Correct.SetFillColor(kBlue)
	Diff_WEtaleg.AddEntry(Diff_WEta_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_WEta_Stack.Add(Diff_WEta_Hist_Correct)

	Diff_WEta_Stack.Draw()
	Diff_WEtaleg.Draw()
	Diff_WEtaCanvas.Update()
	Diff_WEtaCanvas.SaveAs("plots/Diff_WEta.png")

	Diff_WEta_Stack.Write()
	Diff_WEta_Hist_Correct.Write()
	Diff_WEta_Hist_Incorrect.Write()
	# Diff_WEta_Hist_NotReconstructible.Write()
	# Diff_WEta_Hist_NotSemiLeptonic.Write()

	########## 			Hadronic W Energy Diff			##########

	Diff_WEnergyCanvas = TCanvas("Diff_WEnergy","Diff_WEnergy", 0, 0, 800, 600)
	Diff_WEnergyleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_WEnergyleg.SetFillColor(0)
	Diff_WEnergyleg.SetLineColor(0)

	Diff_WEnergy_Stack = THStack("Diff_ W Energy","Diff_ W Energy")

	# Diff_WEnergy_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_WEnergy_Stack.Add(Diff_WEnergy_Hist_NotSemiLeptonic)

	# Diff_WEnergy_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_WEnergy_Stack.Add(Diff_WEnergy_Hist_NotReconstructible)

	Diff_WEnergy_Hist_Incorrect.SetFillColor(kRed)
	Diff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_WEnergy_Stack.Add(Diff_WEnergy_Hist_Incorrect)

	Diff_WEnergy_Hist_Correct.SetFillColor(kBlue)
	Diff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_WEnergy_Stack.Add(Diff_WEnergy_Hist_Correct)

	Diff_WEnergy_Stack.Draw()
	Diff_WEnergyleg.Draw()
	Diff_WEnergyCanvas.Update()
	Diff_WEnergyCanvas.SaveAs("plots/Diff_WEnergy.png")

	Diff_WEnergy_Stack.Write()
	Diff_WEnergy_Hist_Correct.Write()
	Diff_WEnergy_Hist_Incorrect.Write()
	# Diff_WEnergy_Hist_NotReconstructible.Write()
	# Diff_WEnergy_Hist_NotSemiLeptonic.Write()

		########## 			Hadronic W Mass Diff			##########

	Diff_WMassCanvas = TCanvas("Diff_WMass","Diff_WMass", 0, 0, 800, 600)
	Diff_WMassleg = TLegend(0.7,0.5,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Diff_WMassleg.SetFillColor(0)
	Diff_WMassleg.SetLineColor(0)

	Diff_WMass_Stack = THStack("Diff_ W Mass","Diff_ W Mass")

	# Diff_WMass_Hist_NotSemiLeptonic.SetFillColor(kMagenta)
	# Diff_WMassleg.AddEntry(Diff_WMass_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"f")
	# Diff_WMass_Stack.Add(Diff_WMass_Hist_NotSemiLeptonic)

	# Diff_WMass_Hist_NotReconstructible.SetFillColor(kGreen)
	# Diff_WMassleg.AddEntry(Diff_WMass_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"f")
	# Diff_WMass_Stack.Add(Diff_WMass_Hist_NotReconstructible)

	Diff_WMass_Hist_Incorrect.SetFillColor(kRed)
	Diff_WMassleg.AddEntry(Diff_WMass_Hist_Incorrect, "TTbar Wrong Reco" ,"f")
	Diff_WMass_Stack.Add(Diff_WMass_Hist_Incorrect)

	Diff_WMass_Hist_Correct.SetFillColor(kBlue)
	Diff_WMassleg.AddEntry(Diff_WMass_Hist_Correct, "TTbar Right Reco" ,"f")
	Diff_WMass_Stack.Add(Diff_WMass_Hist_Correct)

	Diff_WMass_Stack.Draw()
	Diff_WMassleg.Draw()
	Diff_WMassCanvas.Update()
	Diff_WMassCanvas.SaveAs("plots/Diff_WMass.png")

	Diff_WMass_Stack.Write()
	Diff_WMass_Hist_Correct.Write()
	Diff_WMass_Hist_Incorrect.Write()
	# Diff_WMass_Hist_NotReconstructible.Write()
	# Diff_WMass_Hist_NotSemiLeptonic.Write()

	
	##########			PLOTS SUPERIMPOSED			##########

	########## 				NORMALISING 			##########

	integral = Diff_TopPt_Hist_Correct.Integral()
	Diff_TopPt_Hist_Correct.Scale(1/integral)
	integral = Diff_TopEta_Hist_Correct.Integral()
	Diff_TopEta_Hist_Correct.Scale(1/integral)
	integral = Diff_TopEnergy_Hist_Correct.Integral()
	Diff_TopEnergy_Hist_Correct.Scale(1/integral)
	integral = Diff_TopMass_Hist_Correct.Integral()
	Diff_TopMass_Hist_Correct.Scale(1/integral)

	integral = Diff_WPt_Hist_Correct.Integral()
	Diff_WPt_Hist_Correct.Scale(1/integral)
	integral = Diff_WEta_Hist_Correct.Integral()
	Diff_WEta_Hist_Correct.Scale(1/integral)
	integral = Diff_WEnergy_Hist_Correct.Integral()
	Diff_WEnergy_Hist_Correct.Scale(1/integral)
	integral = Diff_WMass_Hist_Correct.Integral()
	Diff_WMass_Hist_Correct.Scale(1/integral)


	integral = Diff_TopPt_Hist_Incorrect.Integral()
	Diff_TopPt_Hist_Incorrect.Scale(1/integral)
	integral = Diff_TopEta_Hist_Incorrect.Integral()
	Diff_TopEta_Hist_Incorrect.Scale(1/integral)
	integral = Diff_TopEnergy_Hist_Incorrect.Integral()
	Diff_TopEnergy_Hist_Incorrect.Scale(1/integral)
	integral = Diff_TopMass_Hist_Incorrect.Integral()
	Diff_TopMass_Hist_Incorrect.Scale(1/integral)

	integral = Diff_WPt_Hist_Incorrect.Integral()
	Diff_WPt_Hist_Incorrect.Scale(1/integral)
	integral = Diff_WEta_Hist_Incorrect.Integral()
	Diff_WEta_Hist_Incorrect.Scale(1/integral)
	integral = Diff_WEnergy_Hist_Incorrect.Integral()
	Diff_WEnergy_Hist_Incorrect.Scale(1/integral)
	integral = Diff_WMass_Hist_Incorrect.Integral()
	Diff_WMass_Hist_Incorrect.Scale(1/integral)


	# integral = Diff_TopPt_Hist_NotReconstructible.Integral()
	# Diff_TopPt_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_TopEta_Hist_NotReconstructible.Integral()
	# Diff_TopEta_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_TopEnergy_Hist_NotReconstructible.Integral()
	# Diff_TopEnergy_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_TopMass_Hist_NotReconstructible.Integral()
	# Diff_TopMass_Hist_NotReconstructible.Scale(1/integral)

	# integral = Diff_WPt_Hist_NotReconstructible.Integral()
	# Diff_WPt_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_WEta_Hist_NotReconstructible.Integral()
	# Diff_WEta_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_WEnergy_Hist_NotReconstructible.Integral()
	# Diff_WEnergy_Hist_NotReconstructible.Scale(1/integral)
	# integral = Diff_WMass_Hist_NotReconstructible.Integral()
	# Diff_WMass_Hist_NotReconstructible.Scale(1/integral)


	# integral = Diff_TopPt_Hist_NotSemiLeptonic.Integral()
	# Diff_TopPt_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_TopEta_Hist_NotSemiLeptonic.Integral()
	# Diff_TopEta_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_TopEnergy_Hist_NotSemiLeptonic.Integral()
	# Diff_TopEnergy_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_TopMass_Hist_NotSemiLeptonic.Integral()
	# Diff_TopMass_Hist_NotSemiLeptonic.Scale(1/integral)

	# integral = Diff_WPt_Hist_NotSemiLeptonic.Integral()	
	# Diff_WPt_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_WEta_Hist_NotSemiLeptonic.Integral()
	# Diff_WEta_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_WEnergy_Hist_NotSemiLeptonic.Integral()
	# Diff_WEnergy_Hist_NotSemiLeptonic.Scale(1/integral)
	# integral = Diff_WMass_Hist_NotSemiLeptonic.Integral()
	# Diff_WMass_Hist_NotSemiLeptonic.Scale(1/integral)



	########## 			Hadronic Top Pt 			##########

	NormalisedDiff_TopPtCanvas = TCanvas("NormalisedDiff_TopPt","NormalisedDiff_TopPt", 0, 0, 800, 600)
	NormalisedDiff_TopPtleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_TopPtleg.SetFillColor(0)
	NormalisedDiff_TopPtleg.SetLineColor(0)

	# Diff_TopPt_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_TopPt_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_TopPt_Hist_Incorrect.SetLineColor(kRed)
	Diff_TopPt_Hist_Correct.SetLineColor(kBlue)
	# Diff_TopPt_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_TopPt_Hist_NotReconstructible.SetFillColor(0)
	Diff_TopPt_Hist_Incorrect.SetFillColor(0)
	Diff_TopPt_Hist_Correct.SetFillColor(0)

	Diff_TopPt_Hist_Incorrect.Draw("")
	# Diff_TopPt_Hist_NotReconstructible.Draw("same")
	# Diff_TopPt_Hist_NotSemiLeptonic.Draw("same")
	Diff_TopPt_Hist_Correct.Draw("same")

	# NormalisedDiff_TopPtleg.AddEntry(Diff_TopPt_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_TopPtleg.AddEntry(Diff_TopPt_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_TopPtleg.AddEntry(Diff_TopPt_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_TopPtleg.AddEntry(Diff_TopPt_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_TopPtleg.Draw()
	NormalisedDiff_TopPtCanvas.Update()
	NormalisedDiff_TopPtCanvas.SaveAs("plots/NormalisedDiff_TopPt.png")

	########## 			Hadronic Top Eta 			##########

	NormalisedDiff_TopEtaCanvas = TCanvas("NormalisedDiff_TopEta","NormalisedDiff_TopEta", 0, 0, 800, 600)
	NormalisedDiff_TopEtaleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_TopEtaleg.SetFillColor(0)
	NormalisedDiff_TopEtaleg.SetLineColor(0)

	# Diff_TopEta_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_TopEta_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_TopEta_Hist_Incorrect.SetLineColor(kRed)
	Diff_TopEta_Hist_Correct.SetLineColor(kBlue)
	# Diff_TopEta_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_TopEta_Hist_NotReconstructible.SetFillColor(0)
	Diff_TopEta_Hist_Incorrect.SetFillColor(0)
	Diff_TopEta_Hist_Correct.SetFillColor(0)

	Diff_TopEta_Hist_Incorrect.Draw("")
	# Diff_TopEta_Hist_NotReconstructible.Draw("same")
	# Diff_TopEta_Hist_NotSemiLeptonic.Draw("same")
	Diff_TopEta_Hist_Correct.Draw("same")

	# NormalisedDiff_TopEtaleg.AddEntry(Diff_TopEta_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_TopEtaleg.AddEntry(Diff_TopEta_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_TopEtaleg.AddEntry(Diff_TopEta_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_TopEtaleg.AddEntry(Diff_TopEta_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_TopEtaleg.Draw()
	NormalisedDiff_TopEtaCanvas.Update()
	NormalisedDiff_TopEtaCanvas.SaveAs("plots/NormalisedDiff_TopEta.png")

	########## 			Hadronic Top Energy 			##########

	NormalisedDiff_TopEnergyCanvas = TCanvas("NormalisedDiff_TopEnergy","NormalisedDiff_TopEnergy", 0, 0, 800, 600)
	NormalisedDiff_TopEnergyleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_TopEnergyleg.SetFillColor(0)
	NormalisedDiff_TopEnergyleg.SetLineColor(0)

	# Diff_TopEnergy_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_TopEnergy_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_TopEnergy_Hist_Incorrect.SetLineColor(kRed)
	Diff_TopEnergy_Hist_Correct.SetLineColor(kBlue)
	# Diff_TopEnergy_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_TopEnergy_Hist_NotReconstructible.SetFillColor(0)
	Diff_TopEnergy_Hist_Incorrect.SetFillColor(0)
	Diff_TopEnergy_Hist_Correct.SetFillColor(0)

	Diff_TopEnergy_Hist_Incorrect.Draw("")
	# Diff_TopEnergy_Hist_NotReconstructible.Draw("same")
	# Diff_TopEnergy_Hist_NotSemiLeptonic.Draw("same")
	Diff_TopEnergy_Hist_Correct.Draw("same")

	# NormalisedDiff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_TopEnergyleg.AddEntry(Diff_TopEnergy_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_TopEnergyleg.Draw()
	NormalisedDiff_TopEnergyCanvas.Update()
	NormalisedDiff_TopEnergyCanvas.SaveAs("plots/NormalisedDiff_TopEnergy.png")

	########## 			Hadronic Top Mass 			##########

	NormalisedDiff_TopMassCanvas = TCanvas("NormalisedDiff_TopMass","NormalisedDiff_TopMass", 0, 0, 800, 600)
	NormalisedDiff_TopMassleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_TopMassleg.SetFillColor(0)
	NormalisedDiff_TopMassleg.SetLineColor(0)

	# Diff_TopMass_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_TopMass_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_TopMass_Hist_Incorrect.SetLineColor(kRed)
	Diff_TopMass_Hist_Correct.SetLineColor(kBlue)
	# Diff_TopMass_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_TopMass_Hist_NotReconstructible.SetFillColor(0)
	Diff_TopMass_Hist_Incorrect.SetFillColor(0)
	Diff_TopMass_Hist_Correct.SetFillColor(0)

	Diff_TopMass_Hist_Incorrect.Draw("")
	# Diff_TopMass_Hist_NotReconstructible.Draw("same")
	# Diff_TopMass_Hist_NotSemiLeptonic.Draw("same")
	Diff_TopMass_Hist_Correct.Draw("same")

	# NormalisedDiff_TopMassleg.AddEntry(Diff_TopMass_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_TopMassleg.AddEntry(Diff_TopMass_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_TopMassleg.AddEntry(Diff_TopMass_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_TopMassleg.AddEntry(Diff_TopMass_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_TopMassleg.Draw()
	NormalisedDiff_TopMassCanvas.Update()
	NormalisedDiff_TopMassCanvas.SaveAs("plots/NormalisedDiff_TopMass.png")

	########## 			Hadronic W Pt 			##########

	NormalisedDiff_WPtCanvas = TCanvas("NormalisedDiff_WPt","NormalisedDiff_WPt", 0, 0, 800, 600)
	NormalisedDiff_WPtleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_WPtleg.SetFillColor(0)
	NormalisedDiff_WPtleg.SetLineColor(0)

	# Diff_WPt_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_WPt_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_WPt_Hist_Incorrect.SetLineColor(kRed)
	Diff_WPt_Hist_Correct.SetLineColor(kBlue)
	# Diff_WPt_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_WPt_Hist_NotReconstructible.SetFillColor(0)
	Diff_WPt_Hist_Incorrect.SetFillColor(0)
	Diff_WPt_Hist_Correct.SetFillColor(0)

	Diff_WPt_Hist_Incorrect.Draw("")
	# Diff_WPt_Hist_NotReconstructible.Draw("same")
	# Diff_WPt_Hist_NotSemiLeptonic.Draw("same")
	Diff_WPt_Hist_Correct.Draw("same")

	# NormalisedDiff_WPtleg.AddEntry(Diff_WPt_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_WPtleg.AddEntry(Diff_WPt_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_WPtleg.AddEntry(Diff_WPt_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_WPtleg.AddEntry(Diff_WPt_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_WPtleg.Draw()
	NormalisedDiff_WPtCanvas.Update()
	NormalisedDiff_WPtCanvas.SaveAs("plots/NormalisedDiff_WPt.png")

	########## 			Hadronic W Eta 			##########

	NormalisedDiff_WEtaCanvas = TCanvas("NormalisedDiff_WEta","NormalisedDiff_WEta", 0, 0, 800, 600)
	NormalisedDiff_WEtaleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_WEtaleg.SetFillColor(0)
	NormalisedDiff_WEtaleg.SetLineColor(0)

	# Diff_WEta_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_WEta_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_WEta_Hist_Incorrect.SetLineColor(kRed)
	Diff_WEta_Hist_Correct.SetLineColor(kBlue)
	# Diff_WEta_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_WEta_Hist_NotReconstructible.SetFillColor(0)
	Diff_WEta_Hist_Incorrect.SetFillColor(0)
	Diff_WEta_Hist_Correct.SetFillColor(0)

	Diff_WEta_Hist_Incorrect.Draw("")
	# Diff_WEta_Hist_NotReconstructible.Draw("same")
	# Diff_WEta_Hist_NotSemiLeptonic.Draw("same")
	Diff_WEta_Hist_Correct.Draw("same")

	# NormalisedDiff_WEtaleg.AddEntry(Diff_WEta_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_WEtaleg.AddEntry(Diff_WEta_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_WEtaleg.AddEntry(Diff_WEta_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_WEtaleg.AddEntry(Diff_WEta_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_WEtaleg.Draw()
	NormalisedDiff_WEtaCanvas.Update()
	NormalisedDiff_WEtaCanvas.SaveAs("plots/NormalisedDiff_WEta.png")

	########## 			Hadronic W Energy 			##########

	NormalisedDiff_WEnergyCanvas = TCanvas("NormalisedDiff_WEnergy","NormalisedDiff_WEnergy", 0, 0, 800, 600)
	NormalisedDiff_WEnergyleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_WEnergyleg.SetFillColor(0)
	NormalisedDiff_WEnergyleg.SetLineColor(0)

	# Diff_WEnergy_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_WEnergy_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_WEnergy_Hist_Incorrect.SetLineColor(kRed)
	Diff_WEnergy_Hist_Correct.SetLineColor(kBlue)
	# Diff_WEnergy_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_WEnergy_Hist_NotReconstructible.SetFillColor(0)
	Diff_WEnergy_Hist_Incorrect.SetFillColor(0)
	Diff_WEnergy_Hist_Correct.SetFillColor(0)

	Diff_WEnergy_Hist_Incorrect.Draw("")
	# Diff_WEnergy_Hist_NotReconstructible.Draw("same")
	# Diff_WEnergy_Hist_NotSemiLeptonic.Draw("same")
	Diff_WEnergy_Hist_Correct.Draw("same")

	# NormalisedDiff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_WEnergyleg.AddEntry(Diff_WEnergy_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_WEnergyleg.Draw()
	NormalisedDiff_WEnergyCanvas.Update()
	NormalisedDiff_WEnergyCanvas.SaveAs("plots/NormalisedDiff_WEnergy.png")

	########## 			Hadronic W Mass 			##########

	NormalisedDiff_WMassCanvas = TCanvas("NormalisedDiff_WMass","NormalisedDiff_WMass", 0, 0, 800, 600)
	NormalisedDiff_WMassleg = TLegend(0.7,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NormalisedDiff_WMassleg.SetFillColor(0)
	NormalisedDiff_WMassleg.SetLineColor(0)

	# Diff_WMass_Hist_NotSemiLeptonic.SetLineColor(kMagenta)
	# Diff_WMass_Hist_NotReconstructible.SetLineColor(kGreen)
	Diff_WMass_Hist_Incorrect.SetLineColor(kRed)
	Diff_WMass_Hist_Correct.SetLineColor(kBlue)
	# Diff_WMass_Hist_NotSemiLeptonic.SetFillColor(0)
	# Diff_WMass_Hist_NotReconstructible.SetFillColor(0)
	Diff_WMass_Hist_Incorrect.SetFillColor(0)
	Diff_WMass_Hist_Correct.SetFillColor(0)

	Diff_WMass_Hist_Incorrect.Draw("")
	# Diff_WMass_Hist_NotReconstructible.Draw("same")
	# Diff_WMass_Hist_NotSemiLeptonic.Draw("same")
	Diff_WMass_Hist_Correct.Draw("same")

	# NormalisedDiff_WMassleg.AddEntry(Diff_WMass_Hist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	# NormalisedDiff_WMassleg.AddEntry(Diff_WMass_Hist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NormalisedDiff_WMassleg.AddEntry(Diff_WMass_Hist_Incorrect, "TTbar Wrong Reco" ,"le")
	NormalisedDiff_WMassleg.AddEntry(Diff_WMass_Hist_Correct, "TTbar Right Reco" ,"le")

	NormalisedDiff_WMassleg.Draw()
	NormalisedDiff_WMassCanvas.Update()
	NormalisedDiff_WMassCanvas.SaveAs("plots/NormalisedDiff_WMass.png")
	