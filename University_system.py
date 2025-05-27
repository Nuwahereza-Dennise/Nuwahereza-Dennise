#University System: Display Information
#Classes: Person(parent) and Student,Lecturer, Staff(subclasses)
class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        
    def display_information(self):
        print(f"Name: {self.name}. Age: {self.age}. Phone_number: {self.phone_number}")

class Student(Person):
    def __init__(self, name, age, phone_number, student_number, course):
        super().__init__(name, age, phone_number)
        self.student_number = student_number
        self.course = course
    def display_information(self):
        super().display_information()
        print(f"Student Number: {self.student_number}. Course: {self.course}")
    
class Lecturer(Person):
    def __init__(self, name, age, phone_number, lecturer_number, department):
           super().__init__(name, age, phone_number) 
           self.lecturer_number = lecturer_number
           self.department = department
    def display_information(self):
        super().display_information()
        print(f"Lecturer Number: {self.lecturer_number}. Department: {self.department}")
        
class Staff(Person):
    def __init__(self, name, age, phone_number, staff_number, duty):
         super().__init__(name, age, phone_number)
         self.staff_number = staff_number
         self.duty = duty
    def display_information(self):
        super().display_information()
        print(f"Staff Number: {self.staff_number}. Duty: {self.duty}")
        
student1 = Student("Dennise", 22, "0788904942", "S111", "Software Engineering")
lecturer1 = Lecturer("Damalie", 26, "0772739619", "L111", "Networks")
staff1 = Staff("Derrick", 32, "0772424355", "SN111", "Supervision")

student1.display_information()
lecturer1.display_information()
staff1.display_information()
