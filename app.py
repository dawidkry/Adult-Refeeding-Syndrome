import streamlit as st

st.set_page_config(page_title="Refeeding Syndrome Guide", layout="centered")

st.title("Adult Refeeding Syndrome Clinical Tool")
st.caption("Based on Taunton and Somerset NHS Foundation Trust Guidelines")

# --- STEP 1: RISK ASSESSMENT ---
st.header("Step 1: Risk Assessment")

with st.expander("Patient Criteria", expanded=True):
    bmi = st.number_input("Current BMI (kg/m²)", min_value=5.0, max_value=50.0, value=20.0, step=0.1)
    weight_loss = st.number_input("Unintentional weight loss in last 3-6 months (%)", min_value=0.0, max_value=100.0, value=0.0)
    days_starved = st.number_input("Days with little or no nutrition", min_value=0, max_value=100, value=0)
    
    col1, col2 = st.columns(2)
    with col1:
        low_elec = st.checkbox("Low baseline Potassium, Phosphate, or Magnesium") [cite: 51]
        alcohol = st.checkbox("History of alcohol excess") [cite: 56]
    with col2:
        meds = st.checkbox("New insulin, chemo, antacids, or diuretics") [cite: 57]

# Risk Logic based on Section 3.0
risk_level = "Low Risk"
if bmi < 14 or days_starved > 15: [cite: 59, 60]
    risk_level = "Extremely High Risk"
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec): [cite: 48, 49, 50, 51]
    risk_level = "High Risk"
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2: [cite: 52, 53, 54, 55, 56, 57]
    risk_level = "High Risk"
elif days_starved > 5: [cite: 45]
    risk_level = "At Risk"

st.subheader(f"Calculated Risk: {risk_level}")

# --- STEP 2: INITIAL FEEDING & VITAMINS ---
st.header("Step 2: Initial Management")

if risk_level == "Extremely High Risk":
    st.error("**Feeding:** Start at 5 kcal/kg/day. Increase to full requirements by day 7.") [cite: 79]
    st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring.") [cite: 84]
elif risk_level == "High Risk":
    st.warning("**Feeding:** Start at 10 kcal/kg/day. Increase to full requirements by days 4-7.") [cite: 72]
elif risk_level == "At Risk":
    st.info("**Feeding:** Start at max 50% of nutritional requirements for the first 2 days.") [cite: 65]

# Vitamin Prophylaxis (Section 6.4)
st.write("### Vitamin Supplementation (Start Day 1)")
st.info("Give first dose at least 30 mins before feeding starts.") [cite: 110]
st.markdown("""
* **Thiamine:** 50mg QDS (4 times a day) for 10 days. [cite: 106]
* **Vitamin B Co Strong:** 2 tablets TDS (3 times a day) for 10 days. [cite: 105]
* **Forceval:** 1 capsule/tablet daily. [cite: 102]
* *If IV only:* **Pabrinex** Pairs 1 & 2 TDS for 10 days. [cite: 109]
""")

# --- STEP 3: BIOCHEMISTRY & ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Laboratory Monitoring & Correction")

st.write("**Frequency:** Daily until stable, then twice weekly.") [cite: 90]

st.write("### Corrective Actions (Based on Blood Results)")
analyte = st.selectbox("Select abnormal electrolyte:", ["Potassium (K+)", "Magnesium (Mg)", "Phosphate (PO4)"])

# POTASSIUM (Restored + ECG Advice)
if analyte == "Potassium (K+)":
    val_k = st.number_input("Serum K+ (mmol/L)", min_value=0.0, step=0.1)
    if val_k > 0 and val_k < 3.5:
        st.warning("#### ⚠️ ECG: Hypokalaemia Waves")
        st.markdown("* **T-wave flattening** or inversion.\n* **Prominent U-waves**.\n* **ST-depression**.")
        if val_k < 2.5: [cite: 179]
            st.error("40mmol K+ in 1L 0.9% NaCl IV over min 4 hours. Check every 12h.") [cite: 183, 184]
            st.warning("NB: Continuous ECG monitoring essential for rates >20mmol/hr.") [cite: 185]
        else: [cite: 165, 167]
            st.write("2 tablets Sando-K TDS/QDS or IV 40mmol K+ over 8 hours.") [cite: 168, 171, 172, 175]
    elif val_k > 5.5:
        st.error("#### ⚠️ ECG: Hyperkalaemia Waves")
        st.markdown("* **Tall, tented T-waves**.\n* **Loss of P-wave**.\n* **Wide QRS complex**.")

# MAGNESIUM (Fixed Input)
elif analyte == "Magnesium (Mg)":
    val_mg = st.number_input("Serum Mg (mmol/L)", min_value=0.0, step=0.1)
    if val_mg > 0 and val_mg < 0.5: [cite: 152]
        st.error("Give 20mmol Magnesium Sulphate IV over 12 hours. Check serum every 12h.") [cite: 155, 156]
    elif 0.5 <= val_mg < 0.7: [cite: 151]
        st.warning("5ml Magnesium Hydroxide TDS orally until >0.7. Check every 24h.") [cite: 153, 154]

# PHOSPHATE (Restored)
elif analyte == "Phosphate (PO4)":
    val_p = st.number_input("Serum PO4 (mmol/L)", min_value=0.0, step=0.1)
    if val_p > 0 and val_p < 0.3: [cite: 135]
        st.error("Give IV Sodium Glycerophosphate 20mmol over 8-12 hours. Check every 12h.") [cite: 142, 143]
    elif val_p < 0.5: [cite: 129]
        st.warning("If oral route suitable: 2 tablets Phosphate-Sandoz OD. Otherwise: IV replacement.") [cite: 131, 137]
    elif val_p < 0.7: [cite: 123]
        st.info("1 tablet Phosphate-Sandoz OD. Check serum every 24h.") [cite: 125, 134]

# PARENTERAL NUTRITION & CLINICAL ADVICE (Restored)
st.divider()
st.subheader("Clinical Monitoring Notes")
st.markdown("""
* **Parenteral Nutrition (PN):** Monitor blood glucose every 6 hours. 
* **Glucose:** Monitor at least twice daily until full feed established. [cite: 85]
* **Fluid Status:** Restore circulatory volume closely; avoid fluid overload. [cite: 76, 77]
* **Renal Impairment:** Beware of normal K+/PO4 levels in dehydrated patients with renal failure. 
""")

st.caption("Note: Always involve a Dietitian at the earliest opportunity.") [cite: 21]
