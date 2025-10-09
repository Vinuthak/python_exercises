class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name = {self.name}, age = {self.age})"
s1 = Student("Alice", 20)
print(s1) #prints the details elsee without the string method print(s) gives only memory of the object