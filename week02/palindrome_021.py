import sys
from string import punctuation
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.lower()
	a = a.replace(" ", "")
	a = [i for i in a if i.isalpha() or i.isdigit()]
	backward = a[::-1]
	if a == backward:
	    print(True)
	else:
	    print(False)