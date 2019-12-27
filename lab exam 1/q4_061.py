import sys
line = sys.stdin
checker = []
for word in line:
    word = word.strip()
    j = -1
    for i in range(len(word)):
        each_word = "".join(sorted(word[i:j]))
        checker += (each_word,)
        j = j - 1
        if word[i:] in checker:
            print(word[i:])
            break
