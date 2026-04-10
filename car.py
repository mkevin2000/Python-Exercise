class Car:
    wheels = 4   # class variable

    def __init__(self, name):
        self.name = name
c1 = Car("Toyota")
c2 = Car("BMW")

print(c1.wheels)
print(c2.wheels)

Car.wheels = 6

print(c1.wheels)
print(c2.wheels)

c1.wheels = 3

print(c1.wheels)
print(c2.wheels)        