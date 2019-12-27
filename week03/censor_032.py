import sys
line = sys.stdin
file = sys.argv[1]
with open(file, "r") as f:
	censored_words = [line.rstrip() for line in f]
	for i in line:
		i = i.strip()
		i = i.split()
		output = ""
		for q in i:
			for a in censored_words:
				if a in q:
					output += q.replace(a, "@" * len(a)) + " "
				else:
					output += q + " "
					break
		print(output, end = "")
