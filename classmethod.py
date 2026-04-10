class Person:
    count= 0 
    def __init__(self, name):
        self.name = name
        Person.count+=1
    @classmethod
    def reset_count(cls):
        cls.count=0
    @classmethod
    def get_count(cls):
        return cls.count    
Alice = Person("Alice")
Bob = Person("Bob")
print(Person.get_count())
Person.reset_count()
print(Person.get_count())

