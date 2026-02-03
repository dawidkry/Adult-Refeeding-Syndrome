import streamlit as st

# --- 1. PAGE CONFIG ---
# Force the sidebar to be open (expanded) by default
st.set_page_config(
    page_title="Refeeding Syndrome Tool", 
    page_icon="🏥", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- 2. MINIMAL CSS ---
# We are ONLY hiding the 'Made with Streamlit' footer and the 'Deploy' button.
# We are NOT hiding the sidebar or the header icons to ensure stability.
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            .stAppDeployButton {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 3. THE SIDEBAR (Reference Ranges) ---
with st.sidebar:
    st.header("Normal Reference Ranges")
    st.markdown("""
    *Standard adult norms:*
    - **Potassium (K+):** 3.5 – 5.5 mmol/L
    - **Phosphate (PO4):** 0.8 – 1.5 mmol/L
    - **Magnesium (Mg):** 0.7 – 1.0 mmol/L
    - **Corrected Calcium:** 2.2 – 2.6 mmol/L
    - **Sodium (Na+):** 135 – 145 mmol/L
    """)
    st.divider()
    st.info("**MDT Reminder:** A Dietitian should be involved at the earliest opportunity.")

# --- 4. MAIN CONTENT ---
st.title("Adult Refeeding Syndrome Clinical Decision Support")
st.caption("Based on Taunton and Somerset NHS Foundation Trust Guidelines")

# --- STEP 1: RISK ASSESSMENT ---
st.header("Step 1: Risk Assessment")
col1, col2 = st.columns(2)
with col1:
    st.subheader("High Risk Criteria")
    r1 = st.checkbox("BMI < 16 kg/m²")
    r2 = st.checkbox("Unintentional weight loss > 15% (3-6 months)")
    r3 = st.checkbox("Little/no nutrition > 10 days")
    r4 = st.checkbox("Low baseline K+, PO4, or Mg")
    st.divider()
    st.subheader("2+ Criteria Needed (High Risk):")
    c1 = st.checkbox("BMI < 18.5 kg/m²")
    c2 = st.checkbox("Weight loss > 10% (3-6 months)")
    c3 = st.checkbox("Little/no nutrition > 5 days")
    c4 = st.checkbox("History of alcohol excess")
    c5 = st.checkbox("New therapy (insulin, chemo, antacids, diuretics)")

with col2:
    st.subheader("Extremely High Risk Criteria")
    ex1 = st.checkbox("BMI < 14 kg/m²")
    ex2 = st.checkbox("Little/no nutrition > 15 days")

# Risk Level Logic
risk_level = "At Risk (Standard)"
if ex1 or ex2:
    risk_level = "Extremely High Risk"
elif r1 or r2 or r3 or r4 or (sum([c1, c2, c3, c4, c5]) >= 2):
    risk_level = "High Risk"
elif c3:
    risk_level = "At Risk"

st.info(f"Calculated Risk Category: **{risk_level}**")

# --- STEP 2: INITIAL MANAGEMENT ---
st.header("Step 2: Initial Management Plan")
if risk_level == "Extremely High Risk":
    st.error("**Feed:** Start at 5 kcal/kg/day. Increase to full by Day 7.")
    st.warning("**Monitoring:** Consider continuous cardiac rhythm monitoring.")
elif risk_level == "High Risk":
    st.warning("**Feed:** Start at 10 kcal/kg/day. Increase to full by Days 4-7.")
else:
    st.success("**Feed:** Max 50% of requirements for the first 2 days.")

with st.expander("Mandatory Vitamin Prophylaxis (Day 1-10)", expanded=True):
    st.markdown("""
    *Give first dose at least 30 mins before feeding:*
    * **Thiamine** 50mg QDS | **Vit B Co Strong** 2 tabs TDS | **Forceval** 1 cap OD
    * *If IV Only:* **Pabrinex** 1 pair TDS
    """)

# --- STEP 3: ELECTROLYTE REPLACEMENT ---
st.header("Step 3: Electrolyte Replacement & Monitoring")
rep_col, note_col = st.columns([2, 1])

with rep_col:
    analyte = st.selectbox("Select Abnormal Electrolyte:", ["None", "Potassium (K+)", "Phosphate (PO4)", "Magnesium (Mg)"])
    
    if analyte == "Potassium (K+)":
        k_val = st.number_input("Serum K+ (mmol/L):", step=0.1, format="%.1f")
        if 3.0 <= k_val < 3.5:
            st.write("**Action:** 2 tabs Sando-K TDS OR 40mmol K+ IV over 8h.")
        elif 2.5 <= k_val < 3.0:
            st.write("**Action:** 2 tabs Sando-K QDS OR 40mmol K+ IV over 8h.")
        elif k_val < 2.5:
            st.error("**Action:** 40mmol K+ IV over min 4 hours. **ECG monitoring required.**")

    elif analyte == "Phosphate (PO4)":
        p_val = st.number_input("Serum PO4 (mmol/L):", step=0.1, format="%.1f")
        u45 = st.checkbox("Weight < 45kg?")
        if 0.5 <= p_val < 0.7:
            st.write("**Action:** 1 tablet Phosphate-Sandoz OD.")
        elif p_val < 0.5:
            dose = "10mmol" if u45 else "20mmol"
            st.write(f"**Action:** 2 tablets Phosphate-Sandoz OD OR IV Sodium Glycerophosphate ({dose}).")

    elif analyte == "Magnesium (Mg)":
        mg_val = st.number_input("Serum Mg (mmol/L):", step=0.1, format="%.1f")
        if 0.5 <= mg_val < 0.7:
            st.write("**Action:** 5ml Magnesium Hydroxide TDS orally.")
        elif mg_val < 0.5:
            st.error("**Action:** 20mmol Magnesium Sulphate IV over 12 hours.")

with note_col:
    st.subheader("Clinical Notes")
    st.markdown("- Correct K+ and Mg before PO4.\n- Caution in renal impairment.")
    
    # YOUR PREFERRED SLIDER/TOGGLE
    is_parenteral = st.toggle("Patient is on Parenteral Nutrition?")
    if is_parenteral:
        st.warning("⚠️ **Glucose:** Monitor 6-hourly (QDS).")
    else:
        st.info("ℹ️ **Glucose:** Monitor Twice Daily (BD).")

# --- 6. PROFESSIONAL FOOTER ---
st.divider()
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.caption("**Active Date:** 22 May 2017")
with f_col2:
    st.caption("**Review Date:** 22 May 2020")
with f_col3:
    st.caption("**Lead:** Dr Daniel Pearl & Dr Emma Wesley")
