import sys
line = sys.stdin
for a in line:
	a = a.strip()
	middle = len(a) // 2
	if len(a) % 2 == 0:
	    print("No middle character!")
	else:
	    print(a[middle])