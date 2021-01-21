class Employee:

    num_of_emps = 0
    raise_amt = 1.25

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.25)

    # def apply_raise(self):
    #     self.pay = int(self.pay * Employee.raise_amount)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.55

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(">>> ", emp.fullname())

emp_1 = Employee("Dave", "Black", 25000)
emp_2 = Employee("Ion", "Popescu", 35000)

# print(emp_1)
# print(emp_2)

# emp_1.first = "Dave"
# emp_1.last = "Black"
# emp_1.email = "Dave.Black@company.com"
# emp_1.pay = 25000

# emp_2.first = "Mike"
# emp_2.last = "Johnson"
# emp_2.email = "Mike.Johnson@company.com"
# emp_2.pay = 35000

# print(emp_1.email)
# print(emp_2.email)

#print("{} {}".format(emp_1.first, emp_1.last))

# print(emp_2.fullname())
# print(Employee.fullname(emp_1))

## Apply raise to employee
# print(emp_1.pay)
# Employee.apply_raise(emp_1)
# print(emp_1.pay)

# emp_1.raise_amount = 1.50

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
#print(Employee.__dict__)

#print(Employee.num_of_emps)

# Employee.set_raise_amt(1.37)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)

#emp_str_3 = "Mary-Jane-50000"

#first, last, pay = emp_str_3.split("-")
#emp_3 = Employee(first, last, int(pay))

# emp_3 = Employee.from_string(emp_str_3)

# print(emp_3.pay)

# emp_3.apply_raise()

# print(emp_3.pay)

# import datetime

# my_date = datetime.date(2021, 6, 22)

# print(Employee.is_workday(my_date))

dev_1 = Developer("John", "Doe", 55000, "Go")
dev_2 = Developer("Jane", "Foe", 75000, "Python")

#print(help(Developer))

# print(dev_2.email)
# print(dev_2.prog_lang)

# print(dev_2.pay)
# Employee.apply_raise(dev_2)
# print(dev_2.pay)

mgr_1 = Manager("Jake", "Green", 100000, [emp_1, emp_2])

#print(mgr_1.email)

#mgr_1.print_emps()

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(emp_2)

# mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Manager))
