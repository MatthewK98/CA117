import sys
from math import pi
print ("Radius (m)      Area (m^2)    Volume (m^3)\n"
"----------      ----------    ------------")
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

def Area(x):
	return 4 * pi * x ** 2
def Volume(x):
	return 4 / 3 * pi * x ** 3
while x <= z:
	one = float(x)
	two = Area(x)
	three = Volume(x)
	print("{:>10.1f}".format(one),"{:>15.2f}".format(two),"{:>15.2f}".format(three))
	x += y