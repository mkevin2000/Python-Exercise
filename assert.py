p = (6, 8)
assert p.distanceFromOrigin() == 10.0
p.move(-1, -3)
assert p.x == 5
assert p.y == 5
print("All tests passed!")