import sys
line = sys.stdin
q = []
vowels = {}
for word in line:
    word = word.strip().split()
    x = [i for i in word]
    for i in x:
        q += i.lower()
vList = ["a", "e", "i", "o", "u"]

for v in vList:
    vowels[v] = q.count(v)

vowels = [(v, k) for k, v in vowels.items()]
vowels.sort(reverse=True)
vowels_counts = [i[0] for i in vowels]
max_width = max([len(str(count)) for count in vowels_counts])
for v, k in vowels:
    print ("{} : {:>{}}".format(k, v, max_width))
