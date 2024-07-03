import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123"
)


mycurs = mydb.cursor()


# mycurs.execute("SHOW DATABASES")


mycurs.execute(
    "CREATE TABLE IF NOT EXISTS users ("
    "name CHAR(20), "
    "email CHAR(30), "
    "password CHAR(10)"
    ")"
)

result = mycurs.execute("select * from user")
result = mycurs.fetchall()
for db in result:
    print(db)