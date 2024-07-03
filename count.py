fp = open("count.txt", "r")
words = []
lines = 0
charcount = 0

for line in fp:
    words.extend(line.split())
    lines += 1
    charcount += len(line)

fp.close()

print(len(words))
print(lines)
print(charcount)