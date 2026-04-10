def passwordprotect(func):
    def wrapper():
        password=input("Enter the password: ")
        if password=="secret":
            func()
        else:
            print("wrong password")
    return wrapper
@passwordprotect
def mysecret():
    print("I'm starting PHD in summer")
print(mysecret())
   