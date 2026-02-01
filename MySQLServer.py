import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="alx_book_store"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

print(mydb.get_server_info())