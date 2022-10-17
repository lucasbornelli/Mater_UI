class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)

"________________________________________________________________________"

class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary

    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary / 12


emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)
"________________________________________________________________________"

# Import datetime from datetime
from datetime import datetime


class Employee:

    def __init__(self, name, hire_date, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()


# ...Other methods omitted for brevity ...

emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

"________________________________________________________________________"

