import streamlit as st

# Page Config
st.set_page_config(page_title="Refeeding Syndrome Tool", page_icon="🏥")

st.title("Adult Refeeding Syndrome Clinical Tool")
st.info("Based on Taunton and Somerset NHS Foundation Trust Guidelines")

# --- SECTION 1: RISK STRATIFICATION ---
st.header("1. Risk Assessment")
st.write("Select all criteria that apply to the patient:")

col1, col2 = st.columns(2)

with col1:
    bmi_under_16 = st.checkbox("BMI < 16 kg/m²")
    weight_loss_15 = st.checkbox("Unintentional weight loss > 15% (3-6 months)")
    starved_10 = st.checkbox("Little/no nutrition > 10 days")
    low_baseline = st.checkbox("Low baseline K+, PO4, or Mg (prior to feed)")

with col2:
    # Extremely high risk criteria
    bmi_under_14 = st.checkbox("BMI < 14 kg/m²")
    starved_15 = st.checkbox("Little/no nutrition > 15 days")

# Calculation Logic
risk_status = "Standard/Low Risk"
if bmi_under_14 or starved_15:
    risk_status = "Extremely High Risk"
elif bmi_under_16 or weight_loss_15 or starved_10 or low_baseline:
    risk_status = "High Risk"

st.subheader(f"Patient Status: :red[{risk_status}]")

# --- SECTION 2: MANAGEMENT PLAN ---
st.header("2. Initial Management Plan")

if risk_status == "Extremely High Risk":
    st.error("⚠️ **Feeding:** Consider starting at 5 kcal/kg/day. Increase to full requirements by day 7.")
    st.warning("Monitor cardiac rhythm continuously.")
elif risk_status == "High Risk":
    st.warning("⚠️ **Feeding:** Start at 10 kcal/kg/day. Increase to full requirements by days 4-7.")
else:
    st.success("✅ **Feeding:** Limit to 50% of requirements for the first 2 days.")

# Vitamin Protocol
st.subheader("Vitamin Prophylaxis")
st.markdown("""
- **Timeline:** Give first dose at least **30 mins before** feeding starts.
- **Oral:** Thiamine 50mg QDS, Vitamin B Co Strong 2 tabs TDS, Forceval 1 cap OD.
- **IV (Pabrinex):** 1 pair TDS for 10 days if oral route unavailable.
""")

# --- SECTION 3: ELECTROLYTE REPLACEMENT ---
st.header("3. Electrolyte Replacement (Logic-Based)")

analyte = st.selectbox("Select Abnormal Lab Result:", ["None", "Potassium (K+)", "Phosphate (PO4)", "Magnesium (Mg)"])

if analyte == "Potassium (K+)":
    val = st.number_input("Serum K+ (mmol/L)", min_value=0.0, max_value=7.0, step=0.1)
    if val < 2.5:
        st.error("IV Replacement: 40mmol K+ in 1L 0.9% NaCl over min 4 hours.")
        st.warning("CRITICAL: Continuous ECG monitoring required if infusion > 20mmol/hr.")
    elif val < 3.5:
        st.info("Oral Replacement: 2 tablets Sando-K TDS/QDS.")

elif analyte == "Phosphate (PO4)":
    val = st.number_input("Serum PO4 (mmol/L)", min_value=0.0, max_value=3.0, step=0.1)
    if val < 0.3:
        st.error("IV Sodium Glycerophosphate 20mmol over 8-12 hours.")
    elif val < 0.7:
        st.info("Oral Phosphate-Sandoz 1-2 tablets daily.")

# Footer
st.divider()
st.caption("Disclaimer: This tool is for clinical guidance only and does not replace professional judgment or local policy.")
