class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self, other):
        return self.grade<other.grade
    
S = [Student("Kevin", 50), Student("Nelson", 20), Student("Tate", 100)]
for s in sorted(S):
    print(s.name, s.grade)



