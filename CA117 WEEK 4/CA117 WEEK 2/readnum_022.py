import sys
line = sys.stdin
for i in line:
    i = i.strip()
    if i.isdigit() is False:
        print(i, "is not a number")
    else:
        print("Thank you for", i)
        break
