class Point:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5
    def __str__(self):
        return f"point with x coordinate {self.x} and y coordinate {self.y}"
    def halfway(self, target):
        mx= (self.x + target.getx())/2
        my= (self.y + target.gety())/2
        return Point(mx, my)
p1= Point(2, 6)
p2= Point(8, 10)
mid=p1.halfway(p2)
print(p1)
print(p2)
print(mid)
print(mid.getx())
print(mid.gety())