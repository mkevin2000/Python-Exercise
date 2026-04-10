def add(*args):
    print(args)
    return sum(args)
print(add(1,23,45,70))

def create_user_profile(**kwargs):
    print(kwargs)
    create_user_profile = {}
    for key, value in kwargs.items():
        create_user_profile[key] = value
    return create_user_profile
print(create_user_profile(name="John", age=30, city="New York"))
