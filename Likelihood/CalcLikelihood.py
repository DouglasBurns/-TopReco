'''
Created on 08 May 2015

@author: Douglas Burns

Plots CSV, MW.vs.MT, Neutrino Chi Test.

'''

import ROOT 
from ROOT import gROOT, gPad, gStyle, TChain, TFile, TTree, TMath, TH1, TH1F, TH2F, TCanvas, TPad, TAxis, TLegend, TLatex, kRed, kBlue, kGreen
import math

if __name__ == '__main__':


	########## 			SETUP 			##########
	gStyle.SetOptStat("")
	input_file = "../../data/tree_TTJet_5000pb_PFElectron_PFMuon_PF2PATJets_MET.root"

	TrueMassDiscrimHist = TH1F("TrueMassDiscrim","True Mass Discrim", 100, -4, 2)
	TrueCSVDiscrimHist = TH1F("TrueCSVDiscrim","True CSV Discrim", 100, -10, 0)
	TrueNuChi2DiscrimHist = TH1F("TrueNuChi2Discrim","True NuChi2 Discrim", 100, -0.5, 2)
	TrueAllDiscrimHist = TH1F("TrueAllDiscrim","True All Discrim", 100, -15, 0)
		
	FalseMassDiscrimHist = TH1F("FalseMassDiscrim","False Mass Discrim", 100, -4, 2)
	FalseCSVDiscrimHist = TH1F("FalseCSVDiscrim","False CSV Discrim", 100, -10, 0)
	FalseNuChi2DiscrimHist = TH1F("FalseNuChi2Discrim","False NuChi2 Discrim", 100, -0.5, 2)
	FalseAllDiscrimHist = TH1F("FalseAllDiscrim","False All Discrim", 100, -15, 0)

	TotalMassDiscrimHist = TH1F("TotalMassDiscrim","Total Mass Discrim", 100, -4, 2)
	TotalCSVDiscrimHist = TH1F("TotalCSVDiscrim","Total CSV Discrim", 100, -10, 0)
	TotalNuChi2DiscrimHist = TH1F("TotalNuChi2Discrim","Total NuChi2 Discrim", 100, -0.5, 2)
	TotalAllDiscrimHist = TH1F("TotalAllDiscrim","Total All Discrim", 100, -15, 0)


	# inputTree = TTree(input_file.get("Discriminator"))
	inputTree = "TTbar_plus_X_analysis/EPlusJets/Ref selection/LikelihoodReco/Discriminator"
	Chain = TChain(inputTree)
	Chain.Add(input_file)

	Chain.SetBranchStatus("*",1)


	########## 			FILL HISTOGRAMS 		##########

	for event in Chain:

		MassDiscrim = event.__getattr__("MassDiscrimBest")
		CSVDiscrim = event.__getattr__("CSVDiscrimBest")
		NuChi2Discrim = event.__getattr__("NuChi2DiscrimBest")
		AllDiscrim = event.__getattr__("likelihoodRatioDiscrimBest")
		TrueEventReconstruction = event.__getattr__("EventReconstruction")

		TotalMassDiscrimHist.Fill(MassDiscrim)
		TotalCSVDiscrimHist.Fill(CSVDiscrim)
		TotalNuChi2DiscrimHist.Fill(NuChi2Discrim)
		TotalAllDiscrimHist.Fill(AllDiscrim)

		if (TrueEventReconstruction == 0):
			FalseMassDiscrimHist.Fill(MassDiscrim)
			FalseCSVDiscrimHist.Fill(CSVDiscrim)
			FalseNuChi2DiscrimHist.Fill(NuChi2Discrim)
			FalseAllDiscrimHist.Fill(AllDiscrim)

		if (TrueEventReconstruction == 1):
			TrueMassDiscrimHist.Fill(MassDiscrim)
			TrueCSVDiscrimHist.Fill(CSVDiscrim)
			TrueNuChi2DiscrimHist.Fill(NuChi2Discrim)
			TrueAllDiscrimHist.Fill(AllDiscrim)
	########## 			NORMALISING 			##########

	# integral = TrueMassDiscrimHist.Integral()
	# TrueMassDiscrimHist.Scale(1/integral)
	# integral = TrueCSVDiscrimHist.Integral()
	# TrueCSVDiscrimHist.Scale(1/integral)
	# integral = TrueNuChi2DiscrimHist.Integral()
	# TrueNuChi2DiscrimHist.Scale(1/integral)
	# integral = TrueAllDiscrimHist.Integral()
	# TrueAllDiscrimHist.Scale(1/integral)

	# integral = FalseMassDiscrimHist.Integral()
	# FalseMassDiscrimHist.Scale(1/integral)
	# integral = FalseCSVDiscrimHist.Integral()
	# FalseCSVDiscrimHist.Scale(1/integral)
	# integral = FalseNuChi2DiscrimHist.Integral()
	# FalseNuChi2DiscrimHist.Scale(1/integral)
	# integral = FalseAllDiscrimHist.Integral()
	# FalseAllDiscrimHist.Scale(1/integral)

	# integral = TotalMassDiscrimHist.Integral()
	# TotalMassDiscrimHist.Scale(1/integral)
	# integral = TotalCSVDiscrimHist.Integral()
	# TotalCSVDiscrimHist.Scale(1/integral)
	# integral = TotalNuChi2DiscrimHist.Integral()
	# TotalNuChi2DiscrimHist.Scale(1/integral)
	# integral = TotalAllDiscrimHist.Integral()
	# TotalAllDiscrimHist.Scale(1/integral)


	########## 				PLOTTING 			##########


	file = TFile("Likelihood.root", "RECREATE")

	########## 				Mass 				##########

	MassCanvas = TCanvas("Mass","Mass", 0, 0, 800, 600)
	Massleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Massleg.SetFillColor(0)
	Massleg.SetLineColor(0)

	TotalMassDiscrimHist.SetTitle("Mass Discriminator; Mass Disc; Events")
	TotalMassDiscrimHist.GetYaxis().SetTitleOffset(1.2)
	Massleg.AddEntry(TotalMassDiscrimHist, "Total Events" ,"le")
	TotalMassDiscrimHist.Draw()

	TrueMassDiscrimHist.SetLineColor(kBlue)
	Massleg.AddEntry(TrueMassDiscrimHist, "Correct Reconstruction" ,"le")
	TrueMassDiscrimHist.Draw("same")

	FalseMassDiscrimHist.SetLineColor(kRed)
	Massleg.AddEntry(FalseMassDiscrimHist, "Incorrect Reconstruction" ,"le")
	FalseMassDiscrimHist.Draw("same")

	Massleg.Draw()
	MassCanvas.Update()
	MassCanvas.SaveAs("plots/TotalMassDiscrimBest.png")
	MassCanvas.Write()


	########## 				CSV 				##########

	CSVCanvas = TCanvas("CSV","CSV", 0, 0, 800, 600)
	CSVleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	CSVleg.SetFillColor(0)
	CSVleg.SetLineColor(0)

	TotalCSVDiscrimHist.SetTitle("CSV Discriminator; CSV Disc; Events")
	TotalCSVDiscrimHist.GetYaxis().SetTitleOffset(1.2)
	CSVleg.AddEntry(TotalCSVDiscrimHist, "Total Events" ,"le")
	TotalCSVDiscrimHist.Draw()

	TrueCSVDiscrimHist.SetLineColor(kBlue)
	CSVleg.AddEntry(TrueCSVDiscrimHist, "Correct Reconstruction" ,"le")
	TrueCSVDiscrimHist.Draw("same")

	FalseCSVDiscrimHist.SetLineColor(kRed)
	CSVleg.AddEntry(FalseCSVDiscrimHist, "Incorrect Reconstruction" ,"le")
	FalseCSVDiscrimHist.Draw("same")

	CSVleg.Draw()
	CSVCanvas.Update()
	CSVCanvas.SaveAs("plots/TotalCSVDiscrimBest.png")
	CSVCanvas.Write()	


	########## 				NuChi2				##########

	NuChi2Canvas = TCanvas("NuChi2","NuChi2", 0, 0, 800, 600)
	NuChi2leg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	NuChi2leg.SetFillColor(0)
	NuChi2leg.SetLineColor(0)

	TotalNuChi2DiscrimHist.SetTitle("NuChi2 Discriminator; NuChi2 Disc; Events")
	TotalNuChi2DiscrimHist.GetYaxis().SetTitleOffset(1.2)
	NuChi2leg.AddEntry(TotalNuChi2DiscrimHist, "Total Events" ,"le")
	TotalNuChi2DiscrimHist.Draw()

	TrueNuChi2DiscrimHist.SetLineColor(kBlue)
	NuChi2leg.AddEntry(TrueNuChi2DiscrimHist, "Correct Reconstruction" ,"le")
	TrueNuChi2DiscrimHist.Draw("same")

	FalseNuChi2DiscrimHist.SetLineColor(kRed)
	NuChi2leg.AddEntry(FalseNuChi2DiscrimHist, "Incorrect Reconstruction" ,"le")
	FalseNuChi2DiscrimHist.Draw("same")

	NuChi2leg.Draw()
	NuChi2Canvas.Update()
	NuChi2Canvas.SaveAs("plots/TotalNuChi2DiscrimBest.png")
	NuChi2Canvas.Write()


	########## 				All 				##########

	AllCanvas = TCanvas("All","All", 0, 0, 800, 600)
	Allleg = TLegend(0.6,0.7,0.88,0.88)#xmin,ymin,xmax,ymax (in % of canvas)
	Allleg.SetFillColor(0)
	Allleg.SetLineColor(0)

	TotalAllDiscrimHist.SetTitle("All Discriminator; All Disc; Events")
	TotalAllDiscrimHist.GetYaxis().SetTitleOffset(1.2)
	Allleg.AddEntry(TotalAllDiscrimHist, "Total Events" ,"le")
	TotalAllDiscrimHist.Draw()

	TrueAllDiscrimHist.SetLineColor(kBlue)
	Allleg.AddEntry(TrueAllDiscrimHist, "Correct Reconstruction" ,"le")
	TrueAllDiscrimHist.Draw("same")

	FalseAllDiscrimHist.SetLineColor(kRed)
	Allleg.AddEntry(FalseAllDiscrimHist, "Incorrect Reconstruction" ,"le")
	FalseAllDiscrimHist.Draw("same")

	Allleg.Draw()
	AllCanvas.Update()
	AllCanvas.SaveAs("plots/TotalAllDiscrimBest.png")
	AllCanvas.Write()


	TrueMassDiscrimHist.Write()
	TrueCSVDiscrimHist.Write()
	TrueNuChi2DiscrimHist.Write()
	TrueAllDiscrimHist.Write()

	FalseMassDiscrimHist.Write()
	FalseCSVDiscrimHist.Write()
	FalseNuChi2DiscrimHist.Write()
	FalseAllDiscrimHist.Write()

	TotalMassDiscrimHist.Write()
	TotalCSVDiscrimHist.Write()
	TotalNuChi2DiscrimHist.Write()
	TotalAllDiscrimHist.Write()