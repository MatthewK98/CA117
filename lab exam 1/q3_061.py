import sys
import string
line = sys.stdin
special = string.punctuation
for word in line:
    word = word.strip()
    number = 0
    lower = 0
    upper = 0
    special = 0
    for char in word:
        if char.isnumeric():
            number = 1
        elif char.islower():
            lower = 1
        elif char.isupper():
            upper = 1
        else:
            special = 1
    print(number + lower + upper + special)
