import sys
word = sys.argv[1]
word_list = list(word)
for i in range(1, len(word_list,), 2):
    word_list[i - 1], word_list[i] = word_list[i], word_list[i - 1]
print("".join(word_list))
