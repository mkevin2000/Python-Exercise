def add_five(x):
    return x+5
def multiply_by_two(x):
    return x*2
def compose(f1,f2):
    return lambda x: f1(f2(x))
myfunc= compose(add_five, multiply_by_two)
print(myfunc(5))