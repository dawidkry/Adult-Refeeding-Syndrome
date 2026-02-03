# Adult Refeeding Syndrome Clinical Decision Support Tool

[cite_start]An interactive clinical tool designed for medical and nursing staff to prevent, identify, and manage metabolic complications during the reintroduction of nutrition[cite: 10, 15].

## 🏥 Clinical Background
[cite_start]Refeeding Syndrome refers to serious metabolic disturbances (electrolyte shifts and fluid imbalance) that occur when nutrition is reintroduced to starved or malnourished patients[cite: 19, 25]. [cite_start]It is potentially fatal if not recognized promptly[cite: 20].

[cite_start]This application digitizes the **Adult Refeeding Syndrome Guidelines** authored by Natalie Buck (Nutrition Specialist Dietitian) and Lead Consultants Dr. Daniel Pearl & Dr. Emma Wesley[cite: 5, 7].

## 🚀 Key Features

### 1. Automated Risk Stratification
[cite_start]The tool processes patient data to categorize risk according to Trust criteria[cite: 43]:
* [cite_start]**At Risk:** Little/no nutrition for >5 days[cite: 45].
* [cite_start]**High Risk:** BMI <16, weight loss >15%, or low baseline electrolytes (K+, PO4, Mg)[cite: 48, 49, 51].
* [cite_start]**Extremely High Risk:** BMI <14 or little/no nutrition for >15 days[cite: 59, 60].

### 2. Evidence-Based Feeding Protocols
Provides specific starting regimens based on risk level:
* [cite_start]**Extremely High Risk:** Consider starting at $5~kcal/kg/day$[cite: 79].
* [cite_start]**High Risk:** Start at $10~kcal/kg/day$, increasing over 4–7 days[cite: 72].
* [cite_start]**Standard Risk:** Start at max 50% of requirements for the first 2 days[cite: 65].

### 3. Dynamic Electrolyte Replacement Logic
[cite_start]Interactive flowcharts for correcting deficiencies[cite: 96, 122, 149, 164]:
* [cite_start]**Potassium (K+):** Dosing for oral (Sando-K) vs. IV (40mmol infusion)[cite: 168, 171].
* [cite_start]**Phosphate (PO4):** Dosing for Phosphate-Sandoz vs. IV Sodium Glycerophosphate[cite: 125, 137].
* [cite_start]**Magnesium (Mg):** Oral Magnesium Hydroxide vs. IV Magnesium Sulphate[cite: 153, 155].

### 4. Safety Guardrails
* [cite_start]**Pre-feeding Vitamins:** Highlights that the first dose of vitamins must be given at least 30 minutes before feeding[cite: 110].
* [cite_start]**Infusion Monitoring:** Critical alert for continuous ECG monitoring if K+ infusion exceeds 20 mmol/hr[cite: 185].
* [cite_start]**Correction Hierarchy:** Reminds clinicians to correct K+ and Mg before PO4 to avoid further electrolyte drops[cite: 97, 98].

## 🛠 Technical Setup
This app is built with **Python** and **Streamlit**.

1. **Clone the repo:** `git clone https://github.com/your-username/refeeding-guidelines.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run the app:** `streamlit run app.py`

## ⚖️ Disclaimer & Governance
[cite_start]This tool is a digital representation of the Taunton and Somerset NHS Foundation Trust guidelines[cite: 2, 3]. [cite_start]It is intended for adult inpatient areas (Excludes Paediatrics)[cite: 10, 14]. [cite_start]Clinical decisions should always involve a Dietitian and be confirmed against the Trust's active policy database[cite: 16, 21].
