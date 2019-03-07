import sys
file = sys.argv[1]
with open(file, "r") as f:
  q = []
  for line in f:
    words = line.split()
    number = words[0]
    q += (number,)
  highest = max(q)

with open(file, "r") as f:
  for i in f:
    i = i.split()
    number = str(i[0])
    if number == str(highest):
      name = " ".join(i[1:])
      break
    else:
      pass
print("Best student:", name)
print("Best mark:", highest)
