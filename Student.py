class Student:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print("Hello")
S1 = Student("Bro")
S1.hi()
print(S1.name)