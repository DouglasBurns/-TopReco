'''
Created on 08 May 2015

@author: Douglas Burns

Plots CSV, MW.vs.MT, Neutrino Chi Test.

'''

import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1F, TH2F, TCanvas, TPad, TAxis, TLegend, TLatex, kRed, kBlue, kGreen, kMagenta
import math

if __name__ == '__main__':


	########## 			SETUP 			##########
	gStyle.SetOptStat("")
	input_file = "../../data/tree_TTJet_5000pb_PFElectron_PFMuon_PF2PATJets_MET.root"

	MassDiscrimHist_Correct = TH1F("MassDiscrimHist_Correct","MassDiscrimHist_Correct", 100, -4, 2)
	MassDiscrimHist_Incorrect = TH1F("MassDiscrimHist_Incorrect","MassDiscrimHist_Incorrect", 100, -4, 2)
	MassDiscrimHist_NotSemiLeptonic = TH1F("MassDiscrimHist_NotSemiLeptonic","MassDiscrimHist_NotSemiLeptonic", 100, -4, 2)
	MassDiscrimHist_NotReconstructible = TH1F("MassDiscrimHist_NotReconstructible","MassDiscrimHist_NotReconstructible", 100, -4, 2)
	MassDiscrimHist_Total = TH1F("MassDiscrimHist_Total","MassDiscrimHist_Total", 100, -4, 2)

	CSVDiscrimHist_Correct = TH1F("CSVDiscrimHist_Correct","CSVDiscrimHist_Correct", 100, -10, 0)
	CSVDiscrimHist_Incorrect = TH1F("CSVDiscrimHist_Incorrect","CSVDiscrimHist_Incorrect", 100, -10, 0)
	CSVDiscrimHist_NotSemiLeptonic = TH1F("CSVDiscrimHist_NotSemiLeptonic","CSVDiscrimHist_NotSemiLeptonic", 100, -10, 0)
	CSVDiscrimHist_NotReconstructible = TH1F("CSVDiscrimHist_NotReconstructible","CSVDiscrimHist_NotReconstructible", 100, -10, 0)
	CSVDiscrimHist_Total = TH1F("CSVDiscrimHist_Total","CSVDiscrimHist_Total", 100, -10, 0)

	NuChi2DiscrimHist_Correct = TH1F("NuChi2DiscrimHist_Correct","NuChi2DiscrimHist_Correct", 100, -0.5, 0.8)
	NuChi2DiscrimHist_Incorrect = TH1F("NuChi2DiscrimHist_Incorrect","NuChi2DiscrimHist_Incorrect", 100, -0.5, 0.8)
	NuChi2DiscrimHist_NotSemiLeptonic = TH1F("NuChi2DiscrimHist_NotSemiLeptonic","NuChi2DiscrimHist_NotSemiLeptonic", 100, -0.5, 0.8)
	NuChi2DiscrimHist_NotReconstructible = TH1F("NuChi2DiscrimHist_NotReconstructible","NuChi2DiscrimHist_NotReconstructible", 100, -0.5, 0.8)
	NuChi2DiscrimHist_Total = TH1F("NuChi2DiscrimHist_Total","NuChi2DiscrimHist_Total", 100, -0.5, 0.8)

	AllDiscrimHist_Correct = TH1F("AllDiscrimHist_Correct","AllDiscrimHist_Correct", 100, -15, 0)
	AllDiscrimHist_Incorrect = TH1F("AllDiscrimHist_Incorrect","AllDiscrimHist_Incorrect", 100, -15, 0)
	AllDiscrimHist_NotSemiLeptonic = TH1F("AllDiscrimHist_NotSemiLeptonic","AllDiscrimHist_NotSemiLeptonic", 100, -15, 0)
	AllDiscrimHist_NotReconstructible = TH1F("AllDiscrimHist_NotReconstructible","AllDiscrimHist_NotReconstructible", 100, -15, 0)
	AllDiscrimHist_Total = TH1F("AllDiscrimHist_Total","AllDiscrimHist_Total", 100, -15, 0)



	# inputTree = TTree(input_file.get("Discriminator"))
	inputTree = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/Discriminator"
	inputTreeSolution = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/TopReco"

	Chain = TChain(inputTree)
	Chain.Add(input_file)
	ChainSolution = TChain(inputTreeSolution)
	ChainSolution.Add(input_file)

	Chain.AddFriend(ChainSolution)

	Chain.SetBranchStatus("*",1)


	########## 			FILL HISTOGRAMS 		##########

	for event in Chain:

		MassDiscrim = event.__getattr__("MassDiscrimBest")
		CSVDiscrim = event.__getattr__("CSVDiscrimBest")
		NuChi2Discrim = event.__getattr__("NuChi2DiscrimBest")
		AllDiscrim = event.__getattr__("likelihoodRatioDiscrimBest")
		# TrueEventReconstruction = event.__getattr__("EventReconstruction")
		TypeofSolution = event.__getattr__("TypeofSolution")

		MassDiscrimHist_Total.Fill(MassDiscrim)
		CSVDiscrimHist_Total.Fill(CSVDiscrim)
		NuChi2DiscrimHist_Total.Fill(NuChi2Discrim)
		AllDiscrimHist_Total.Fill(AllDiscrim)

		if (TypeofSolution == 1):#Correct = 1
			MassDiscrimHist_Correct.Fill(MassDiscrim)
			CSVDiscrimHist_Correct.Fill(CSVDiscrim)
			NuChi2DiscrimHist_Correct.Fill(NuChi2Discrim)
			AllDiscrimHist_Correct.Fill(AllDiscrim)

		if (TypeofSolution == 2):#Reconstruction Chose Wrong Combination = 2
			MassDiscrimHist_Incorrect.Fill(MassDiscrim)
			CSVDiscrimHist_Incorrect.Fill(CSVDiscrim)
			NuChi2DiscrimHist_Incorrect.Fill(NuChi2Discrim)
			AllDiscrimHist_Incorrect.Fill(AllDiscrim)

		if (TypeofSolution == 3):#Event does not have all partons present = 3
			MassDiscrimHist_NotSemiLeptonic.Fill(MassDiscrim)
			CSVDiscrimHist_NotSemiLeptonic.Fill(CSVDiscrim)
			NuChi2DiscrimHist_NotSemiLeptonic.Fill(NuChi2Discrim)
			AllDiscrimHist_NotSemiLeptonic.Fill(AllDiscrim)

		if (TypeofSolution == 4):#Event is not semiLeptonic = 4
			MassDiscrimHist_NotReconstructible.Fill(MassDiscrim)
			CSVDiscrimHist_NotReconstructible.Fill(CSVDiscrim)
			NuChi2DiscrimHist_NotReconstructible.Fill(NuChi2Discrim)
			AllDiscrimHist_NotReconstructible.Fill(AllDiscrim)




	########## 			NORMALISING 			##########

	# integral = MassDiscrimHist_Total.Integral()
	# MassDiscrimHist_Total.Scale(1/integral)
	# integral = CSVDiscrimHist_Total.Integral()
	# CSVDiscrimHist_Total_Total.Scale(1/integral)
	# integral = NuChi2DiscrimHist_Total.Integral()
	# NuChi2DiscrimHist_Total.Scale(1/integral)
	# integral = AllDiscrimHist_Total.Integral()
	# AllDiscrimHist_Total.Scale(1/integral)

	# integral = MassDiscrimHist_Correct.Integral()
	# MassDiscrimHist_Correct.Scale(1/integral)
	# integral = CSVDiscrimHist_Correct.Integral()
	# CSVDiscrimHist_Correct.Scale(1/integral)
	# integral = NuChi2DiscrimHist_Correct.Integral()
	# NuChi2DiscrimHist_Correct.Scale(1/integral)
	# integral = AllDiscrimHist_Correct.Integral()
	# AllDiscrimHist_Correct.Scale(1/integral)

	# integral = MassDiscrimHist_Incorrect.Integral()
	# MassDiscrimHist_Incorrect.Scale(1/integral)
	# integral = CSVDiscrimHist_Incorrect.Integral()
	# CSVDiscrimHist_Incorrect.Scale(1/integral)
	# integral = NuChi2DiscrimHist_Incorrect.Integral()
	# NuChi2DiscrimHist_Incorrect.Scale(1/integral)
	# integral = AllDiscrimHist_Incorrect.Integral()
	# AllDiscrimHist_Incorrect.Scale(1/integral)

	# integral = MassDiscrimHist_NotSemiLeptonic.Integral()
	# MassDiscrimHist_NotSemiLeptonic.Scale(1/integral)
	# integral = CSVDiscrimHist_NotSemiLeptonic.Integral()
	# CSVDiscrimHist_NotSemiLeptonic.Scale(1/integral)
	# integral = NuChi2DiscrimHist_NotSemiLeptonic.Integral()
	# NuChi2DiscrimHist_NotSemiLeptonic.Scale(1/integral)
	# integral = AllDiscrimHis_NotSemiLeptonic.Integral()
	# AllDiscrimHist_NotSemiLeptonic.Scale(1/integral)

	# integral = MassDiscrimHist_NotReconstructible.Integral()
	# MassDiscrimHist_NotReconstructible.Scale(1/integral)
	# integral = CSVDiscrimHist_NotReconstructible.Integral()
	# CSVDiscrimHist_NotReconstructible.Scale(1/integral)
	# integral = NuChi2DiscrimHist_NotReconstructible.Integral()
	# NuChi2DiscrimHist_NotReconstructible.Scale(1/integral)
	# integral = AllDiscrimHist_NotReconstructible.Integral()
	# AllDiscrimHist_NotReconstructible.Scale(1/integral)


	########## 				PLOTTING 			##########


	file = TFile("E_Likelihood.root", "RECREATE")

	########## 				Mass 				##########

	MassCanvas = TCanvas("Mass","Mass", 0, 0, 800, 600)
	Massleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Massleg.SetFillColor(0)
	Massleg.SetLineColor(0)

	MassDiscrimHist_NotSemiLeptonic.SetLineColor(kMagenta)
	MassDiscrimHist_NotReconstructible.SetLineColor(kGreen)
	MassDiscrimHist_Incorrect.SetLineColor(kRed)
	MassDiscrimHist_Correct.SetLineColor(kBlue)

	MassDiscrimHist_Total.SetTitle("Mass Discriminator; Mass Disc; Events")
	MassDiscrimHist_Total.GetYaxis().SetTitleOffset(1.2)

	MassDiscrimHist_Total.Draw("")
	MassDiscrimHist_Incorrect.Draw("same")
	MassDiscrimHist_NotReconstructible.Draw("same")
	MassDiscrimHist_NotSemiLeptonic.Draw("same")
	MassDiscrimHist_Correct.Draw("same")

	Massleg.AddEntry(MassDiscrimHist_Total, "TTBar Total" ,"le")
	Massleg.AddEntry(MassDiscrimHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	Massleg.AddEntry(MassDiscrimHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	Massleg.AddEntry(MassDiscrimHist_Incorrect, "TTbar Wrong Reco" ,"le")
	Massleg.AddEntry(MassDiscrimHist_Correct, "TTbar Right Reco" ,"le")


	Massleg.Draw()
	MassCanvas.Update()
	MassCanvas.SaveAs("plots/Total_E_MassDiscrimBest.png")
	MassCanvas.Write()

	########## 				CSV 				##########

	CSVCanvas = TCanvas("CSV","CSV", 0, 0, 800, 600)
	CSVleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	CSVleg.SetFillColor(0)
	CSVleg.SetLineColor(0)

	CSVDiscrimHist_NotSemiLeptonic.SetLineColor(kMagenta)
	CSVDiscrimHist_NotReconstructible.SetLineColor(kGreen)
	CSVDiscrimHist_Incorrect.SetLineColor(kRed)
	CSVDiscrimHist_Correct.SetLineColor(kBlue)

	CSVDiscrimHist_Total.SetTitle("CSV Discriminator; Mass Disc; Events")
	CSVDiscrimHist_Total.GetYaxis().SetTitleOffset(1.2)

	CSVDiscrimHist_Total.Draw("")
	CSVDiscrimHist_Incorrect.Draw("same")
	CSVDiscrimHist_NotReconstructible.Draw("same")
	CSVDiscrimHist_NotSemiLeptonic.Draw("same")
	CSVDiscrimHist_Correct.Draw("same")

	CSVleg.AddEntry(CSVDiscrimHist_Total, "TTBar Total" ,"le")
	CSVleg.AddEntry(CSVDiscrimHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	CSVleg.AddEntry(CSVDiscrimHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	CSVleg.AddEntry(CSVDiscrimHist_Incorrect, "TTbar Wrong Reco" ,"le")
	CSVleg.AddEntry(CSVDiscrimHist_Correct, "TTbar Right Reco" ,"le")


	CSVleg.Draw()
	CSVCanvas.Update()
	CSVCanvas.SaveAs("plots/Total_E_CSVDiscrimBest.png")
	CSVCanvas.Write()


	########## 				NuChi2				##########

	########## 				CSV 				##########

	NuChi2Canvas = TCanvas("NuChi2","NuChi2", 0, 0, 800, 600)
	NuChi2leg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NuChi2leg.SetFillColor(0)
	NuChi2leg.SetLineColor(0)

	NuChi2DiscrimHist_NotSemiLeptonic.SetLineColor(kMagenta)
	NuChi2DiscrimHist_NotReconstructible.SetLineColor(kGreen)
	NuChi2DiscrimHist_Incorrect.SetLineColor(kRed)
	NuChi2DiscrimHist_Correct.SetLineColor(kBlue)

	NuChi2DiscrimHist_Total.SetTitle("NuChi2 Discriminator; Mass Disc; Events")
	NuChi2DiscrimHist_Total.GetYaxis().SetTitleOffset(1.2)

	NuChi2DiscrimHist_Total.Draw("")
	NuChi2DiscrimHist_Incorrect.Draw("same")
	NuChi2DiscrimHist_NotReconstructible.Draw("same")
	NuChi2DiscrimHist_NotSemiLeptonic.Draw("same")
	NuChi2DiscrimHist_Correct.Draw("same")

	NuChi2leg.AddEntry(NuChi2DiscrimHist_Total, "TTBar Total" ,"le")
	NuChi2leg.AddEntry(NuChi2DiscrimHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	NuChi2leg.AddEntry(NuChi2DiscrimHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	NuChi2leg.AddEntry(NuChi2DiscrimHist_Incorrect, "TTbar Wrong Reco" ,"le")
	NuChi2leg.AddEntry(NuChi2DiscrimHist_Correct, "TTbar Right Reco" ,"le")


	NuChi2leg.Draw()
	NuChi2Canvas.Update()
	NuChi2Canvas.SaveAs("plots/Total_E_NuChi2DiscrimBest.png")
	NuChi2Canvas.Write()

	########## 				All 				##########

	AllCanvas = TCanvas("All","All", 0, 0, 800, 600)
	Allleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Allleg.SetFillColor(0)
	Allleg.SetLineColor(0)

	AllDiscrimHist_NotSemiLeptonic.SetLineColor(kMagenta)
	AllDiscrimHist_NotReconstructible.SetLineColor(kGreen)
	AllDiscrimHist_Incorrect.SetLineColor(kRed)
	AllDiscrimHist_Correct.SetLineColor(kBlue)

	AllDiscrimHist_Total.SetTitle("All Discriminator; Mass Disc; Events")
	AllDiscrimHist_Total.GetYaxis().SetTitleOffset(1.2)

	AllDiscrimHist_Total.Draw("")
	AllDiscrimHist_Incorrect.Draw("same")
	AllDiscrimHist_NotReconstructible.Draw("same")
	AllDiscrimHist_NotSemiLeptonic.Draw("same")
	AllDiscrimHist_Correct.Draw("same")

	Allleg.AddEntry(AllDiscrimHist_Total, "TTBar Total" ,"le")
	Allleg.AddEntry(AllDiscrimHist_NotSemiLeptonic, "TTbar Not SemiLeptonic" ,"le")
	Allleg.AddEntry(AllDiscrimHist_NotReconstructible, "TTbar Not Reconstructible" ,"le")
	Allleg.AddEntry(AllDiscrimHist_Incorrect, "TTbar Wrong Reco" ,"le")
	Allleg.AddEntry(AllDiscrimHist_Correct, "TTbar Right Reco" ,"le")


	Allleg.Draw()
	AllCanvas.Update()
	AllCanvas.SaveAs("plots/TotalAll_E_DiscrimBest.png")
	AllCanvas.Write()

	########## 				Write Histos 				##########

	MassDiscrimHist_Total.Write()
	CSVDiscrimHist_Total.Write()
	NuChi2DiscrimHist_Total.Write()
	AllDiscrimHist_Total.Write()

	MassDiscrimHist_Correct.Write()
	CSVDiscrimHist_Correct.Write()
	NuChi2DiscrimHist_Correct.Write()
	AllDiscrimHist_Correct.Write()

	MassDiscrimHist_Incorrect.Write()
	CSVDiscrimHist_Incorrect.Write()
	NuChi2DiscrimHist_Incorrect.Write()
	AllDiscrimHist_Incorrect.Write()

	MassDiscrimHist_NotSemiLeptonic.Write()
	CSVDiscrimHist_NotSemiLeptonic.Write()
	NuChi2DiscrimHist_NotSemiLeptonic.Write()
	AllDiscrimHist_NotSemiLeptonic.Write()

	MassDiscrimHist_NotReconstructible.Write()
	CSVDiscrimHist_NotReconstructible.Write()
	NuChi2DiscrimHist_NotReconstructible.Write()
	AllDiscrimHist_NotReconstructible.Write()

