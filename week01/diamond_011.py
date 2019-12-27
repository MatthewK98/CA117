import sys
amount_astericks = int(sys.argv[1])
for i in range(1,amount_astericks + 1):#Columns
	for j in range(0,amount_astericks - i):#Rows
		print(" ",end="")
	print(("* " * i).rstrip())
#print(("* " * amount_astericks).rstrip())

for i in range(amount_astericks- 1,0,-1):#Colums
    for j in range(1,amount_astericks - i):#Rows
        print(" ",end= "")
    print(" *" * i)