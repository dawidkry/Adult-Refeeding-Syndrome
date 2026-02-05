import streamlit as st
from fpdf import FPDF
import datetime

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
        low_elec = st.checkbox("Low baseline K+, PO4, or Mg")
        alcohol = st.checkbox("History of alcohol excess")
    with col2:
        meds = st.checkbox("New insulin, chemo, antacids, or diuretics")

# Risk Logic
risk_level = "Low Risk"
rec_kcal = 25
if bmi < 14 or days_starved > 15:
    risk_level = "Extremely High Risk"; rec_kcal = 5
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec):
    risk_level = "High Risk"; rec_kcal = 10
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2:
    risk_level = "High Risk"; rec_kcal = 10
elif days_starved > 5:
    risk_level = "At Risk"; rec_kcal = 15

st.subheader(f"Calculated Risk: {risk_level}")

# --- STEP 2: INITIAL MANAGEMENT ---
st.header("Step 2: Initial Management")
if risk_level == "Extremely High Risk":
    st.error(f"**Feeding:** Start at {rec_kcal} kcal/kg/day. Increase to full requirements by day 7.")
elif risk_level == "High Risk":
    st.warning(f"**Feeding:** Start at {rec_kcal} kcal/kg/day. Increase to full requirements by days 4-7.")
elif risk_level == "At Risk":
    st.info("**Feeding:** Start at max 50% of nutritional requirements for the first 2 days.")

kcal_slider = st.slider("Target Initial Energy (kcal/kg/day):", min_value=5, max_value=35, value=rec_kcal)
daily_target = round(weight * kcal_slider)
st.success(f"**Initial Energy Target: {daily_target} kcal/day**")

st.write("### Vitamin Supplementation (Start Day 1)")
st.markdown("""
* **Thiamine:** 50mg QDS for 10 days.
* **Vitamin B Co Strong:** 2 tablets TDS for 10 days.
* **Forceval:** 1 capsule daily.
* *If IV only:* **Pabrinex** Pairs 1 & 2 TDS for 10 days.
""")

# --- STEP 3: ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Laboratory Monitoring & Correction")
analyte = st.selectbox("Select abnormal electrolyte:", ["None", "Potassium (K+)", "Magnesium (Mg)", "Phosphate (PO4)", "Calcium (Adj)"])

treatment_note = ""

if analyte == "Potassium (K+)":
    val_k = st.number_input("Serum K+ (mmol/L)", min_value=0.0, step=0.1)
    if 0.1 <= val_k < 3.5:
        st.warning("#### ⚠️ Clinical Action: Review ECG for Hypokalaemia")
        
        if val_k < 2.5:
            treatment_note = "40mmol K+ in 1L 0.9% NaCl IV over min 4 hours. Check serum K+ every 12h."
        else:
            treatment_note = "2 tablets Sando-K TDS/QDS or 40mmol K+ IV over 8 hours."
    elif val_k >= 5.5:
        st.error("#### 🚨 Clinical Action: Hyperkalaemia Management")
        
        treatment_note = "Stop all K+ supplements. Urgent medical review. Contact nutrition team."

elif analyte == "Magnesium (Mg)":
    val_mg = st.number_input("Serum Mg (mmol/L)", min_value=0.0, step=0.1)
    if val_mg < 0.5:
        treatment_note = "20mmol Mg Sulphate IV over 12 hours. Check every 12h."
    elif val_mg < 0.7:
        treatment_note = "5ml Mg Hydroxide TDS orally until >0.7. Check every 24h."

elif analyte == "Phosphate (PO4)":
    val_p = st.number_input("Serum PO4 (mmol/L)", min_value=0.0, step=0.1)
    if val_p < 0.3:
        treatment_note = "IV Sodium Glycerophosphate 20mmol over 8-12 hours. (50% dose if <45kg)."
    elif val_p < 0.7:
        treatment_note = "1-2 tablets Phosphate-Sandoz OD. Check every 24h."

elif analyte == "Calcium (Adj)":
    val_ca = st.number_input("Adjusted Calcium (mmol/L)", min_value=0.0, step=0.1)
    if val_ca < 2.2:
        treatment_note = "Correct Magnesium first. If Ca <1.9 or symptomatic: 10ml Calcium Gluconate 10% IV over 10 mins."

if treatment_note:
    st.info(f"**Treatment Advice:** {treatment_note}")

# --- STEP 4: REPORT GENERATION ---
st.divider()
st.header("Step 4: Clinical Summary")
patient_id = st.text_input("Patient Identifier (e.g., Initials/Hospital Number)")

if st.button("Generate Summary"):
    summary = f"""
    REFEEDING RISK ASSESSMENT
    Date: {datetime.date.today()}
    Patient ID: {patient_id}
    ---------------------------
    Risk Level: {risk_level}
    Weight: {weight}kg | BMI: {bmi}
    Initial Target: {daily_target} kcal/day ({kcal_slider} kcal/kg/day)
    
    Management Plan:
    - Vitamins: Thiamine 50mg QDS, Vit B Co Strong 2 tabs TDS, Forceval OD.
    - Electrolyte Correction: {treatment_note if treatment_note else 'None required at assessment'}
    - Monitoring: Daily U&Es, Mg, PO4, Glucose.
    """
    st.text_area("Copy/Paste to Notes:", summary, height=250)
    
    # Simple TXT download for local records
    st.download_button("Download Summary (.txt)", summary, file_name=f"Refeeding_{patient_id}.txt")

st.caption("Note: This tool is a clinical decision aid and does not replace professional judgment.")
