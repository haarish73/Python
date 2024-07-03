import sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()

# CREATING TABLE INTO SQL :-

# cur.execute(
#     "CREATE TABLE IF NOT EXISTS student ("
#     "name CHAR(20), "
#     "email CHAR(30), "
#     "password CHAR(10)"
#     ")"
# )

# INSERTING INTO TABLE :-


cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("harish", "harish@gmail.com", "12345"))
cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("masthan", "masthan@gmail.com", "23456"))
cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("vishnu", "vishnu@gmail.com", "34567"))

# cur.execute('INSERT INTO student values("harish","khan@gmail.com","12345")')

# DELETE FROM TBALE

# cur.execute('delete from student where name="harish"')

#UPDATE TABLE

cur.execute('update student set name ="vishnu" where password="45678"')

cur.execute("SELECT * FROM STUDENT")


tables = cur.fetchall()
print(tables)