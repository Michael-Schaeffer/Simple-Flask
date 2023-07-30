import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxx"
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE users")

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
