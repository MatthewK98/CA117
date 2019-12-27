import sys
line = []
for i in sys.stdin:
    line.append(i)
def Position(a):
    return int(a[0:2])
def Club(a):
    a = a.strip()
    a = a.split()
    a = " ".join(a[1:-8])
    return (a)

def longestClub(a):
  highest = 0
  for i in a:
    if len(Club(i)) > highest:
      highest = 0
      highest += len(Club(i))
  return(highest)
longestName = longestClub(line)
print("POS" + " CLUB" + " " * (longestName - 2) + "P   W   D   L  GF  GA  GD PTS")
for a in line:
    a = a.strip()
    Details = a.split()
    print("{:>3}".format(Position(a)) + " " + Club(a) + (longestName - len(Club(a))) * " " + " " + Details[-8] + "{:>4}".format(Details[-7]) + "{:>4}".format(Details[-6]) + "{:>4}".format(Details[-5]) + "{:>4}".format(Details[-4]) + "{:>4}".format(Details[-3]) + "{:>4}".format(Details[-2]) + "{:>4}".format(Details[-1]))
