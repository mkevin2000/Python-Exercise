def sayHiFirst(func):
    def wrapper():
        print("Starting function...")
        func()
    return wrapper
@sayHiFirst
def sayhi():
    print("Kevin")
sayhi()