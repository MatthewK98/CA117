import sys
text = sys.stdin
all_text = [a.strip() for a in text]
print("Words with q but no u:", [a for a in all_text if a.lower().count("qu") < a.lower().count("q")])
