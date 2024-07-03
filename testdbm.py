import dbm
db = dbm.open("dbm1","r")
print(list(dbm.keys()))
print(list(dbm.values()))