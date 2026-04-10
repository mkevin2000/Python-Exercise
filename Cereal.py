class Cereal:
    def __init__(self, name, brand, fiber):
        self.name= name
        self.brand= brand
        self.fiber= fiber
    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber."  
c1= Cereal("cornflakes", "Kellogg's", 1)
c2= Cereal("Honey Nut Cheerios", "General Mills", 3)
print(c1)
print(c2)


