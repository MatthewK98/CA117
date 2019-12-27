import sys
file = sys.argv[1]
with open(file, "r") as f:
  q = []
  for i in f:
    i = i.split()
    number = i[0]
    q += (number,)
highest = max(q)

with open(file, "r") as f:
    names = ""
    for i in f:
       i = i.split()
       number = i[0]
       if highest == number:
         if names != "":
          names += ", "
         names += " ".join(i[1:])

print("Best student(s):", names)
print("Best mark:", highest)


# Best Students : Michael Murphy, John Kelly
# Best mark: 89
