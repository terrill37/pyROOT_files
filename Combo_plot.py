import ROOT
import os

file_name = 'hists_13_05_20_HLTTDR_phase2'
root_file_name = file_name +'.root'
#directory = '../../'

#os.chdir(directory)

inFile = ROOT.TFile(root_file_name, "READ")

#output_dir = 'pdf'
#if not os.path.isdir(output_dir):
 #   os.mkdir(output_dir)

output = file_name+'.pdf'
#output_png_dir = output_dir

dir_path = 'pfTracks'
#dir_path_copy = 'pfTracks_copy'

can = ROOT.TCanvas()

plot_names=['pt_s', 'pt_m', 'pt_l', 'pz_l', 'eta', 'phi', 'm_s', 'm', 'm_l', 'e', 'etaPhi',
        'ip3d_l', 'ip3d', 'ip3d_sig_l', 'ip3d_sig', 'ip3d_err_l', 'ip3d_err',
        'ip2d_l', 'ip2d', 'ip2d_vs_pt', 'ip2d_vs_eta', 'ip2d_sig_l', 'ip2d_sig',
        'ip2d_err_l', 'ip2d_err',
        'DecayLenVal_l', 'DecayLenVal', 'JetDistVal', 'PtRel', 'Momentum', 'Pt_logx',
        'Eta', 'Phi', 'PPar', 'DeltaR', 'DeltaR_l', 'EtaRel', 'PtRatio', 'PParRatio',
        'Chi2', 'NTotalHits', 'NPixelHits', 'NStripHits', 'HasInnerPixHit', 
#        Eta_forAlgo0, Phi_forAlgo0, Pt_forAlgo0,
 #       Eta_forAlgo1, Phi_forAlgo1, Pt_forAlgo1,
  #      Eta_forAlgo2, Phi_forAlgo2, Pt_forAlgo2,
   #     Eta_forAlgo3, Phi_forAlgo3, Pt_forAlgo3,
    #    Eta_forAlgo4, Phi_forAlgo4, Pt_forAlgo4,
     #   Eta_forAlgo5, Phi_forAlgo5, Pt_forAlgo5,
      #  Eta_forAlgo6, Phi_forAlgo6, Pt_forAlgo6,
       # Eta_forAlgo7, Phi_forAlgo7, Pt_forAlgo7,
#        Eta_forAlgo8, Phi_forAlgo8, Pt_forAlgo8,
 #       Eta_forAlgo9, Phi_forAlgo9, Pt_forAlgo9,
  #      Eta_forAlgo10, Phi_forAlgo10, Pt_forAlgo10,
   #     Eta_forAlgo11, Phi_forAlgo11, Pt_forAlgo11,
    #    Eta_forAlgo12, Phi_forAlgo12, Pt_forAlgo12,
     #   Eta_forAlgo13, Phi_forAlgo13, Pt_forAlgo13,
      #  Eta_forAlgo14, Phi_forAlgo14, Pt_forAlgo14,
       # Eta_forAlgo15, Phi_forAlgo15, Pt_forAlgo15,
#        Eta_forAlgo16, Phi_forAlgo16, Pt_forAlgo16,
 #       Eta_forAlgo17, Phi_forAlgo17, Pt_forAlgo17,
  #      Eta_forAlgo18, Phi_forAlgo18, Pt_forAlgo18,
   #     Eta_forAlgo19, Phi_forAlgo19, Pt_forAlgo19,
    #    Eta_forAlgo20, Phi_forAlgo20, Pt_forAlgo20,
     #   Eta_forAlgo21, Phi_forAlgo21, Pt_forAlgo21,
      #  Eta_forAlgo22, Phi_forAlgo22, Pt_forAlgo22,
       # Eta_forAlgo23, Phi_forAlgo23, Pt_forAlgo23,
#        Eta_forAlgo24, Phi_forAlgo24, Pt_forAlgo24,
 #       Eta_forAlgo25, Phi_forAlgo25, Pt_forAlgo25,
  #      Eta_forAlgo26, Phi_forAlgo26, Pt_forAlgo26,
   #     Eta_forAlgo27, Phi_forAlgo27, Pt_forAlgo27,
    #    Eta_forAlgo28, Phi_forAlgo28, Pt_forAlgo28,
     #   Eta_forAlgo29, Phi_forAlgo29, Pt_forAlgo29,
      #  nMatches, matched_dip2d, matched_phi_vs_dip2d, matched_eta_vs_dip2d,
       # matched_dPtRel, matched_dMomentum, matched_dEta, matched_dEta_s,
#        matched_dPhi, matched_dR, matched_dR_s, matched_dEta_vs_dMomentum,
 #       matched_dEta_vs_dPhi, 
  #      secondClosest_dEta, secondClosest_dEta_s, secondClosest_dMomentum,
   #     secondClosest_dR, secondClosest_dR_s, secondClosest_dEta_vs_dMomentum,
    #    dEta12, nTracks, charge, IsFromSV, IsFromV0, algo, origAlgo, PV, PVweight,
     #   SV, SVweight, nTrackMap, pixHitMap, stripHitMap, totHitMap, innerPixHitMap]
        ]
can.Print(output+"[")
for i in range(0, len(plot_names), 1):

    hist = inFile.Get(dir_path+"/"+plot_names[i])
    #hist_copy = inFile.Get(dir_path_copy+"/"+plot_names[i])

    can.cd()
    can.SetLogy(0)

    hist.SetLineColor(14)

    hist.Draw("h")
    #hist_copy.Draw("h, same")

    can.Print(output)
    can.SaveAs(file_name+plot_names[i]+".png")
    can.SaveAs(file_name+plot_names[i]+".pdf")

can.Print(output+"]")
