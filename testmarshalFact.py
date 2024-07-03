import marshal

fp = open("marshal_2.txt","rb")
data = marshal.load(fp)
exec(data)