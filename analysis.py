# employee_analysis.py
# Author: 24f2007963@ds.study.iitm.ac.in

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

# Generate synthetic data
np.random.seed(42)
departments = ["R&D", "Sales", "HR", "Marketing", "Finance"]
regions = ["North", "South", "East", "West"]

data = {
    "EmployeeID": range(1, 101),
    "Department": np.random.choice(departments, size=100, p=[0.2, 0.3, 0.2, 0.2, 0.1]),
    "Region": np.random.choice(regions, size=100)
}

df = pd.DataFrame(data)

# Frequency count for "R&D"
rd_count = (df["Department"] == "R&D").sum()
print(rd_count)
print(f"Frequency count for R&D department: {rd_count}")

# Create histogram
fig, ax = plt.subplots(figsize=(8,6))
sns.countplot(x="Department", data=df, palette="Set2", ax=ax)
ax.set_title("Employee Distribution by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Count")

# Convert matplotlib figure to HTML using mpld3
plot_html = mpld3.fig_to_html(fig)

# Inject JavaScript to print R&D count to browser console
js_console = f"""
<script>
console.log("Frequency count for R&D department: {rd_count}");
</script>
"""

# Final HTML combining plot + console JS
html_content = f"""
<html>
<head>
<title>Employee Department Histogram</title>
</head>
<body>
<h2>Employee Department Histogram</h2>
<h3>Frequency count for R&D department: {rd_count}</h3>
<p>{rd_count}</p>
{plot_html}
{js_console}
</body>
</html>
"""

# Save HTML
with open("employee_department_histogram.html", "w") as f:
    f.write(html_content)

print("HTML file generated. Open in browser and check console for R&D count.")
