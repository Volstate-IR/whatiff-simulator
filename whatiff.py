import streamlit as st
import yaml

# Reads the preset configuration file
with open("presets.yml", "r") as presets_file:
    PRESETS = yaml.safe_load(presets_file)

st.set_page_config(layout="wide")

st.title("whatiFF - Funding Formula Simulator")
st.markdown("A simple calculator that lets you alter the funding formula. Defaults to 2026-27 VSCC Funding Formula Data.")

preset_col, _, _, _ = st.columns(4)

with preset_col:
    # PRESET SELECTOR
    preset_name = st.selectbox(
        "Select Funding Formula Preset",
        list(PRESETS.keys()),
        index=0
    )

    st.write()


preset = PRESETS[preset_name]

st.divider()

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    total_points_metric_container = st.empty()


with metric_col2:
    fixed_costs_share_metric_container = st.empty()


with metric_col3:
    qaf_share_metric_container = st.empty()


with metric_col4:
    points_change_metric_container = st.empty()


calculator_col1, calculator_col2, calculator_col3, calculator_col4 = st.columns(4)

with calculator_col1:
    st.header("Basics")
    st.markdown("Make small adjustments for a better what-if scenario")

    last_year_total_points = st.number_input("Last Year Total Points", 0, 1000, value=preset.get("last_year_total_points"))

    qaf_score = st.number_input("Quality Assurance Funding (QAF) Score", 0, 100, value=preset.get("qaf_score"))
    fixed_costs = st.number_input("$ Fixed Costs", 0, max_value=None, value=preset.get("fixed_costs"))


with calculator_col2:

    st.header("Progression")
    st.markdown("The number of students surpassing a credit hour threshold.")

    # PROGRESSION 12
    progression12 = st.number_input("Students Accumulating 12CH", 0, 5000, value=preset.get("progression12"))
    combined_12_text_container = st.empty()

    st.write()

    # PROGRESSION 24
    progression24 = st.number_input("Students Accumulating 24CH", 0, 5000, value=preset.get("progression24"))
    combined_24_text_container = st.empty()

    st.write()

    # PROGRESSION 36
    progression36 = st.number_input("Students Accumulating 36CH", 0, 5000, value=preset.get("progression36"))
    combined_36_text_container = st.empty()


with calculator_col3:
    st.header("Completion and Success")
    st.markdown("The number of students receiving credentials.")

    # ASSOCIATES
    associates = st.number_input("Associates Degrees", 0, 5000, value=preset.get("associates"))
    combined_associates_text_container = st.empty()

    st.write()

    reverse_associates = st.number_input("Reverse Associates Degrees", 0, 5000, value=preset.get("reverse_associates"))
    combined_reverse_associates_text_container = st.empty()
    st.markdown("Enter the *actual amount* of degrees issued to students via reverse transfer. This will be halved by the calculator automatically.")

    st.write()

    # 1-2Y CERTS
    lt_certificates = st.number_input("1-2y Certificates", 0, 5000, value=preset.get("lt_certificates"))
    combined_lt_certificates_text_container = st.empty()

    st.write()

    # <1Y CERTS
    st_certificates = st.number_input("<1y Certificates", 0, 5000, value=preset.get("st_certificates"))
    combined_st_certificates_text_container = st.empty()


with calculator_col4:
    st.header("Other")
    st.markdown("Other factors impacting the funding formula.")

    dual_enrollment = st.number_input("Dual Enrollment", 0, 5000, value=preset.get("dual_enrollment"))
    transfer = st.number_input("Transferring out with 12CH", 0, 5000, value=preset.get("transfer"))
    awards_per_fte = st.number_input("Awards per 100FTE", 0.0, 5000.0, value=preset.get("awards_per_fte"))
    job_placements = st.number_input("Job Placements", 0, 5000, value=preset.get("job_placements"))
    workforce_training = st.number_input("Workforce Training", 0, 500000, value=preset.get("workforce_training"))


st.divider()

st.header("Advanced Settings")
st.markdown("The settings below are for advanced users! Please don't use these unless you" \
" know what you're doing!")

special_pops_column, scaler_column, weight_column, utility_column = st.columns(4)

with special_pops_column:
    st.header("Special Populations")
    st.markdown("You can modify the special population bonus percentages here. " \
    "These are the actual values from the selected preset "
    "and should probably not be changed.")

    # SPECIAL POPULATION MULTIPLIERS
    sp_12_multiplier = st.number_input(
        "12CH Special Population % Bonus", 
        0.00, 
        1000.00, 
        value=preset.get("sp_12_multiplier"),
        format="%.2f"
    )

    sp_24_multiplier = st.number_input(
        "24CH Special Population % Bonus", 
        0.00, 
        1000.00, 
        value=preset.get("sp_24_multiplier"), 
        format="%.2f"
    )

    sp_36_multiplier = st.number_input(
        "36CH Special Population % Bonus",
        0.00,
        1000.00,
        value=preset.get("sp_36_multiplier"),
        format="%.2f"
    )

    associates_multipler = st.number_input(
        "Associates Degree Special Population % Bonus",
        0.00,
        1000.00,
        value=preset.get("associates_multipler"),
        format="%.2f"
    )

    reverse_associates_multipler = st.number_input(
        "Reverse Associates Degree Special Population % Bonus",
        0.00,
        1000.00,
        value=preset.get("reverse_associates_multiplier"),
        format="%.2f"
    )

    lt_certificates_multipler = st.number_input(
        "1-2y Certificates Special Population % Bonus",
        0.00,
        1000.00,
        value=preset.get("lt_certificates_multipler"),
        format="%.2f"
    )

    st_certificates_multipler = st.number_input(
        "<1y Certificates Special Population % Bonus",
        0.00,
        1000.00,
        value=preset.get("st_certificates_multipler"),
        format="%.2f"
    )


with scaler_column:
    st.header("Scales")
    st.markdown("This is where you can change the scaling used by the formula. " \
    "These are the actual values from the selected preset "
    "and should probably not be changed.")

    sp_12_scale = st.number_input(
        "12CH Progression Scale",
        0.00,
        1000.00,
        value=preset.get("sp_12_scale"),
        format="%.2f"
    )

    sp_24_scale = st.number_input(
        "24CH Progression Scale",
        0.00,
        1000.00,
        value=preset.get("sp_24_scale"),
        format="%.2f"
    )

    sp_36_scale = st.number_input(
        "36CH Progression Scale",
        0.00,
        1000.00,
        value=preset.get("sp_36_scale"),
        format="%.2f"
    )

    associates_scale = st.number_input(
        "Associates Degree Scale",
        0.00,
        1000.00,
        value=preset.get("associates_scale"),
        format="%.2f"
    )

    lt_certificates_scale = st.number_input(
        "1-2y Certificate Scale",
        0.00,
        1000.00,
        value=preset.get("lt_certificates_scale"),
        format="%.2f"
    )

    st_certificates_scale = st.number_input(
        "<1y Certificate Scale",
        0.00,
        1000.00,
        value=preset.get("st_certificates_scale"),
        format="%.2f"
    )

    dual_enrollment_scale = st.number_input(
        "Dual Enrollment Scale",
        0.00,
        1000.00,
        value=preset.get("dual_enrollment_scale"),
        format="%.2f"
    )

    transfer_scale = st.number_input(
        "Transfer Out with 12CH Scale",
        0.00,
        1000.00,
        value=preset.get("transfer_scale"),
        format="%.2f"
    )

    awards_per_fte_scale = st.number_input(
        "Awards per 100 FTE Scale",
        0.00,
        1000.00,
        value=preset.get("awards_per_fte_scale"),
        format="%.2f"
    )

    job_placements_scale = st.number_input(
        "Job Placement Scale",
        0.00,
        1000.00,
        value=preset.get("job_placements_scale"),
        format="%.2f"
    )

    workforce_training_scale = st.number_input(
        "Workforce Training Scale",
        0.00,
        1000.00,
        value=preset.get("workforce_training_scale"),
        format="%.2f"
    )


with weight_column:
    st.header("Weights")
    st.markdown("This is where you can change the weights used by the formula. " \
    "These are the actual values from the selected preset "
    "and should probably not be changed.")

    sp_12_weight = st.number_input(
        "% 12CH Progression Weight",
        0.00,
        1000.00,
        value=preset.get("sp_12_weight"),
        step=0.1,
        format="%.1f"
    )

    sp_24_weight = st.number_input(
        "% 24CH Progression Weight",
        0.00,
        1000.00,
        value=preset.get("sp_24_weight"),
        step=0.1,
        format="%.1f"
    )

    sp_36_weight = st.number_input(
        "% 36CH Progression Weight",
        0.00,
        1000.00,
        value=preset.get("sp_36_weight"),
        step=0.1,
        format="%.1f"
    )

    associates_weight = st.number_input(
        "% Associates Degree Weight",
        0.00,
        1000.00,
        value=preset.get("associates_weight"),
        step=0.1,
        format="%.1f"
    )

    lt_certificates_weight = st.number_input(
        "% 1-2y Certificate Weight",
        0.00,
        1000.00,
        value=preset.get("lt_certificates_weight"),
        step=0.1,
        format="%.1f"
    )

    st_certificates_weight = st.number_input(
        "% <1y Certificate Weight",
        0.00,
        1000.00,
        value=preset.get("st_certificates_weight"),
        step=0.1,
        format="%.1f"
    )

    dual_enrollment_weight = st.number_input(
        "% Dual Enrollment Weight",
        0.00,
        1000.00,
        value=preset.get("dual_enrollment_weight"),
        step=0.1,
        format="%.1f"
    )

    transfer_weight = st.number_input(
        "% Transfer Out with 12CH Weight",
        0.00,
        1000.00,
        value=preset.get("transfer_weight"),
        step=0.1,
        format="%.1f"
    )

    awards_per_fte_weight = st.number_input(
        "% Awards per 100 FTE Weight",
        0.00,
        1000.00,
        value=preset.get("awards_per_fte_weight"),
        step=0.1,
        format="%.1f"
    )

    job_placements_weight = st.number_input(
        "% Job Placement Weight",
        0.00,
        1000.00,
        value=preset.get("job_placements_weight"),
        step=0.1,
        format="%.1f"
    )

    workforce_training_weight = st.number_input(
        "% Workforce Training Weight",
        0.00,
        1000.00,
        value=preset.get("workforce_training_weight"),
        step=0.1,
        format="%.1f"
    )


with utility_column:
    st.header("Misc")
    st.markdown("Misc funding formula values are stored here. " \
    "These are the actual values from the selected preset "
    "and should probably not be changed.")

    fixed_cost_constant = st.number_input("Fixed Cost Constant", 0.0, 100.0, value=preset.get("fixed_cost_constant"), step=0.1, format="%.1f")
    qaf_constant = st.number_input("Quality Assurance Constant", 0.00, 100.00, value=preset.get("qaf_constant"), format="%.2f")

    statewide_points_earned = st.number_input("Points earned by weighted outcomes statewide", 0, 1000000, value=preset.get("statewide_points_earned"))
    st.markdown("The total number of points earned through weighted outcomes statewide, *EXCLUDING* the community college being reviewed.")

    statewide_fixed_costs = st.number_input("$ Statewide Fixed Costs", 0, 10000000000, value=preset.get("statewide_fixed_costs"))
    st.markdown("The total statewide fixed cost in dollars, *EXCLUDING* the community college being reviewed.")

st.divider()

# Footer
st.markdown("Office of Research, Assessment, and Special Initiatives - v0.3 - joshua.king@volstate.edu")


# COMBINING CALCULATIONS
combined_progression12 = (progression12 + (progression12 * (sp_12_multiplier / 100)))
combined_progression24 = (progression24 + (progression24 * (sp_24_multiplier / 100)))
combined_progression36 = (progression36 + (progression36 * (sp_36_multiplier / 100)))
combined_associates = (associates + (associates * (associates_multipler / 100)))
combined_reverse_associates = (reverse_associates + (reverse_associates * (reverse_associates_multipler / 100))) / 2
combined_lt_certificates = (lt_certificates + (lt_certificates * (lt_certificates_multipler / 100)))
combined_st_certificates = (st_certificates + (st_certificates * (st_certificates_multipler / 100)))

combined_12_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_progression12, 0))}")
combined_24_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_progression24, 0))}")
combined_36_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_progression36, 0))}")
combined_associates_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_associates, 0))}")
combined_reverse_associates_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_reverse_associates, 0))}")
combined_lt_certificates_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_lt_certificates, 0))}")
combined_st_certificates_text_container.markdown(f"Combined Value (including special populations): {int(round(combined_st_certificates, 0))}")


# SCALING CALCULATIONS
scaled_progression12 = (combined_progression12 / sp_12_scale)
scaled_progression24 = (combined_progression24 / sp_24_scale)
scaled_progression36 = (combined_progression36 / sp_36_scale)
scaled_associates = ((combined_associates + combined_reverse_associates) / associates_scale)
scaled_lt_certificates = (combined_lt_certificates / lt_certificates_scale)
scaled_st_certificates = (combined_st_certificates / st_certificates_scale)
scaled_dual_enrollment = (dual_enrollment / dual_enrollment_scale)
scaled_transfer = (transfer / transfer_scale)
scaled_awards_per_fte = (awards_per_fte / awards_per_fte_scale)
scaled_job_placements = (job_placements / job_placements_scale)
scaled_workforce_training = (workforce_training / workforce_training_scale)


# WEIGHTING CALCULATIONS
weighted_progression12 = (scaled_progression12 * (sp_12_weight / 100))
weighted_progression24 = (scaled_progression24 * (sp_24_weight / 100))
weighted_progression36 = (scaled_progression36 * (sp_36_weight / 100))
weighted_associates = (scaled_associates * (associates_weight / 100))
weighted_lt_certificates = (scaled_lt_certificates * (lt_certificates_weight / 100))
weighted_st_certificates = (scaled_st_certificates * (st_certificates_weight / 100))
weighted_dual_enrollment = (scaled_dual_enrollment * (dual_enrollment_weight / 100))
weighted_transfer = (scaled_transfer * (transfer_weight / 100))
weighted_awards_per_fte = (scaled_awards_per_fte * (awards_per_fte_weight / 100))
weighted_job_placements = (scaled_job_placements * (job_placements_weight / 100))
weighted_workforce_training = (scaled_workforce_training * (workforce_training_weight / 100))

total_weighted_score = weighted_progression12 + weighted_progression24 + weighted_progression36 + \
    weighted_associates + weighted_lt_certificates + weighted_st_certificates + weighted_dual_enrollment + \
    weighted_transfer + weighted_awards_per_fte + weighted_job_placements + weighted_workforce_training


# FIXED COST CALCULATIONS
fixed_costs_points_available = (statewide_points_earned + total_weighted_score) * (fixed_cost_constant / 100)
fixed_costs_pct_share = fixed_costs / (statewide_fixed_costs + fixed_costs)
fixed_costs_points = fixed_costs_pct_share * fixed_costs_points_available

# QAF CALCULATIONS
maximum_qaf_points = (total_weighted_score + fixed_costs_points) * (qaf_constant / 100)
earned_qaf_points = maximum_qaf_points * (qaf_score / 100)

# FINAL POINTS CALCULATION
total_points = int(round(total_weighted_score + fixed_costs_points + earned_qaf_points, 0))

points_change = str(round(((total_points - last_year_total_points) / last_year_total_points) * 100, 2)) + "%"

total_points_metric_container.metric(label="Total Points", value=total_points)
fixed_costs_share_metric_container.metric(label="Fixed Cost Points (incl in total)", value=int(round(fixed_costs_points, 0)))
qaf_share_metric_container.metric(label="QAF Points (incl in total)", value=int(round(earned_qaf_points, 0)))
points_change_metric_container.metric(label="% Points Change", value=points_change)