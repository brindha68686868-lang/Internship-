import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

cursor = conn.cursor()

sql = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
values = (101, "Brindha", 19)

cursor.execute(sql, values)
conn.commit()

print(cursor.rowcount, "record inserted.")

conn.close()