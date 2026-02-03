import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Refeeding Syndrome Tool", 
    page_icon="🏥", 
    layout="wide",
    initial_sidebar_state="collapsed" # We'll hide the actual sidebar and build our own
)

# --- 2. CSS LOCKDOWN ---
hide_st_style = """
            <style>
            /* Hide the actual sidebar, header, and all developer menus */
            [data-testid="stSidebar"], 
            [data-testid="stHeader"], 
            [data-testid="stToolbar"], 
            #MainMenu, 
            footer {
                display: none !important;
            }
            
            .stAppDeployButton {display:none !important;}
            .block-container {padding-top: 1.5rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 3. MAIN LAYOUT (Creating a Permanent Sidebar Column) ---
# We split the page into a small left column (1) and a large main column (4)
side_col, main_col = st.columns([1, 4])

# --- FIXED LEFT COLUMN (Acts as your Sidebar) ---
with side_col:
    st.markdown("### 📊 Reference Ranges")
    st.info("""
    **Standard Adult Norms:**
    - **K+:** 3.5 – 5.5 mmol/L
    - **PO4:** 0.8 – 1.5 mmol/L
    - **Mg:** 0.7 – 1.0 mmol/L
    - **Ca:** 2.2 – 2.6 mmol/L
    - **Na+:** 135 – 145 mmol/L
    """)
    st.divider()
    st.caption("**MDT:** Consult Dietitian early.")
    st.caption("**Taunton & Somerset NHS Trust**")

# --- MAIN CONTENT ---
with main_col:
    st.title("Adult Refeeding Syndrome Clinical Decision Support")
    st.caption("Clinical Guidance Tool")

    # --- STEP 1: RISK ASSESSMENT ---
    st.header("Step 1: Risk Assessment")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("High Risk")
        r1 = st.checkbox("BMI < 16 kg/m²")
        r2 = st.checkbox("Unintentional weight loss > 15% (3-6 months)")
        r3 = st.checkbox("Little/no nutrition > 10 days")
        r4 = st.checkbox("Low baseline K+, PO4, or Mg")
        st.write("---")
        st.subheader("2+ Criteria Needed (High Risk)")
        c1 = st.checkbox("BMI < 18.5 kg/m²")
        c2 = st.checkbox("Weight loss > 10% (3-6 months)")
        c3 = st.checkbox("Little/no nutrition > 5 days")
        c4 = st.checkbox("History of alcohol excess")
        c5 = st.checkbox("New therapy (insulin, chemo, antacids, diuretics)")

    with col2:
        st.subheader("Extremely High Risk")
        ex1 = st.checkbox("BMI < 14 kg/m²")
        ex2 = st.checkbox("Little/no nutrition > 15 days")

    risk_level = "At Risk (Standard)"
    if ex1 or ex2:
        risk_level = "Extremely High Risk"
    elif r1 or r2 or r3 or r4 or (sum([c1, c2, c3, c4, c5]) >= 2):
        risk_level = "High Risk"
    elif c3:
        risk_level = "At Risk"

    st.warning(f"Calculated Risk Category: **{risk_level}**")

    # --- STEP 2: MANAGEMENT ---
    st.header("Step 2: Initial Management Plan")
    if risk_level == "Extremely High Risk":
        st.error("**Feed:** Start 5 kcal/kg/day. Increase to full by Day 7.")
    elif risk_level == "High Risk":
        st.warning("**Feed:** Start 10 kcal/kg/day. Increase to full by Day 4-7.")
    else:
        st.success("**Feed:** Max 50% requirements for first 2 days.")

    with st.expander("💊 Mandatory Vitamin Prophylaxis (Day 1-10)", expanded=True):
        st.markdown("**Give first dose at least 30 mins before feeding**")
        st.markdown("- **Thiamine:** 50mg QDS\n- **Vit B Co Strong:** 2 tabs TDS\n- **Forceval:** 1 cap OD\n- **Pabrinex:** 1 pair TDS (if IV)")

    # --- STEP 3: ELECTROLYTES ---
    st.header("Step 3: Electrolyte Replacement")
    rep_col, note_col = st.columns([2, 1])

    with rep_col:
        analyte = st.selectbox("Select Abnormal Electrolyte:", ["None", "Potassium (K+)", "Phosphate (PO4)", "Magnesium (Mg)"])
        if analyte == "Potassium (K+)":
            k_val = st.number_input("Serum K+ (mmol/L):", step=0.1)
            if k_val < 2.5: st.error("40mmol K+ IV over min 4h. **Continuous ECG required.**")
            elif k_val < 3.5: st.write("2 tabs Sando-K TDS/QDS OR 40mmol K+ IV over 8h.")
        
        elif analyte == "Phosphate (PO4)":
            p_val = st.number_input("Serum PO4 (mmol/L):", step=0.1)
            u45 = st.checkbox("Weight < 45kg?")
            if p_val < 0.5:
                dose = "10mmol" if u45 else "20mmol"
                st.write(f"2 tabs Phosphate-Sandoz OD OR IV Sodium Glycerophosphate ({dose}).")

    with note_col:
        st.subheader("Clinical Notes")
        st.markdown("- Correct K+ and Mg before PO4.")
        
        # CLEAR PARENTERAL NUTRITION TOGGLE
        is_parenteral = st.toggle("Patient is on Parenteral Nutrition?")
        if is_parenteral:
            st.warning("⚠️ **Glucose:** Monitor 6-hourly (QDS).")
        else:
            st.info("ℹ️ **Glucose:** Monitor Twice Daily (BD).")

    # --- FOOTER ---
    st.divider()
    f1, f2, f3 = st.columns(3)
    with f1: st.caption("**Active:** 22 May 2017")
    with f2: st.caption("**Review:** 22 May 2020")
    with f3: st.caption("**Lead:** Dr D Pearl & Dr E Wesley")
