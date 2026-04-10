class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_y_to_x(self):
        self.y = self.x

p1 = Point(3, 9)
p2 = Point(5, 7)
p3 = Point(2, 4)

print(p1.x, p1.y)

p2.move_y_to_x()

print(p2.x, p2.y)
print(p3.x, p3.y)
    
    