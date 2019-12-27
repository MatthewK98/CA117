class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def midpoint(self, other):
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)


class Circle:

    def __init__(self, centre=None, radius=0):
        self.centre = centre if centre else Point()
        self.radius = radius

    def __str__(self):
        return "Centre: {}\nRadius: {}".format(self.centre, self.radius)

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius, centre=self.centre.midpoint(other.centre))

def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)

if __name__ == '__main__':
    main()
