import sys
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.split()
	first = a[0]
	second = a[1]
	i = 0
	add = 0
	while i < len(first):
		converter = int(first[-1 - i]) * int(second) ** i
		add += converter
		i = i + 1
	print(add)