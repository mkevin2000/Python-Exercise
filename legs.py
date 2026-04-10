class Animal:
    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return f"Animal with {self.arms} arms and {self.legs} legs"

spider = Animal(4,4)

print(spider)