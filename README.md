# Adult Refeeding Syndrome Clinical Decision Support Tool

[cite_start]An interactive clinical application designed for medical and nursing staff to facilitate the identification, stratification, and management of metabolic complications during the reintroduction of nutrition[cite: 10, 15].

## 🏥 Clinical Context
[cite_start]Refeeding Syndrome involves serious metabolic disturbances—specifically electrolyte shifts and fluid imbalances—that occur when nutrition is reintroduced to starved or malnourished patients[cite: 19]. [cite_start]This condition is potentially fatal if not recognized and managed promptly[cite: 20].

[cite_start]This digital tool is based on the **Adult Refeeding Syndrome Guidelines** from the Taunton and Somerset NHS Foundation Trust, led by Dr. Daniel Pearl and Dr. Emma Wesley[cite: 2, 7].

## 🚀 Key Features

### 1. Risk Stratification Engine
The tool automates the assessment of patient risk levels based on clinical criteria:
* [cite_start]**At Risk:** Patients with little or no nutrition for >5 days[cite: 45].
* [cite_start]**High Risk:** BMI <16 kg/m², weight loss >15% in 3-6 months, little/no nutrition for >10 days, or low baseline electrolytes[cite: 48, 49, 50, 51].
* [cite_start]**Extremely High Risk:** BMI <14 kg/m² or starvation for >15 days[cite: 59, 60].

### 2. Tailored Feeding Regimens
Provides specific caloric starting points based on the calculated risk:
* [cite_start]**Extremely High Risk:** Start at 5 kcal/kg/day and increase gradually to meet full requirements by day 7[cite: 79].
* [cite_start]**High Risk:** Start at 10 kcal/kg/day, increasing gradually to meet full requirements by days 4-7[cite: 72].
* [cite_start]**At Risk:** Initial feed at maximum 50% of requirements for the first two days[cite: 65].

### 3. Dynamic Electrolyte Management
Interactive logic for correcting biochemical abnormalities based on Trust replacement charts:
* [cite_start]**Potassium (K+):** Dosing protocols for oral (Sando-K) and IV infusions[cite: 168, 171, 183].
* [cite_start]**Phosphate (PO4):** Guided replacement using Phosphate-Sandoz or IV Sodium Glycerophosphate[cite: 125, 137].
* [cite_start]**Magnesium (Mg):** Management paths for oral Magnesium Hydroxide vs. IV Magnesium Sulphate[cite: 153, 155].

### 4. Patient Safety & Clinical Governance
* [cite_start]**Prophylaxis:** The first dose of vitamins and minerals must be administered at least 30 minutes before feeding[cite: 110].
* [cite_start]**Hierarchy of Correction:** Potassium and magnesium should be corrected first, then calcium and finally phosphate to prevent secondary drops[cite: 97, 98].
* [cite_start]**Safety Monitoring:** Continuous ECG monitoring is essential if Potassium infusion rates exceed 20 mmol/hr[cite: 185].

## ✅ Clinical Validation & Logic Mapping
The application logic has been cross-referenced with official Trust flowcharts to ensure dosing accuracy:
* [cite_start]**Electrolyte Hierarchy:** Enforces correction of K+ and Mg before PO4 to prevent further electrolyte depletion[cite: 97, 98].
* [cite_start]**Route Suitability:** Logic differentiates between oral and IV routes based on serum levels (e.g., PO4 <0.3 mmol/l requiring IV)[cite: 135, 137].
* [cite_start]**Dose Adjustments:** Includes specific instructions for patients <45 kg, such as a 50% reduction for IV Phosphate[cite: 139].

## 🛠 Technical Stack
* **Language:** Python 3.x
* **Framework:** Streamlit
* **Deployment:** GitHub / Streamlit Cloud

## ⚖️ Disclaimer
[cite_start]This tool is a digital reference for the Taunton and Somerset NHS Foundation Trust guidelines[cite: 1, 2]. [cite_start]It is intended for use in adult inpatient areas only and excludes Paediatrics[cite: 10, 14]. [cite_start]All clinical decisions should be made in conjunction with the multidisciplinary Nutrition Team[cite: 21].
