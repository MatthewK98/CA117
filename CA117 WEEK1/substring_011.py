import sys
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.split()
	first = a[0]
	second = a[1]
	if first.upper() in second.upper():
		print(True)
	else:
		print(False)