import sys
line = sys.stdin
for word in line:
    word = word.strip()
    for i in word:
        if i in ":,@?-.\n":
            word = word.replace(i, " ")
        word = word.lower()
    word = word.split()
    for i in word:
        if len(i) > 3 and i.isnumeric() is False:
            dict[i] = dict.get(i, 0) + 1
low = sorted((v, k) for (k, v) in dict.items())
longestkey = 0
longestvalue = 0

for i in range((len(low))):
    if low[i][1] >= 3:
        if len(low[i][0]) > longestkey:
            longestkey = len(low[i][0])
        if len(str(low[i][1])) > longestvalue:
            longestvalue = len(str(low[i][1]))
for i in range(len(low)):
    if low[i][1] >= 3:
        print("{:>{}} : {:>{}}".format(low[i][0]))
