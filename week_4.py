def convert(s):
    ch = list(s)
    for i in range(len(s)):
        if (i == 0 and ch[i] != ' ') or (ch[i] != ' ' and ch[i - 1] == ' '):
            if ch[i].islower():
                ch[i] = chr(ord(ch[i]) - ord('a') + ord('A'))
        elif ch[i].isupper():
            ch[i] = chr(ord(ch[i]) + ord('a') - ord('A'))
    st = "".join(ch)
    return st

strout = "hi abc cdef"
print(convert(strout))
