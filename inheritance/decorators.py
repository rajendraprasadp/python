class Employee:
    company = "boeing"
    salary = 5000
    salaryBonus = 400
    # totalSalary=5400

# property decorators
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

# SETTERS AND GETTERS
# the method name with property decorator is called GETTER METHOD
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
print(e.totalSalary)


e.totalSalary = 6000

print(e.salary)
print(e.salaryBonus)
