import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")

print(myclient.list_database_names())

mydb = myclient["cmrec1"]

mydblist = myclient.list_database_names()

"""if "cmrec" in mydblist:
    print("Database exists")
else:
    print("Database doesn't exist")"""

mydb = myclient["cmrec"]
# mycol = mydb["cse"]
#
# mylist = mydb.list_collection_names()
# if "cse" in mylist:
#     print("Collection exists")
# else:
#     print("Collection does not exist")
mycol = mydb["cse"]
mydoc = {"name": "John Doe", "age": 25, "major": "Computer Science"}
mycol.insert_one(mydoc)
x = mycol.inser_many


