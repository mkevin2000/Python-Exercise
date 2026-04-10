import math
class Point:
    def __init__(self, initX, initY):
        self.X=initX
        self.Y=initY
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def distancefromOrigin(self):
        return math.sqrt((self.X**2)+(self.Y**2))
    def distance(self, point2):
        xdiff=point2.getX()-self.X
        ydiff=point2.getY()-self.Y
        dist=math.sqrt((xdiff**2)+(ydiff**2))
        return dist 