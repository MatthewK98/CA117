import sys
line = sys.stdin
add = 0
for a in line:
	a = a.strip()
	a = a.split()
	add += len(a)
print(add)