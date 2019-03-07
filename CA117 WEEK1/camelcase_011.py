import sys
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.split()
	i = 0
	full_line = ""
	while i < len(a):
		full_line += a[i].capitalize() + " "
		i = i + 1
	print(full_line.strip())