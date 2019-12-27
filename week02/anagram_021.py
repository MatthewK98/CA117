import sys
line = sys.stdin
for a in line:
    a = a.strip()
    a = a.split()
    left = a[0].lower()
    right = a[1].lower()
    left = "".join(sorted(left))
    right = "".join(sorted(right))
    if left == right:
        print(True)
    else:
        print(False)
