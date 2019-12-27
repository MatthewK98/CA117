import sys
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.split()
	first = a[0].upper() #TAC
	second = a[1].upper() #ACT
	first =  ''.join(sorted(first)) #ACT
	second = ''.join(sorted(second)) #ACT

	if first in second:
 	    print(True)
	else:
 	    print(False)