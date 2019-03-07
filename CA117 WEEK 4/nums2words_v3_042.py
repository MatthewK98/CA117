import sys
line = sys.stdin
file = sys.argv[1]
with open(file, "r") as f:
    q = []
    for i in f:
        i = i.strip()
        i = i.split()
        english = i[0]
        irish = i[1]
        q += (irish,)
irish_numbers = q

for i in line:
  i = i.strip()
  i = i.split()
  line = ""
  for a in i:
    a = int(a)
    line += irish_numbers[a] + " "
  print(line.strip())
