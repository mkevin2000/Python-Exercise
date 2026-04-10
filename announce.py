def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def say_hi(name):
    print(f"Hi, {name}!")
@repeat(2)
def announce(message):
    print(f" Announcement: {message}")
say_hi("Alice")                
announce("This message will be announced twice.")