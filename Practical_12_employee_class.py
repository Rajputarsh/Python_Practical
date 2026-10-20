class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_count(cls):
        print("Total employees:", cls.count)


e1 = Employee("Amit", 50000)
e2 = Employee("Riya", 60000)
e3 = Employee("Neha", 55000)

e1.display()
e2.display()
e3.display()
Employee.display_count()
