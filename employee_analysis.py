import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Generate dataset
np.random.seed(42)
departments = ['Finance', 'Operations', 'HR', 'R&D', 'Marketing', 'Sales']
regions = ['North America', 'Europe', 'Asia Pacific', 'Middle East', 'Africa', 'South America']

n = 100
data = {
    'employee_id': [f'EMP{str(i+1).zfill(3)}' for i in range(n)],
    'department': np.random.choice(departments, size=n, p=[0.15,0.25,0.15,0.15,0.15,0.15]),
    'region': np.random.choice(regions, size=n),
    'performance_score': np.round(np.random.normal(loc=75, scale=12, size=n), 2),
    'years_experience': np.random.randint(0, 31, size=n),
    'satisfaction_rating': np.round(np.random.uniform(2.5, 5.0, size=n), 1)
}
df = pd.DataFrame(data)

# Sample top rows (your given ones)
sample_top5 = pd.DataFrame([
    ['EMP001','Finance','Middle East',85.16,11,4.9],
    ['EMP002','Operations','Africa',93.17,1,4.2],
    ['EMP003','HR','Europe',83.25,9,4.0],
    ['EMP004','Finance','Asia Pacific',62.29,10,3.2],
    ['EMP005','Operations','North America',82.58,12,4.8],
], columns=df.columns)
df.iloc[:5] = sample_top5.values

# Frequency of R&D
rd_count = (df['department'] == 'R&D').sum()
print("Frequency count for 'R&D':", rd_count)

# Plot
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

# HTML
html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Employee Analysis</title></head>
<body>
<h1>Employee Performance Analysis</h1>
<p>Verification email: <b>24f2007963@ds.study.iitm.ac.in</b></p>
<p>R&D count: {rd_count}</p>
<img src="data:image/png;base64,{img_b64}" />
</body>
</html>
"""
open("employee_analysis.html","w",encoding="utf-8").write(html)
