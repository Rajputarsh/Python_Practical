import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point2D(3, 4)
p2 = Point2D(6, 8)
print("p1 =", p1)
print("p2 =", p2)
print("Distance of p1 from origin:", p1.distance_from_origin())
print("Distance between p1 and p2:", p1.distance_to(p2))
