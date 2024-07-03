import marshal

fp = open("marsh1.txt","rb")
data = marshal.load(fp)
exec(data)
