class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age}")

# inheritance
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")
        print(f"My id is {self.student_id}")
s1 = Student("Alice", 20, "123")
s1.greet()
s1.study()