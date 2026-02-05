import streamlit as st

st.set_page_config(page_title="Refeeding Syndrome Guide", layout="centered")

# --- SIDEBAR: REFERENCE RANGES ---
with st.sidebar:
    st.header("🎯 Reference Ranges")
    st.info("""
    **Standard Adult Ranges (Verify Locally):**
    
    * **Potassium ($K^+$):** 3.5 – 5.5 mmol/L
    * **Magnesium ($Mg$):** 0.7 – 1.0 mmol/L
    * **Phosphate ($PO_4$):** 0.8 – 1.5 mmol/L
    * **Calcium (Adj):** 2.2 – 2.6 mmol/L
    """)
    
    st.warning("""
    **⚠️ Correction Priority:**
    1.  Potassium & Magnesium
    2.  Calcium
    3.  Phosphate
    
    *Rationale: IV phosphate can lower Ca/Mg/K further.*
    """)
    
    st.markdown("---")
    st.caption("Guideline: Taunton & Somerset NHS Foundation Trust")

# --- MAIN APP CONTENT ---
st.title("Adult Refeeding Syndrome Clinical Tool")

# --- STEP 1: RISK ASSESSMENT ---
st.header("Step 1: Risk Assessment")

with st.expander("Patient Criteria", expanded=True):
    weight = st.number_input("Current Weight (kg)", min_value=20.0, max_value=250.0, value=70.0, step=0.1)
    bmi = st.number_input("Current BMI (kg/m²)", min_value=5.0, max_value=50.0, value=20.0, step=0.1)
    weight_loss = st.number_input("Unintentional weight loss in last 3-6 months (%)", min_value=0.0, max_value=100.0, value=0.0)
    days_starved = st.number_input("Days with little or no nutrition", min_value=0, max_value=100, value=0)
    
    col1, col2 = st.columns(2)
    with col1:
        low_elec = st.checkbox("Low baseline Potassium, Phosphate, or Magnesium")
        alcohol = st.checkbox("History of alcohol excess")
    with col2:
        meds = st.checkbox("New insulin, chemo, antacids, or diuretics")

# Risk Logic based on Section 3.0
risk_level = "Low Risk"
rec_kcal = 25

if bmi < 14 or days_starved > 15:
    risk_level = "Extremely High Risk"
    rec_kcal = 5
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec):
    risk_level = "High Risk"
    rec_kcal = 10
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2:
    risk_level = "High Risk"
    rec_kcal = 10
elif days_starved > 5:
    risk_level = "At Risk"
    rec_kcal = 15

st.subheader(f"Calculated Risk: {risk_level}")

# --- STEP 2: INITIAL MANAGEMENT ---
st.header("Step 2: Initial Management")

if risk_level == "Extremely High Risk":
    st.error(f"**Feeding:** Start at {rec_kcal} kcal/kg/day. Increase to full requirements by day 7.")
    st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring.")
elif risk_level == "High Risk":
    st.warning(f"**Feeding:** Start at {rec_kcal} kcal/kg/day. Increase to full requirements by days 4-7.")
elif risk_level == "At Risk":
    st.info("**Feeding:** Start at max 50% of nutritional requirements for the first 2 days.")

# Feeding Rate Slider
kcal_slider = st.slider("Target Initial Energy (kcal/kg/day):", min_value=5, max_value=35, value=rec_kcal)
st.success(f"**Initial Energy Target: {round(weight * kcal_slider)} kcal/day**")

st.write("### Vitamin Supplementation (Start Day 1)")
st.info("Give first dose at least 30 mins before feeding starts.")
st.markdown("""
* **Thiamine:** 50mg QDS (4 times a day) for 10 days.
* **Vitamin B Co Strong:** 2 tablets TDS (3 times a day) for 10 days.
* **Forceval:** 1 capsule/tablet daily.
* *If IV only:* **Pabrinex** Pairs 1 & 2 TDS for 10 days.
""")

# --- STEP 3: LABORATORY MONITORING & CORRECTION ---
st.header("Step 3: Laboratory Monitoring & Correction")

st.write("**Frequency:** Daily until stable, then twice weekly.")

st.write("### Corrective Actions (Based on Blood Results)")
analyte = st.selectbox("Select abnormal electrolyte:", ["Potassium (K+)", "Magnesium (Mg)", "Phosphate (PO4)"])

# POTASSIUM
if analyte == "Potassium (K+)":
    val_k = st.number_input("Serum K+ (mmol/L)", min_value=0.0, step=0.1)
    
    if 0.1 <= val_k < 3.5:
        st.warning("#### ⚠️ Clinical Action: Review ECG for Hypokalaemia")
        st.markdown("""
        **Look for morphological changes:**
        * **P-wave flattening** (or increased amplitude)
        * **T-wave flattening** or inversion
        * **Prominent U-waves** (characteristic)
        * **ST-segment depression**
        """)
        
        
        
        if val_k < 2.5:
            st.error("**Treatment Advice:** 40mmol K+ in 1L 0.9% NaCl IV over min 4 hours.")
            st.info("**Monitoring:** Check serum K+ every 12 hours (Ref: 184).")
            st.warning("NB: Continuous ECG monitoring is essential for rates >20 mmol/hr.")
        elif val_k < 3.0:
            st.write("**Treatment Advice:** 2 tablets Sando-K QDS orally (72 mmol K+) OR 40mmol K+ IV over min 8 hours.")
            st.info("**Monitoring:** Check serum K+ every 24 hours.")
        else:
            st.write("**Treatment Advice:** 2 tablets Sando-K TDS orally (72 mmol K+) OR 40mmol K+ IV over min 8 hours.")
            st.info("**Monitoring:** Check serum K+ every 24 hours.")
            
    elif val_k > 5.5:
        st.error("#### 🚨 Clinical Action: Review ECG for Hyperkalaemia")
        st.markdown("""
        **ECG Warning Signs:**
        * **Tented (Peaked) T-waves** (tall/narrow)
        * **P-wave flattening** or disappearance
        * **Widening of the QRS complex** (Imminent cardiac arrest)
        """)
        
        
        
        st.warning("**Clinical Warning:** Beware of renal impairment in malnourished/dehydrated patients.")
        st.info("**Treatment Advice:** Stop all potassium-containing fluids/supplements. Urgent medical review required. Contact nutrition team.")

# MAGNESIUM
elif analyte == "Magnesium (Mg)":
    val_mg = st.number_input("Serum Mg (mmol/L)", min_value=0.0, step=0.1)
    if 0.1 <= val_mg < 0.5:
        st.error("**Treatment Advice:** Give 20mmol Magnesium Sulphate IV over 12 hours. Check serum every 12h.")
    elif 0.5 <= val_mg < 0.7:
        st.warning("**Treatment Advice:** 5ml Magnesium Hydroxide TDS orally until serum >0.7 mmol/L, then 5ml BD x 48 hr.")
        st.info("**Monitoring:** Check serum Mg every 24 hours.")

# PHOSPHATE
elif analyte == "Phosphate (PO4)":
    val_p = st.number_input("Serum PO4 (mmol/L)", min_value=0.0, step=0.1)
    if 0.1 <= val_p < 0.3:
        st.error("**Treatment Advice:** Give IV Sodium Glycerophosphate 20mmol over 8-12 hours. Check serum every 12h.")
        if weight < 45: 
            st.warning("NB: Reduce dose by 50% for patients <45kg.")
    elif 0.3 <= val_p < 0.5:
        st.warning("**Treatment Advice:** If oral route suitable: 2 tablets Phosphate-Sandoz OD. Otherwise: IV replacement.")
    elif 0.5 <= val_p < 0.7:
        st.info("**Treatment Advice:** 1 tablet Phosphate-Sandoz OD. Check serum every 24h.")

# CLINICAL MONITORING NOTES
st.divider()
st.subheader("Clinical Monitoring Notes")
st.markdown("""
* **Parenteral Nutrition (PN):** Monitor blood glucose every 6 hours.
* **Glucose:** Monitor at least twice daily until full feed established.
* **Fluid Status:** Restore circulatory volume closely; avoid fluid overload.
* **Renal Impairment:** Beware of normal K+/PO4 levels in dehydrated patients with renal failure.
""")

st.caption("Note: Always involve a Dietitian at the earliest opportunity.")
