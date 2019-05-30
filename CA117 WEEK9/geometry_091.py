from math import sqrt
class Point:
    def __init__(self, x=0.00, y=0.00):
        self.x = x
        self.y = y
        
    def distance(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        z = sqrt(x ** 2 + y ** 2)
        return z

class Shape:
    def __init__(self, points=[]):
        self.points = points
        
    def sides(self):
        output = []
        for i in range(len(self.points) - 1):
            output.append(self.points[i].distance(self.points[i + 1]))
        output.append(self.points[0].distance(self.points[-1]))
        return output
        
    def perimeter(self):
        return sum(self.sides())
        
class Triangle(Shape):
    def area(self):
        s = sum(self.sides()) / 2
        return s
        

def main():

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()