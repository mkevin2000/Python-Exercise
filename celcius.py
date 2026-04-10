def addLogging(func): # The argument, func is a function

    def wrapper(x): # x is the argument that we're going to pass to func
        print(f"About to call the function with argument {x}")
        result = func(x) # actually call our function and store the result
        print(f"Done with the function with argument {x}. Result: {result}")
        return result # return whatever our function returned

    return wrapper # return our new function

def double(x):
    print("Inside double")
    return x * 2

logged_double = addLogging(double)

double_3 = logged_double(3)
print(f"logged_double(3) returned {double_3}")

print("-"*20)

logged_add_one = addLogging(lambda x: x + 1)
ten_plus_1 = logged_add_one(10)
print(f"logged_add_one(10) returned {ten_plus_1}")
