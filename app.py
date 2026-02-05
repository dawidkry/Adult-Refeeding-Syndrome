import streamlit as st

# --- CONFIGURATION & HEADER ---
st.set_page_config(page_title="Adult Refeeding Guideline", layout="centered")

st.title("Adult Refeeding Syndrome Clinical Tool")
st.caption("Based on Taunton and Somerset NHS Foundation Trust Guidelines [cite: 2, 4]")

# --- STEP 1: RISK ASSESSMENT ---
st.header("Step 1: Risk Assessment")
st.info("Identify patients at risk of refeeding syndrome prior to initiating nutrition[cite: 37].")

with st.expander("Patient Assessment Criteria", expanded=True):
    col_a, col_b = st.columns(2)
    with col_a:
        bmi = st.number_input("Current BMI (kg/m²) [cite: 48, 53, 59, 61]", min_value=5.0, max_value=50.0, value=20.0, step=0.1)
        weight_loss = st.number_input("Unintentional weight loss in last 3-6 months (%) [cite: 49, 54, 62]", min_value=0.0, max_value=100.0, value=0.0)
    with col_b:
        days_starved = st.number_input("Days with little or no nutrition [cite: 45, 50, 60]", min_value=0, max_value=100, value=0)
        low_elec_baseline = st.checkbox("Low baseline K+, PO4, or Mg (prior to feeding) [cite: 51]")

    st.write("**Additional Factors (High Risk if 2 or more met with BMI <18.5)[cite: 52]:**")
    col_c, col_d = st.columns(2)
    with col_c:
        alcohol = st.checkbox("History of alcohol excess [cite: 56]")
    with col_d:
        meds = st.checkbox("New insulin, chemotherapy, antacids, or diuretics [cite: 57]")

# Risk Logic Implementation
risk_level = "Standard Risk"
if bmi < 14 or days_starved > 15:
    risk_level = "Extremely High Risk"
elif (bmi < 16 or weight_loss > 15 or days_starved > 10 or low_elec_baseline):
    risk_level = "High Risk"
elif ( (bmi < 18.5) + (weight_loss > 10) + (days_starved > 5) + alcohol + meds ) >= 2:
    risk_level = "High Risk"
elif days_starved > 5:
    risk_level = "At Risk"

if risk_level == "Extremely High Risk":
    st.error(f"Assessment: {risk_level}")
elif risk_level == "High Risk":
    st.warning(f"Assessment: {risk_level}")
else:
    st.success(f"Assessment: {risk_level}")

# --- STEP 2: INITIAL MANAGEMENT ---
st.header("Step 2: Initial Management")

# Feeding & Monitoring Guidance
if risk_level == "Extremely High Risk":
    st.markdown("### 🍴 Feeding Plan")
    st.write("* Start at **5 kcal/kg/day**[cite: 79].")
    st.write("* Increase gradually to meet full requirements by day 7[cite: 79].")
    st.write("* **Cardiac Monitoring:** Consider continuous cardiac rhythm monitoring[cite: 84].")
elif risk_level == "High Risk":
    st.markdown("### 🍴 Feeding Plan")
    st.write("* Start at **10 kcal/kg/day**[cite: 72].")
    st.write("* Increase gradually to meet full requirements by days 4-7[cite: 72].")
elif risk_level == "At Risk":
    st.markdown("### 🍴 Feeding Plan")
    st.write("* Start at maximum **50% of nutritional requirements** for the first 2 days[cite: 65].")

# Prophylaxis
st.markdown("### 💊 Vitamin Prophylaxis (Start Day 1)")
st.warning("First dose must be given at least 30 minutes BEFORE feeding[cite: 110].")
st.markdown("""
* **Thiamine:** 50 mg four times a day (QDS) for 10 days[cite: 106].
* **Vitamin B Co Strong:** 2 tablets three times a day (TDS) for 10 days[cite: 105].
* **Forceval:** 1 capsule (or soluble tablet) daily for 10 days[cite: 102, 103].
* **If I.V. required:** Pabrinex vials 1 and 2 three times a day (TDS) for 10 days[cite: 109].
""")

# --- STEP 3: LABORATORY MONITORING & CORRECTION ---
st.header("Step 3: Laboratory Monitoring & Correction")
st.write("Monitor biochemistry daily until stable, then twice weekly[cite: 90].")

# Hierarchy Alert
st.warning("⚠️ **Correction Priority:** Correct K+ and Mg first, then Calcium, and finally Phosphate[cite: 97].")

analyte = st.selectbox("Select electrolyte to review:", ["Potassium (K+)", "Magnesium (Mg)", "Phosphate (PO4)"])

# POTASSIUM LOGIC
if analyte == "Potassium (K+)":
    k_val = st.number_input("Current Serum K+ (mmol/L):", min_value=0.0, step=0.1)
    
    if k_val > 0 and k_val < 3.5:
        st.subheader("⚠️ ECG Guidance: Hypokalaemia")
        st.markdown("""
        **Classic ECG Changes to monitor:**
        * Flattened or inverted T-waves.
        * **Prominent U-waves** (following the T-wave).
        * ST-segment depression.
        * Prolonged PR interval.
        """)
        
        if k_val < 2.5:
            st.error("**Treatment (Severe):** 40 mmol K+ in 1L 0.9% NaCl I.V. over min 4 hours[cite: 183].")
            st.error("🚨 Continuous ECG monitoring is ESSENTIAL (infusion > 20 mmol/hr)[cite: 185].")
            st.write("**Repeat Bloods:** Every 12 hours[cite: 184].")
        elif k_val < 3.0:
            st.warning("**Treatment (Moderate):** 2 tablets Sando-K QDS (72 mmol/day) OR 40 mmol K+ I.V. over min 8 hours[cite: 172, 175].")
            st.write("**Repeat Bloods:** Every 24 hours[cite: 177].")
        else:
            st.info("**Treatment (Mild):** 2 tablets Sando-K TDS (72 mmol/day) OR 40 mmol K+ I.V. over min 8 hours[cite: 168, 171].")
            st.write("**Repeat Bloods:** Every 24 hours[cite: 176].")
            
    elif k_val > 5.5:
        st.subheader("🚨 ECG Guidance: Hyperkalaemia")
        st.markdown("""
        **Clinical Urgency - monitor for:**
        * **Tall, tented (peaked) T-waves.**
        * P-wave flattening or loss.
        * **Widening of the QRS complex** (Warning: Imminent cardiac arrest).
        """)

# MAGNESIUM LOGIC
elif analyte == "Magnesium (Mg)":
    mg_val = st.number_input("Current Serum Mg (mmol/L):", min_value=0.0, step=0.05)
    
    if mg_val > 0 and mg_val < 0.5:
        st.error("**Treatment (Severe):** 20 mmol Magnesium Sulphate I.V. over 12 hours[cite: 155].")
        st.write("**Repeat Bloods:** Every 12 hours[cite: 156].")
    elif 0.5 <= mg_val < 0.7:
        st.warning("**Treatment (Mild/Moderate):** 5 ml Magnesium Hydroxide TDS orally (21 mmol Mg) until level > 0.7, then BD for 48 hrs[cite: 153].")
        st.write("**Repeat Bloods:** Every 24 hours[cite: 154].")

# PHOSPHATE LOGIC
elif analyte == "Phosphate (PO4)":
    po4_val = st.number_input("Current Serum PO4 (mmol/L):", min_value=0.0, step=0.05)
    
    if po4_val > 0 and po4_val < 0.3:
        st.error("**Treatment (Severe):** I.V. Sodium Glycerophosphate 20 mmol in 1L 0.9% NaCl over 8-12 hours[cite: 142].")
        st.write("**Repeat Bloods:** Every 12 hours[cite: 143].")
    elif 0.3 <= po4_val < 0.5:
        st.warning("**Treatment (Moderate):** If oral route suitable: 2 tablets Phosphate-Sandoz OD (32 mmol). If I.V. needed: 20 mmol over 8-12 hours[cite: 131, 137, 138].")
        st.write("**Repeat Bloods:** Every 12-24 hours[cite: 134, 143].")
    elif 0.5 <= po4_val < 0.7:
        st.info("**Treatment (Mild):** 1 tablet Phosphate-Sandoz OD (16 mmol)[cite: 125].")
        st.write("**Repeat Bloods:** Every 24 hours[cite: 134].")

st.divider()
st.caption("Disclaimer: This tool is for clinical guidance for medical staff. Always consult a Dietitian and local Trust policies[cite: 21, 32].")
