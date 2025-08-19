import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("employee_data.csv")

# Frequency count for R&D department
rd_count = (df['department'] == 'R&D').sum()

# Plot histogram of department distribution
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='department')
plt.xticks(rotation=45)
plt.title("Department Distribution")

# Save the plot as an image
plt.savefig("department_distribution.png")

# Create HTML file
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Employee Analysis</title>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <p>Frequency count for 'R&D' department: {rd_count}</p>
    <img src="department_distribution.png" alt="Department Distribution Histogram">
    <script>
        console.log("Frequency count for 'R&D' department: {rd_count}");
        console.log(8);
    </script>
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print(f"Frequency count for 'R&D' department: {rd_count}")
