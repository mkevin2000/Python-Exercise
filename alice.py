class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __lt__(self, other):
        return self.marks < other.marks
    def __str__(self):
        return f"{self.name} has {self.marks} marks."
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "F"
    def is_passing(self):
        return self.marks >= 50
    def is_failing(self):
        return self.marks < 50
        
s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
s3 = Student("Charlie", 80)
s4 = Student("David", 95)
students = [s1, s2, s3, s4]
print("Students sorted by marks:")
for student in sorted(students):
    print(student)
print("\nGrades:")
for student in students:
    print(f"{student.name} has grade {student.grade()}.")
print("\nPassing students:")        
for student in students:
    if student.is_passing():
        print(f"{student.name} is passing.")