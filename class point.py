class Point:
    def __init__(self, initX, initY):
        self.X=initX
        self.Y=initY
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def distanceFromOrigin(self):
        return ((self.X**2)+(self.Y**2))**0.5
p=Point(7,6)
print(p.distanceFromOrigin())
    