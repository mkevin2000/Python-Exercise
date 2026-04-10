class load:
    def __init__(self, Pickup, Drop, Rate, Miles):
        self.Pickup= Pickup
        self.Drop= Drop
        self.Rate= Rate
        self.Miles= Miles
    def rate_per_mile(self):
        return self.rate/self.Miles
    def __str__(self):
        return f"{self.Pickup} to {self.Drop} ${self.Rate}. {self.Miles} miles"
L= load("Dallas", "Miami", 5800, 1300)
print(L)
print(L.rate_per_mile())   