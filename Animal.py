class Animal:
    """A class representing an animal with arms and legs."""    
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs  
    def limbs(self):
        return self.arms + self.legs
print(Animal(2, 2).limbs())
help(Animal)
Animal?