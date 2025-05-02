import pandas as pd
from fpdf import FPDF
import os
import matplotlib.pyplot as plt

# Define the directory path
directory = r"f:\internship task"
csv_path = os.path.join(directory, "data.csv")
pdf_path = os.path.join(directory, "Student_Report.pdf")

# Read and analyze data
data = pd.read_csv(csv_path)
average_marks = data["Marks"].mean()
highest = data.loc[data["Marks"].idxmax()]
lowest = data.loc[data["Marks"].idxmin()]
# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(data['Name'], data['Marks'], color='skyblue')
plt.title('Student Performance Chart')
plt.xlabel('Student Names')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(directory, 'performance_chart.png'))
plt.close()

# Create PDF 
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 24)
pdf.cell(0, 20, "Student Performance Report", ln=True, align='C')
pdf.ln(10)

# Add performance chart
pdf.image(os.path.join(directory, 'performance_chart.png'), x=10, w=190)
pdf.ln(10)

# Student data table
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Student Marks Details", ln=True)
pdf.ln(5)

pdf.set_font("Arial", "", 12)
for i, row in data.iterrows():
    pdf.cell(0, 8, f"{row['Name']} - {row['Marks']} marks", ln=True)
pdf.ln(10)

# Analysis 
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "Analysis Summary", ln=True)
pdf.ln(5)

pdf.set_font("Arial", "", 12)
pdf.cell(0, 8, f"Class Average: {average_marks:.2f} marks", ln=True)
pdf.cell(0, 8, f"Highest Score: {highest['Name']} ({highest['Marks']} marks)", ln=True)
pdf.cell(0, 8, f"Lowest Score: {lowest['Name']} ({lowest['Marks']} marks)", ln=True)

# Save PDF
pdf.output(pdf_path)
print(f"PDF report generated successfully at {pdf_path}!")

# Clean up temporary files
os.remove(os.path.join(directory, 'performance_chart.png'))