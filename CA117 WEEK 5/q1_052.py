import sys
word = sys.argv[1]
number = int(sys.argv[2])
i = 0
n = len(word)

while i < number:
    word = word[-1] + word[:-1]
    i = i + 1
print(word)