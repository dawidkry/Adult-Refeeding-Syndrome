import streamlit as st

st.header("3. Biochemistry Monitoring & Replacement")

# Displaying standard monitoring frequency from Table 1 [cite: 90]
st.subheader("Standard Monitoring Frequency")
st.info("""
**Daily until stable, then twice weekly:**
- Sodium, Potassium, Calcium, Phosphate, and Magnesium[cite: 90].
- **Note:** By day 7, if stable, frequency can be reduced to 2-3 times a week[cite: 94].
""")

# Electrolyte Replacement Logic
st.subheader("Electrolyte Replacement Protocols")
st.warning("Potassium and magnesium should be corrected first, then calcium and finally phosphate[cite: 97].")

analyte = st.selectbox("Select Electrolyte to Review:", ["Select...", "Potassium (K+)", "Phosphate (PO4)", "Magnesium (Mg)"])

if analyte == "Potassium (K+)":
    # Logic from Chart 3 [cite: 164]
    val = st.number_input("Current Serum K+ (mmol/L):", step=0.1)
    if 3.0 <= val < 3.5:
        st.write("**Action:** 2 tablets Sando-K TDS orally OR 40 mmol K+ IV in 1L 0.9% NaCl over min 8 hours[cite: 168, 171].")
        st.write("**Monitoring:** Check serum K+ every 24 hours[cite: 176].")
    elif 2.5 <= val < 3.0:
        st.write("**Action:** 2 tablets Sando-K QDS orally OR 40 mmol K+ IV in 1L 0.9% NaCl over min 8 hours[cite: 172, 175].")
        st.write("**Monitoring:** Check serum K+ every 24 hours[cite: 178].")
    elif val < 2.5:
        st.error("**Action:** 40 mmol K+ in 1L 0.9% NaCl IV over min 4 hours[cite: 183].")
        st.error("**Safety:** Continuous ECG monitoring is essential for infusion rates > 20 mmol/hr.")
        st.write("**Monitoring:** Check serum K+ every 12 hours[cite: 184].")

elif analyte == "Phosphate (PO4)":
    # Logic from Chart 1 [cite: 122]
    val = st.number_input("Current Serum PO4 (mmol/L):", step=0.1)
    is_under_45kg = st.checkbox("Patient weight < 45kg?")
    
    if 0.5 <= val < 0.7:
        st.write("**Action:** 1 tablet Phosphate-Sandoz OD. If oral route unsuitable, contact Nutrition Team[cite: 125, 126].")
        st.write("**Monitoring:** Check serum PO4 every 24 hours[cite: 134].")
    elif 0.3 <= val < 0.5:
        suitable = st.radio("Is oral route suitable?", ["Yes", "No"])
        if suitable == "Yes":
            st.write("**Action:** 2 tablets Phosphate-Sandoz OD[cite: 131].")
            st.write("**Monitoring:** Check serum PO4 every 24 hours[cite: 134].")
        else:
            dose = "10 mmol (reduced)" if is_under_45kg else "20 mmol"
            st.write(f"**Action:** IV Sodium Glycerophosphate ({dose}) in 1L 0.9% NaCl over 8-12 hours[cite: 137, 138, 139].")
            st.write("**Monitoring:** Check serum PO4/Ca/K/Mg every 12 hours[cite: 143].")
    elif val < 0.3:
        dose = "10 mmol (reduced)" if is_under_45kg else "20 mmol"
        st.error(f"**Action:** IV Sodium Glycerophosphate ({dose}) in 1L 0.9% NaCl over 8-12 hours[cite: 140, 142].")
        st.write("**Monitoring:** Check serum PO4/Ca/K/Mg every 12 hours[cite: 143].")

elif analyte == "Magnesium (Mg)":
    # Logic from Chart 2 [cite: 149]
    val = st.number_input("Current Serum Mg (mmol/L):", step=0.1)
    if 0.5 <= val < 0.7:
        st.write("**Action:** 5 ml Magnesium Hydroxide TDS orally until serum > 0.7, then 5 ml BD for 48 hrs[cite: 153].")
        st.write("**Monitoring:** Check serum Mg every 24 hours[cite: 154].")
    elif val < 0.5:
        st.error("**Action:** 20 mmol Magnesium Sulphate IV over 12 hours[cite: 155].")
        st.write("**Monitoring:** Check serum Mg every 12 hours[cite: 156].")
