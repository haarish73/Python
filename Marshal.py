import marshal

src = """
a=10
b =20
print("multiplication=",a*b)
"""
code = compile(src,"src","exec")
fp = open("marsh1.txt","wb")
marshal.dump(code,fp)
fp.close()