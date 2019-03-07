import sys

# from math import pi
# digit = int(sys.argv[1])
# print("{:.{digit}f}".format(pi, digit=digit))
from math import pi
digit = int(sys.argv[1])
print("{:.{w}f}".format(pi, w=digit))


#print("{:.{}f}".format(pi, digit))