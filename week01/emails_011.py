import sys
line = sys.stdin
for a in line:
	a = a.strip()
	a = a.replace("."," ")
	for i in a:
	    if i.isdigit():
	        a = a.replace(i," ")
	a = a.split()
	firstname = a[0].capitalize()
	lastname = a[1].capitalize()
	fullname = firstname + " " + lastname
	print(fullname)