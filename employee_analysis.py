import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Load real dataset (must be in same folder as this script)
df = pd.read_csv("employee_data.csv")

# Calculate R&D frequency
rd_count = (df['department'] == 'R&D').sum()
print("Frequency count for 'R&D' department:", rd_count)

# Create department distribution plot
dept_counts = df['department'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(dept_counts.index, dept_counts.values)
ax.set_title('Department Distribution')
ax.set_xlabel('Department')
ax.set_ylabel('Count')
for i,v in enumerate(dept_counts.values):
    ax.text(i, v+0.5, str(v), ha='center')
buf = BytesIO()
fig.savefig(buf, format='png')
plt.close(fig)
img_b64 = base64.b64encode(buf.getvalue()).decode()

# Write HTML file
html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Employee Analysis</title></head>
<body>
<h1>Employee Performance Analysis</h1>
<p>Verification email: <b>24f2007963@ds.study.iitm.ac.in</b></p>
<p>Frequency count for "R&D" department: <b>{rd_count}</b></p>
<img src="data:image/png;base64,{img_b64}" />
</body>
</html>
"""
open("employee_analysis.html","w",encoding="utf-8").write(html)
