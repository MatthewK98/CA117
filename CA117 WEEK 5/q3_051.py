import sys
line = sys.stdin
for a in line:
    a = a.strip()
    fullword = ""
    for i in a:
        if i.isupper():
            fullword += i
        elif i.isupper() is False:
            fullword += i.replace(i, " ")
    fullword = fullword.split()
    print(sorted([i for i in fullword], key=len)[-1])
