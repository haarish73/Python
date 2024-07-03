import dbm

db = dbm.open("dbm2.db", 'r')
for k, v in db.items():
    print(k, v)
