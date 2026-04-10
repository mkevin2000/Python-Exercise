class Person:
    def __init__(self, name, age):
        self.first_name = name.split()[0]
        self.last_name = name.split()[-1]
        self.age = age
    def GetGivenName(self):
        return self.first_name
    def GetFamilyName(self):
        return self.last_name
    def IsChild(self):
        return self.age < 18
    
p1= Person("Steve Jobs", 56)
print(p1.GetGivenName())
print(p1.GetFamilyName())
print(p1.IsChild())