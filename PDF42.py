from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("student_report.pdf")

styles = getSampleStyleSheet()

content = []

title = Paragraph("Student Report", styles['Title'])
content.append(title)

content.append(Spacer(1, 12))

content.append(Paragraph("Name: John Doe", styles['Normal']))
content.append(Paragraph("Roll Number: 101", styles['Normal']))
content.append(Paragraph("Course: Python Programming", styles['Normal']))
content.append(Paragraph("Marks: 95", styles['Normal']))

pdf.build(content)

print("PDF generated successfully!")