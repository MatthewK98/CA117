import sys
line = sys.stdin
goodies ={}
skipped = []
for word in line:
    word = word.strip().replace(","," ").split(":")
    name = word[0]
    numbers = word[1]
    total = 0
    good = True
    for i in (numbers.split()):
        if i.isnumeric():
            total += int(i)
        else:
            good = False
            skipped.append(name)
            break
    if good == True:
        goodies[name] = total
lowest = sorted((k,v) for (v,k) in goodies.items(),)[-1::-1]
for row in range(len(lowest)):
    print("{} : {}".format(lowest[row][1],lowest[row][0]))
print("Skipped:")
for row in skipped:
    print(row)