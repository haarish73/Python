import marshal

src = """
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial=:", fact)
"""
code = compile(src,"src","exec")
fp = open("marshal_2.txt","wb")
marshal.dump(code,fp)
fp.close()