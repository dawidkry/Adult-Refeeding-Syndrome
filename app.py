import streamlit as st

st.set_page_config(page_title="Refeeding Syndrome Guide", layout="centered")

# --- SIDEBAR: MOVING REFERENCE RANGES ---
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
if bmi < 14 or days_starved > 15:
    risk_level = "Extremely High Risk"
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec):
    risk_level = "High Risk"
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2:
    risk_level = "High Risk"
elif days_starved > 5:
    risk_level = "At Risk"

st.subheader(f"Calculated Risk: {risk_level}")

# --- STEP 2: INITIAL FEEDING & VITAMINS ---
st.header("Step 2: Initial Management")

if risk_level == "Extremely High Risk":
    st.error("**Feeding:** Start at 5 kcal/kg/day. Increase to full requirements by day 7.")
    st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring.")
elif risk_level == "High Risk":
    st.warning("**Feeding:** Start at 10 kcal/kg/day. Increase to full requirements by days 4-7.")
elif risk_level == "At Risk":
    st.info("**Feeding:** Start at max 50% of nutritional requirements for the first 2 days.")

st.write("### Vitamin Supplementation (Start Day 1)")
st.info("Give first dose at least 30 mins before feeding starts.")
st.markdown("""
* **Thiamine:** 50mg QDS (4 times a day) for 10 days.
* **Vitamin B Co Strong:** 2 tablets TDS (3 times a day) for 10 days.
* **Forceval:** 1 capsule/tablet daily.
* *If IV only:* **Pabrinex** Pairs 1 & 2 TDS for 10 days.
""")

# --- STEP 3: BIOCHEMISTRY & ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Laboratory Monitoring & Correction")

st.
