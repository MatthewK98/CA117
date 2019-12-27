from math import sqrt
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, point2):
        x = self.x - point2.x
        y = self.y - point2.y
        z = sqrt(x ** 2 + y ** 2)
        return z

    def __str__(self):
        return "({}, {})".format(float(self.x), float(self.y))

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)

    def midpoint(self):
        return Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)


class Circle:
    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def overlaps(self, c2):
        return self.radius + c2.radius > self.centre.distance(c2.centre)  # Why dont we use Point() ?

def main():
    p1 = Point(2)
    p2 = Point(6, 8)
    p3 = Point(3, 4)

    s1 = Segment(Point(), p3)
    s2 = Segment(p1, p2)
    p4 = s1.midpoint()

    c1 = Circle(p1, 5)
    c2 = Circle(p2, 2)
    c3 = Circle(p1, 2)

    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(s1.length())
    print(c1.overlaps(c2))
    print(c2.overlaps(c1))
    print(c1.overlaps(c3))
    print(c3.overlaps(c1))
    print(c3.overlaps(c2))

if __name__ == '__main__':
    main()
