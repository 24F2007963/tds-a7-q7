# employee_analysis.py
# Author: 24f2007963@ds.study.iitm.ac.in

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate synthetic employee dataset
np.random.seed(42)
departments = ["R&D", "Sales", "HR", "Marketing", "Finance"]
regions = ["North", "South", "East", "West"]

data = {
    "EmployeeID": range(1, 101),
    "Department": np.random.choice(departments, size=100, p=[0.2, 0.3, 0.2, 0.2, 0.1]),
    "Region": np.random.choice(regions, size=100)
}

df = pd.DataFrame(data)

# Optional: Save dataset (if needed)
# df.to_csv("employee_data.csv", index=False)

# 2. Frequency count for "R&D" department
rd_count = (df["Department"] == "R&D").sum()
print(f"Frequency count for R&D department: {rd_count}")

# 3. Create histogram of departments
plt.figure(figsize=(8,6))
sns.countplot(x="Department", data=df, palette="Set2")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save the plot as HTML using mpld3
import mpld3
html_str = mpld3.fig_to_html(plt.gcf())
with open("employee_department_histogram.html", "w") as f:
    f.write(html_str)

print("Histogram saved as 'employee_department_histogram.html'")
