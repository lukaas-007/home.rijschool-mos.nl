import mysql.connector

mydb = mysql.connector.connect(
  host="phpmyadmin.lucasvanbriemen.nl",
  user="LucasDatabase",
  password="LucasDatabase",
  database="rijles"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM users"
mycursor.execute(sql)

print(mycursor.rowcount, "record inserted.")