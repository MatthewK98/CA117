import sys
line = sys.stdin
for a in line:
	a = a.strip()
	first = a[0].upper()
	last = a[-1].upper()
	middle = a[1:-1]
	if len(a) > 1:
		print(first + middle + last)