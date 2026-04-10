class Point:
    def __init__(self, X, Y):
        self.x= X
        self.y= Y
    def distanceFromOrigin(self):
        return(self.x**2 + self.y**2)**0.5
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy    
p= Point(3, 4)        
assert p.y==4
assert p.x==3
assert p.distancefromorigin()==5.0
p.move(1, 2)
assert p.y==6
assert p.x==4
