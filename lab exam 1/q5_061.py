import sys
line = sys.stdin
golf = {}
for word in line:
    word = word.strip().split()
    numbers = word[-3::1]
    name = " ".join(word[:-3])
    total = 0
    for char in numbers:
        total += int(char)
    golf[name] = total
low = sorted((k, v) for (v, k) in golf.items())
longest = 0
for i in golf:
    if len(i) > longest:
        longest = 0
        longest = len(i)
longestname = longest
highest = 0
for i in golf.values():
    if len(str(i)) > highest:
        highest = 0
        highest = len(str(i))
longestscore = highest


for row in low:
     print("{:>{width}}: {:>{length}}".format(row[1], row[0], width=longestname, length=longestscore))
