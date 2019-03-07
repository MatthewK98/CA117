import sys
line = sys.stdin
all_text = [a.strip() for a in line]
atleast_5_letters = [a for a in all_text if len(a) >= 5]
atleast_5_letters_lower = set([a.lower() for a in atleast_5_letters])
reverse_words = [a for a in atleast_5_letters if a[::-1].lower() in atleast_5_letters_lower]
print(reverse_words)