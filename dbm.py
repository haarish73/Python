import dbm

db = dbm.open("dbm1.db","n")
db['one'] = '1'
db['Two'] = '2'
db['three'] = '3'
with dbm.open("dbm1.db") as db: