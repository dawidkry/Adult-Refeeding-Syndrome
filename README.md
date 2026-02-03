# Adult Refeeding Syndrome Clinical Decision Support Tool

An interactive clinical application designed for medical and nursing staff to facilitate the identification, stratification, and management of metabolic complications during the reintroduction of nutrition.

## 🏥 Clinical Context
Refeeding Syndrome involves serious metabolic disturbances—specifically electrolyte shifts and fluid imbalances—that occur when nutrition is reintroduced to starved or malnourished patients. This condition is potentially fatal if not recognized and managed promptly.

This digital tool is based on the **Adult Refeeding Syndrome Guidelines** from the Taunton and Somerset NHS Foundation Trust, led by Dr. Daniel Pearl and Dr. Emma Wesley (Consultant Gastroenterologists).

## 🚀 Key Features

### 1. Risk Stratification Engine
The tool automates the assessment of patient risk levels based on clinical criteria:
* **At Risk:** Patients with little or no nutrition for >5 days.
* **High Risk:** BMI <16 kg/m², weight loss >15% in 3-6 months, or low baseline electrolytes (K+, PO4, Mg).
* **Extremely High Risk:** BMI <14 kg/m² or starvation for >15 days.

### 2. Tailored Feeding Regimens
Provides specific caloric starting points based on the calculated risk:
* **Extremely High Risk:** Recommendations to start at $5~kcal/kg/day$.
* **High Risk:** Start at $10~kcal/kg/day$, increasing gradually over 4–7 days.
* **Standard Risk:** Initial feed at max 50% of requirements for the first 48 hours.

### 3. Dynamic Electrolyte Management
Interactive logic for correcting biochemical abnormalities:
* **Potassium (K+):** Dosing protocols for oral (Sando-K) and IV infusions, including the mandatory 20 mmol/hr safety cap.
* **Phosphate (PO4):** Guided replacement using Phosphate-Sandoz or IV Sodium Glycerophosphate.
* **Magnesium (Mg):** Management paths for oral Magnesium Hydroxide vs. IV Magnesium Sulphate.

### 4. Patient Safety & Clinical Governance
* **Prophylaxis:** Alerts clinicians that the first dose of vitamins (Thiamine/Pabrinex) must be administered at least 30 minutes before feeding.
* **Hierarchy of Correction:** Built-in reminders to prioritize Potassium and Magnesium correction before Phosphate to prevent secondary metabolic drops.
* **Monitoring:** Outlines the schedule for biochemical testing (daily until stable, then twice weekly).

## 🛠 Technical Stack
* **Language:** Python 3.x
* **Framework:** Streamlit
* **Deployment:** Optimized for GitHub and Streamlit Cloud

## ⚖️ Disclaimer
This tool is a digital reference for the Taunton and Somerset NHS Foundation Trust guidelines. It is intended for use in adult inpatient areas only (Excludes Paediatrics). All clinical decisions should be made in conjunction with the multidisciplinary Nutrition Team.
