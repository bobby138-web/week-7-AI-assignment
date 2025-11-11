# audit_bias.py
# Bias audit using IBM AI Fairness 360

import pandas as pd
import matplotlib.pyplot as plt
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric
from aif360.algorithms.preprocessing import Reweighing

# Load dataset
dataset = CompasDataset()

# Define privileged and unprivileged groups
privileged_groups = [{'race': 1}]      # Caucasian
unprivileged_groups = [{'race': 0}]    # African-American

# Compute bias metrics
metric = BinaryLabelDatasetMetric(
    dataset,
    unprivileged_groups=unprivileged_groups,
    privileged_groups=privileged_groups
)

print("Difference in mean outcomes (Favorable Rate Gap):", metric.mean_difference())
print("Disparate Impact:", metric.disparate_impact())

# Apply reweighing to mitigate bias
rw = Reweighing(unprivileged_groups=unprivileged_groups,
                privileged_groups=privileged_groups)
dataset_transf = rw.fit_transform(dataset)

# Visualize before and after reweighing
labels = ['Before Reweighing', 'After Reweighing']
bias_values = [metric.disparate_impact(),
               BinaryLabelDatasetMetric(dataset_transf,
                                        unprivileged_groups=unprivileged_groups,
                                        privileged_groups=privileged_groups).disparate_impact()]

plt.bar(labels, bias_values)
plt.title("Disparate Impact Before and After Bias Mitigation")
plt.ylabel("Disparate Impact Ratio")
plt.show()
