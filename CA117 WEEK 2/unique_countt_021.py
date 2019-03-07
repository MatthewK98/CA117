import sys
from string import punctuation
line = sys.stdin

unique_words = set()
for a in line:
	a = a.strip()
	exclude = set(punctuation)
	a = ''.join(ch for ch in a if ch not in exclude)
	a = a.strip().upper().split()
	for a in a:
	    unique_words.add(a)
result = list(unique_words)

print(len(result))