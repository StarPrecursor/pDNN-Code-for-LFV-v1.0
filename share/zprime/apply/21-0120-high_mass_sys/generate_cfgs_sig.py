temp = '''config:
    include:
        - "share/zprime/train/high_mass_all_mass.yaml"

job:
    job_name: "apply-all-mass-sys-sig"
    job_type: "apply"
    load_job_name: "train-all-mass"

input:
    reset_feature: false
    # only remove negative events for training
    rm_negative_weight_events: false
    # apply to sys trees
    arr_path: "zprime/arrays"
    arr_version: "21-0120-sys"
    variation: "{p_variation}"
    campaign: "run2"
    channel: "dummy_channel"
    sig_list:
        - "sig_Zp042"
        - "sig_Zp045"
        - "sig_Zp048"
        - "sig_Zp051"
        - "sig_Zp054"
        - "sig_Zp057"
        - "sig_Zp060"
        - "sig_Zp063"
        - "sig_Zp066"
        - "sig_Zp069"
        - "sig_Zp072"
        - "sig_Zp075"
    bkg_list: []
    selected_features:
        - "mz1"
        - "ptl1"
        - "ptl2"
        - "ptl3"
        - "ptl4"
        - "etal1"
        - "etal2"
        - "etal3"
        - "etal4"
        - "mz1_mz2"
        - "ptz1"
        - "ptz2"
        - "mzz"
        - "ptzz"
        - "deltarl12"
        - "deltarl34"
        - "detal12"
        - "detal34"
    validation_features:
        - "mz1"
        - "mz2"
    feature_norm_alias:
        mz1: "mz1_p"

apply:
    book_fit_npy: true
    cfg_fit_npy:
        fit_npy_region:
        fit_npy_branches:
            - "mz1"
            - "mz2"
        npy_save_dir: "zprime/arrays_fit/21-0120-sys/high_mass/{p_variation}"

'''

sig_ntuple_names = [
    "tree_NOMINAL",
    "tree_FT_EFF_B_systematics__1down",
    "tree_FT_EFF_B_systematics__1up",
    "tree_FT_EFF_C_systematics__1down",
    "tree_FT_EFF_C_systematics__1up",
    "tree_FT_EFF_Light_systematics__1down",
    "tree_FT_EFF_Light_systematics__1up",
    "tree_FT_EFF_extrapolation__1down",
    "tree_FT_EFF_extrapolation__1up",
    "tree_FT_EFF_extrapolation_from_charm__1down",
    "tree_FT_EFF_extrapolation_from_charm__1up",
    "tree_MUON_EFF_ISO_STAT__1down",
    "tree_MUON_EFF_ISO_STAT__1up",
    "tree_MUON_EFF_ISO_SYS__1down",
    "tree_MUON_EFF_ISO_SYS__1up",
    "tree_MUON_EFF_RECO_STAT__1down",
    "tree_MUON_EFF_RECO_STAT__1up",
    "tree_MUON_EFF_RECO_STAT_LOWPT__1down",
    "tree_MUON_EFF_RECO_STAT_LOWPT__1up",
    "tree_MUON_EFF_RECO_SYS__1down",
    "tree_MUON_EFF_RECO_SYS__1up",
    "tree_MUON_EFF_RECO_SYS_LOWPT__1down",
    "tree_MUON_EFF_RECO_SYS_LOWPT__1up",
    "tree_MUON_EFF_TTVA_STAT__1down",
    "tree_MUON_EFF_TTVA_STAT__1up",
    "tree_MUON_EFF_TTVA_SYS__1down",
    "tree_MUON_EFF_TTVA_SYS__1up",
    "tree_MUON_ID__1down",
    "tree_MUON_ID__1up",
    "tree_MUON_MS__1down",
    "tree_MUON_MS__1up",
    "tree_MUON_SAGITTA_RESBIAS__1down",
    "tree_MUON_SAGITTA_RESBIAS__1up",
    "tree_MUON_SAGITTA_RHO__1down",
    "tree_MUON_SAGITTA_RHO__1up",
    "tree_MUON_SCALE__1down",
    "tree_MUON_SCALE__1up",
    "tree_PRW_DATASF__1down",
    "tree_PRW_DATASF__1up",
]

for variation in sig_ntuple_names:
    with open(f"high_mass_all-mass_apply_sys_sig_{variation}.yaml", "w+") as file:
        file.write(temp.format(p_variation=variation))

