def subtract (x):
    return x-32
def multiply (x):
    return x*5/9
def compose (func1, func2):
    return lambda x: func1(func2(x))
fah_to_cel = compose(multiply, subtract)
print(fah_to_cel(212))
