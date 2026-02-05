import streamlit as st

st.set_page_config(page_title="Refeeding Syndrome Guide", layout="centered")

# --- SIDEBAR: MOVING REFERENCE RANGES ---
with st.sidebar:
    st.header("🎯 Reference Ranges")
    st.info("""
    **Standard Adult Ranges (Verify Locally):**
    
    * [cite_start]**Potassium ($K^+$):** 3.5 – 5.5 mmol/L [cite: 165]
    * [cite_start]**Magnesium ($Mg$):** 0.7 – 1.0 mmol/L [cite: 151]
    * [cite_start]**Phosphate ($PO_4$):** 0.8 – 1.5 mmol/L [cite: 123]
    * [cite_start]**Calcium (Adj):** 2.2 – 2.6 mmol/L [cite: 90]
    """)
    
    st.warning("""
    **⚠️ Correction Priority:**
    1.  Potassium & Magnesium
    2.  Calcium
    3.  Phosphate
    
    [cite_start]*Rationale: IV phosphate can lower Ca/Mg/K further.* [cite: 97, 98]
    """)
    
    st.markdown("---")
    st.caption("Guideline: Taunton & Somerset NHS Foundation Trust")

# --- MAIN APP CONTENT ---
st.title("Adult Refeeding Syndrome Clinical Tool")

# --- STEP 1: RISK ASSESSMENT ---
st.header("Step 1: Risk Assessment")

with st.expander("Patient Criteria", expanded=True):
    bmi = st.number_input("Current BMI (kg/m²)", min_value=5.0, max_value=50.0, value=20.0, step=0.1)
    weight_loss = st.number_input("Unintentional weight loss in last 3-6 months (%)", min_value=0.0, max_value=100.0, value=0.0)
    days_starved = st.number_input("Days with little or no nutrition", min_value=0, max_value=100, value=0)
    
    col1, col2 = st.columns(2)
    with col1:
        [cite_start]low_elec = st.checkbox("Low baseline Potassium, Phosphate, or Magnesium") [cite: 51]
        [cite_start]alcohol = st.checkbox("History of alcohol excess") [cite: 56]
    with col2:
        [cite_start]meds = st.checkbox("New insulin, chemo, antacids, or diuretics") [cite: 57]

# Risk Logic based on Section 3.0
risk_level = "Low Risk"
if bmi < 14 or days_starved > 15:
    [cite_start]risk_level = "Extremely High Risk" [cite: 59, 60]
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec):
    [cite_start]risk_level = "High Risk" [cite: 48, 49, 50, 51]
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2:
    [cite_start]risk_level = "High Risk" [cite: 52, 53, 54, 55, 56, 57]
elif days_starved > 5:
    [cite_start]risk_level = "At Risk" [cite: 45]

st.subheader(f"Calculated Risk: {risk_level}")

# --- STEP 2: INITIAL FEEDING & VITAMINS ---
st.header("Step 2: Initial Management")

if risk_level == "Extremely High Risk":
    [cite_start]st.error("**Feeding:** Start at 5 kcal/kg/day. Increase to full requirements by day 7[cite: 79].")
    [cite_start]st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring[cite: 84].")
elif risk_level == "High Risk":
    [cite_start]st.warning("**Feeding:** Start at 10 kcal/kg/day. Increase to full requirements by days 4-7[cite: 72].")
elif risk_level == "At Risk":
    [cite_start]st.info("**Feeding:** Start at max 50% of nutritional requirements for the first 2 days[cite: 65].")

st.write("### Vitamin Supplementation (Start Day 1)")
[cite_start]st.info("Give first dose at least 30 mins before feeding starts[cite: 110].")
st.markdown("""
* [cite_start]**Thiamine:** 50mg QDS (4 times a day) for 10 days[cite: 106].
* [cite_start]**Vitamin B Co Strong:** 2 tablets TDS (3 times a day) for 10 days[cite: 105].
* [cite_start]**Forceval:** 1 capsule/tablet daily[cite: 102].
* [cite_start]*If IV only:* **Pabrinex** Pairs 1 & 2 TDS for 10 days[cite: 109].
""")

# --- STEP 3: BIOCHEMISTRY & ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Laboratory Monitoring & Correction")

[cite_start]st.write("**Frequency:** Daily until stable, then twice weekly[cite: 90].")

st.write("### Corrective Actions (Based on Blood Results)")
analyte = st.selectbox("Select abnormal electrolyte:", ["Potassium (K+)", "Magnesium (Mg)", "Phosphate (PO4)"])

# POTASSIUM (Corrected Logic)
if analyte == "Potassium (K+)":
    val_k = st.number_input("Serum K+ (mmol/L)", min_value=0.0, step=0.1)
    
    if 0.1 <= val_k < 3.5:
        st.warning("#### ⚠️ Clinical Action: Review ECG for Hypokalaemia")
        st.markdown("""
        **Look for the following specific changes:**
        * **P-wave flattening** (or increased amplitude).
        * **T-wave flattening** or inversion.
        * **Prominent U-waves** (the characteristic sign).
        * **ST-segment depression**.
        """)
                
        if val_k < 2.5:
            [cite_start]st.error("**Treatment Advice:** 40mmol K+ in 1L 0.9% NaCl IV over min 4 hours. Check every 12h[cite: 183, 184].")
            [cite_start]st.warning("NB: Continuous ECG monitoring essential for rates >20mmol/hr[cite: 185].")
        else:
            [cite_start]st.write("**Treatment Advice:** 2 tablets Sando-K TDS/QDS or IV 40mmol K+ over 8 hours[cite: 168, 175].")
            
    elif val_k >= 5.5:
        st.error("#### 🚨 Clinical Action: Review ECG for Hyperkalaemia")
        st.markdown("""
        **Look for the following specific changes:**
        * **Tented (Peaked) T-waves** (narrow-based and tall).
        * **P-wave flattening** or disappearance.
        * **Widening of the QRS complex** (Warning: Imminent cardiac arrest).
        """)
        
# MAGNESIUM (Corrected Logic)
elif analyte == "Magnesium (Mg)":
    val_mg = st.number_input("Serum Mg (mmol/L)", min_value=0.0, step=0.1)
    if 0.1 <= val_mg < 0.5:
        [cite_start]st.error("**Treatment Advice:** Give 20mmol Magnesium Sulphate IV over 12 hours. Check serum every 12h[cite: 155, 156].")
    elif 0.5 <= val_mg < 0.7:
        [cite_start]st.warning("**Treatment Advice:** 5ml Magnesium Hydroxide TDS orally until >0.7. Check every 24h[cite: 153, 154].")

# PHOSPHATE (Corrected Logic)
elif analyte == "Phosphate (PO4)":
    val_p = st.number_input("Serum PO4 (mmol/L)", min_value=0.0, step=0.1)
    if 0.1 <= val_p < 0.3:
        [cite_start]st.error("**Treatment Advice:** Give IV Sodium Glycerophosphate 20mmol over 8-12 hours. Check serum every 12h[cite: 137, 143].")
    elif 0.3 <= val_p < 0.5:
        [cite_start]st.warning("**Treatment Advice:** If oral route suitable: 2 tablets Phosphate-Sandoz OD. Otherwise: IV replacement[cite: 129, 131].")
    elif 0.5 <= val_p < 0.7:
        [cite_start]st.info("**Treatment Advice:** 1 tablet Phosphate-Sandoz OD. Check serum every 24h[cite: 123, 134].")

# PARENTERAL NUTRITION & CLINICAL ADVICE
st.divider()
st.subheader("Clinical Monitoring Notes")
st.markdown("""
* [cite_start]**Parenteral Nutrition (PN):** Monitor blood glucose every 6 hours[cite: 86].
* [cite_start]**Glucose:** Monitor at least twice daily until full feed established[cite: 85].
* [cite_start]**Fluid Status:** Restore circulatory volume closely; avoid fluid overload[cite: 76, 77].
* [cite_start]**Renal Impairment:** Beware of normal K+/PO4 levels in dehydrated patients with renal failure[cite: 87].
""")

[cite_start]st.caption("Note: Always involve a Dietitian at the earliest opportunity[cite: 21].")
