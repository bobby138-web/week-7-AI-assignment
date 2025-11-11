# AI Ethics Assignment - Week 7

## Overview

This repository contains the AI Ethics assignment for Week 7, covering theoretical understanding, case study analysis, practical dataset audit, and ethical reflections.

## Folder Structure

```
compas_audit_project/
├── audit_bias.py        # Python script for bias audit using AI Fairness 360
├── report.md            # Summary report of findings and remediation steps
├── data/                # Folder containing the COMPAS dataset
└── README.md            # This file
```

## Part 1: Theoretical Understanding

* Short answer questions on algorithmic bias, transparency vs explainability, and GDPR.
* Ethical principles matching.

## Part 2: Case Study Analysis

* **Case 1:** Biased hiring tool (Amazon example)
* **Case 2:** Facial recognition system in policing
* Includes identification of bias, ethical risks, fixes, and fairness metrics.

## Part 3: Practical Audit

* Audit of the COMPAS Recidivism Dataset using Python, Pandas, Matplotlib, and IBM AI Fairness 360.
* Generates metrics such as disparate impact and mean outcome differences.
* Visualization of bias before and after mitigation.
* Includes `audit_bias.py` and `report.md`.

## Part 4: Ethical Reflection

* Personal reflection on ensuring adherence to ethical AI principles in future projects.

## Bonus Task

* Drafted 1-page policy guideline for ethical AI use in healthcare.
* Covers patient consent protocols, bias mitigation, and transparency requirements.

## Requirements

* Python 3.x
* Libraries: `pandas`, `matplotlib`, `aif360`

## Usage

1. Install required libraries:

   ```bash
   pip install pandas matplotlib aif360
   ```
2. Run the bias audit script:

   ```bash
   python audit_bias.py
   ```
3. View the generated report in `report.md`.

## References

* IBM AI Fairness 360: [https://aif360.mybluemix.net/](https://aif360.mybluemix.net/)
* GDPR Guidelines: [https://gdpr-info.eu/](https://gdpr-info.eu/)
* ProPublica COMPAS Analysis: [https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and-analysis](https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and-analysis)
