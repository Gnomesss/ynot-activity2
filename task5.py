class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name} received a raise of ₱{amount:.2f}.")

    def display_employee(self):
        print(f"Name: {self.name}\nPosition: {self.position}\nSalary: ₱{self.salary:.2f}\n")


employee = Employee("Lenard Balintong", "Mechanical Engineer", 696969)

print("Before Raise:")
employee.display_employee()

employee.give_raise(6969)

print("After Raise:")
employee.display_employee()
