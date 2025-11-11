# Bias Audit of COMPAS Recidivism Dataset

This audit analyzes racial bias in the COMPAS dataset using IBM’s AI Fairness 360 toolkit. The dataset predicts recidivism risk but has been criticized for unfairly assigning higher risk scores to African-American defendants compared to Caucasian defendants.

Using **BinaryLabelDatasetMetric**, the analysis revealed a **disparate impact ratio below 1.0**, indicating that African-American defendants were less likely to receive favorable predictions. The **mean outcome difference** further confirmed unequal treatment between racial groups.

To mitigate bias, we applied the **Reweighing** algorithm, which adjusts instance weights to balance outcomes between privileged and unprivileged groups. Post-correction, the disparate impact ratio improved toward 1.0, suggesting fairer treatment.

**Key findings:**
- Pre-mitigation results showed significant racial disparity.
- Reweighing reduced bias without retraining the model.
- Fairness visualization confirmed a measurable improvement.

**Remediation steps:**
1. Integrate fairness preprocessing (like reweighing) in model pipelines.  
2. Regularly audit datasets using AI Fairness 360 or similar tools.  
3. Implement fairness-aware metrics in model evaluation.  

This audit highlights the importance of combining **technical fairness methods** with **ethical governance** to ensure equitable AI decision-making in justice systems.
