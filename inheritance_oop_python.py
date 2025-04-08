class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        print(f"Name: {self.name},\nAge: {self.age},\nSalary: {self.salary}")
        
class Student(Person):
    def __init__(self,name,age,Institute,grade):
        super().__init__(name,age)
        self.institute=Institute
        self.grade=grade
    def display(self):
        print(f"Name: {self.name},\nAge: {self.age}, \nStudy Level: {self.institute},\nGrade: {self.grade} ") 
    
        

person1=Person("Umer Farooq",20)
employee1=Employee("Hassan Khan",25,120000)
student1=Student("Ali Khan",19,"University of Central Punjab","6th Semester")

print("Person Details:")
person1.display()

print("\nEmployee Details: ")
employee1.display()

print("\nStudent Details: ")
student1.display()
