class Student:
    def __init__(s, name, age, course):
        s.name = name
        s.age = age
        s.course = course

    def display_info(s):
        print(f"Name: {s.name}")
        print(f"Age: {s.age}")
        print(f"Course: {s.course}")

    def introduce(s):
        print(f"Hi, my name is {s.name}. {s.age} years old, and I am studying {s.course}.")    
        

student1 = Student("Hance Hitutuane", "19", "DIP-IT")
print("\n")
student1.introduce()

student2 = Student("Lenard Balintong", "23", "DIP-HM")
print("\n")
student2.introduce()

student3 = Student("Jerson Panisales", "20", "DIP-TM")
print("\n")
student3.introduce()
