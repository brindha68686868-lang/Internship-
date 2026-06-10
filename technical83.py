from datetime import datetime

project_name = "Student Management System"
version = "1.0"

documentation = f"""
PROJECT DOCUMENTATION
=====================

Project Name : {project_name}
Version      : {version}
Generated On : {datetime.now()}

DESCRIPTION
-----------
This project manages student records.

FEATURES
--------
1. Add Student
2. View Student
3. Update Student
4. Delete Student

TECHNOLOGIES
------------
- Python
- SQLite

AUTHOR
------
Brindha
"""

with open("project_documentation.txt", "w") as file:
    file.write(documentation)

print("Documentation generated successfully!")