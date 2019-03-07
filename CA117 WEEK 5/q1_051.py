import sys
s = sys.argv[1]
sl = list(s)
for i in range(1, len(s), 2):
    sl[i-1], sl[i] = sl[i], sl[i-1]
print("".join(sl))