# Adult Refeeding Syndrome Clinical Decision Support Tool

An interactive clinical application designed for medical and nursing staff to facilitate the identification, stratification, and management of metabolic complications during the reintroduction of nutrition.

## 🏥 Clinical Context
Refeeding Syndrome involves serious metabolic disturbances—specifically electrolyte shifts and fluid imbalances—that occur when nutrition is reintroduced to starved or malnourished patients. This condition is potentially fatal if not recognized and managed promptly.

This digital tool is based on the Adult Refeeding Syndrome Guidelines from the Taunton and Somerset NHS Foundation Trust, led by Dr. Daniel Pearl and Dr. Emma Wesley.

## 🚀 Key Features

### 1. Risk Stratification Engine
The tool automates the assessment of patient risk levels based on clinical criteria:
* **At Risk:** Patients with little or no nutrition for >5 days.
* **High Risk:** BMI <16 kg/m², weight loss >15% in 3-6 months, little/no nutrition for >10 days, or low baseline electrolytes.
* **Extremely High Risk:** BMI <14 kg/m² or starvation for >15 days.

### 2. Tailored Feeding Regimens
Provides specific caloric starting points based on the calculated risk:
* **Extremely High Risk:** Start at 5 kcal/kg/day and increase gradually to meet full requirements by day 7.
* **High Risk:** Start at 10 kcal/kg/day, increasing gradually to meet full requirements by days 4-7.
* **At Risk:** Initial feed at maximum 50% of requirements for the first two days.

### 3. Dynamic Electrolyte Management
Interactive logic for correcting biochemical abnormalities based on Trust replacement charts:
* **Potassium (K+):** Dosing protocols for oral (Sando-K) and IV infusions.
* **Phosphate (PO4):** Guided replacement using Phosphate-Sandoz or IV Sodium Glycerophosphate.
* **Magnesium (Mg):** Management paths for oral Magnesium Hydroxide vs. IV Magnesium Sulphate.

### 4. Patient Safety & Clinical Governance
* **Prophylaxis:** The first dose of vitamins and minerals must be administered at least 30 minutes before feeding.
* **Hierarchy of Correction:** Potassium and magnesium should be corrected first, then calcium and finally phosphate to prevent secondary drops.
* **Safety Monitoring:** Continuous ECG monitoring is essential if Potassium infusion rates exceed 20 mmol/hr.

## ✅ Clinical Validation & Logic Mapping
The application logic has been cross-referenced with official Trust flowcharts to ensure dosing accuracy:
* **Electrolyte Hierarchy:** Enforces correction of K+ and Mg before PO4 to prevent further electrolyte depletion.
* **Route Suitability:** Logic differentiates between oral and IV routes based on serum levels (e.g., PO4 <0.3 mmol/l requiring IV).
* **Dose Adjustments:** Includes specific instructions for patients <45 kg, such as a 50% reduction for certain IV Phosphate doses.

## 🛠 Technical Stack
* **Language:** Python 3.x
* **Framework:** Streamlit
* **Deployment:** GitHub / Streamlit Cloud

## ⚖️ Disclaimer
This tool is a digital reference for the Taunton and Somerset NHS Foundation Trust guidelines. It is intended for use in adult inpatient areas only and excludes Paediatrics. All clinical decisions should be made in conjunction with the multidisciplinary Nutrition Team.
