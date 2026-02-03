import streamlit as st

# Page Config
st.set_page_config(page_title="Refeeding Syndrome Tool", page_icon="🏥", layout="wide")

st.title("Adult Refeeding Syndrome Clinical Decision Support")
[cite_start]st.caption("Based on Taunton and Somerset NHS Foundation Trust Guidelines [cite: 1, 2, 3]")

# --- SIDEBAR: REFERENCE RANGES ---
with st.sidebar:
    st.header("Normal Reference Ranges")
    st.markdown("""
    *Standard adult norms (may vary by lab):*
    - **Potassium (K+):** 3.5 – 5.0 mmol/L
    - **Phosphate (PO4):** 0.8 – 1.5 mmol/L
    - **Magnesium (Mg):** 0.7 – 1.0 mmol/L
    - **Corrected Calcium:** 2.2 – 2.6 mmol/L
    - **Sodium (Na+):** 135 – 145 mmol/L
    """)
    st.divider()
    [cite_start]st.write("**MDT Reminder:** A Dietitian should be involved at the earliest opportunity[cite: 21, 32].")

# --- STEP 1: RISK STRATIFICATION ---
st.header("Step 1: Risk Assessment")
col_risk1, col_risk2 = st.columns(2)

with col_risk1:
    st.subheader("High Risk Criteria")
    [cite_start]r1 = st.checkbox("BMI < 16 kg/m² [cite: 48]")
    [cite_start]r2 = st.checkbox("Unintentional weight loss > 15% (last 3-6 months) [cite: 49]")
    [cite_start]r3 = st.checkbox("Little/no nutrition > 10 days [cite: 50]")
    [cite_start]r4 = st.checkbox("Low baseline K+, PO4, or Mg [cite: 51]")
    
    st.write("---")
    st.subheader("2+ Criteria Needed:")
    [cite_start]c1 = st.checkbox("BMI < 18.5 kg/m² [cite: 53]")
    [cite_start]c2 = st.checkbox("Weight loss > 10% (3-6 months) [cite: 54]")
    [cite_start]c3 = st.checkbox("Little/no nutrition > 5 days [cite: 55]")
    [cite_start]c4 = st.checkbox("History of alcohol excess [cite: 56]")
    [cite_start]c5 = st.checkbox("New insulin, chemo, antacids, or diuretics [cite: 57]")

with col_risk2:
    st.subheader("Extremely High Risk Criteria")
    [cite_start]ex1 = st.checkbox("BMI < 14 kg/m² [cite: 59]")
    [cite_start]ex2 = st.checkbox("Little/no nutrition > 15 days [cite: 60]")

# Logic for Risk Level
risk_level = "At Risk (Standard)"
if ex1 or ex2:
    risk_level = "Extremely High Risk"
elif r1 or r2 or r3 or r4:
    risk_level = "High Risk"
elif (sum([c1, c2, c3, c4, c5])) >= 2:
    risk_level = "High Risk"
elif c3: # Little/no nutrition > 5 days
    risk_level = "At Risk"

st.info(f"Calculated Risk Category: **{risk_level}**")

# --- STEP 2: INITIAL MANAGEMENT ---
st.header("Step 2: Initial Management Plan")

# Feeding & Monitoring
if risk_level == "Extremely High Risk":
    [cite_start]st.error("**Feed:** Consider starting at 5 kcal/kg/day. Increase to full requirements by Day 7[cite: 79].")
    [cite_start]st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring[cite: 84].")
elif risk_level == "High Risk":
    [cite_start]st.warning("**Feed:** Start at 10 kcal/kg/day. Increase to full by Days 4-7[cite: 72].")
else:
    [cite_start]st.success("**Feed:** Start at max 50% of requirements for the first 2 days[cite: 65].")

# Vitamins (Section 6.4)
with st.expander("Mandatory Vitamin Prophylaxis (Day 1-10)", expanded=True):
    [cite_start]st.markdown("### Give first dose at least 30 mins before feeding [cite: 110]")
    st.markdown("""
    * [cite_start]**Thiamine:** 50 mg QDS [cite: 106]
    * [cite_start]**Vitamin B Co Strong:** 2 tablets TDS [cite: 105]
    * [cite_start]**Forceval:** 1 capsule OD [cite: 102]
    * [cite_start]*If IV Only:* **Pabrinex** 1 pair TDS [cite: 109]
    """)

# --- STEP 3: ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Electrolyte Replacement & Monitoring")
[cite_start]st.write("**Frequency:** Daily until stable, then twice weekly[cite: 90].")
[cite_start]st.caption("Safety Note: Correct Potassium and Magnesium FIRST, then Calcium, then Phosphate[cite: 97].")

replacement_col, info_col = st.columns([2, 1])

with replacement_col:
    analyte = st.selectbox("Select Abnormal Electrolyte:", ["None", "Potassium (K+)", "Phosphate (PO4)", "Magnesium (Mg)"])

    if analyte == "Potassium (K+)":
        k_val = st.number_input("Serum K+ (mmol/L):", step=0.1, format="%.1f")
        if 3.0 <= k_val < 3.5:
            [cite_start]st.write("**Action:** 2 tabs Sando-K TDS (72mmol) OR 40mmol K+ IV in 1L 0.9% NaCl over 8h[cite: 168, 171].")
            [cite_start]st.write("**Monitor:** Check serum K+ every 24h[cite: 176].")
        elif 2.5 <= k_val < 3.0:
            [cite_start]st.write("**Action:** 2 tabs Sando-K QDS (72mmol) OR 40mmol K+ IV in 1L 0.9% NaCl over 8h[cite: 172, 175].")
            [cite_start]st.write("**Monitor:** Check serum K+ every 24h[cite: 178].")
        elif k_val < 2.5:
            [cite_start]st.error("**Action:** 40mmol K+ in 1L 0.9% NaCl IV over min 4 hours[cite: 183].")
            [cite_start]st.error("**CRITICAL:** Continuous ECG monitoring essential for infusion rates > 20mmol/hr[cite: 185].")
            [cite_start]st.write("**Monitor:** Check serum K+ every 12h[cite: 184].")

    elif analyte == "Phosphate (PO4)":
        p_val = st.number_input("Serum PO4 (mmol/L):", step=0.1, format="%.1f")
        [cite_start]under_45 = st.checkbox("Patient weight < 45kg? (Requires 50% dose reduction) [cite: 139]")
        
        if 0.5 <= p_val < 0.7:
            [cite_start]st.write("**Action:** 1 tablet Phosphate-Sandoz OD (16mmol)[cite: 125].")
            [cite_start]st.write("**Monitor:** Check serum PO4 every 24h[cite: 134].")
        elif 0.3 <= p_val < 0.5:
            oral = st.radio("Is oral route suitable?", ["Yes", "No"])
            if oral == "Yes":
                [cite_start]st.write("**Action:** 2 tablets Phosphate-Sandoz OD (32mmol)[cite: 131, 133].")
            else:
                dose = "10mmol" if under_45 else "20mmol"
                [cite_start]st.write(f"**Action:** IV Sodium Glycerophosphate ({dose}) in 1L 0.9% NaCl over 8-12h[cite: 137, 138, 139].")
            [cite_start]st.write("**Monitor:** Check serum PO4 every 24h (oral) or 12h (IV)[cite: 134, 143].")
        elif p_val < 0.3:
            dose = "10mmol" if under_45 else "20mmol"
            [cite_start]st.error(f"**Action:** IV Sodium Glycerophosphate ({dose}) in 1L 0.9% NaCl over 8-12h[cite: 140, 142].")
            [cite_start]st.write("**Monitor:** Check serum PO4/Ca/K/Mg every 12h[cite: 143].")

    elif analyte == "Magnesium (Mg)":
        mg_val = st.number_input("Serum Mg (mmol/L):", step=0.1, format="%.1f")
        if 0.5 <= mg_val < 0.7:
            [cite_start]st.write("**Action:** 5ml Magnesium Hydroxide TDS orally until level > 0.7, then 5ml BD for 48h[cite: 153].")
            [cite_start]st.write("**Monitor:** Check serum Mg every 24h[cite: 154].")
        elif mg_val < 0.5:
            [cite_start]st.error("**Action:** 20mmol Magnesium Sulphate IV over 12 hours[cite: 155].")
            [cite_start]st.write("**Monitor:** Check serum Mg every 12h[cite: 156].")

with info_col:
    st.subheader("General Warnings")
    st.markdown("""
    - [cite_start]**Glucose:** Monitor BD until full feed; 6-hourly if on PN[cite: 85, 86].
    - [cite_start]**Fluids:** Restore circulatory volume but avoid fluid overload[cite: 76, 77].
    - [cite_start]**Renal Impairment:** Beware of dehydration masking low K+/PO4 levels[cite: 87].
    """)

st.divider()
[cite_start]st.caption("Disclaimer: This digital tool is for guidance and does not replace clinical judgment or official Trust policy database access[cite: 16, 17].")
