# salaryAi = salary * increment ;salaryAf = salaryAfterIncrement

class Employee:
    salary = 1000
    increment = 2

    @property
    def salaryAi(self):
        return self.salary*self.increment

    @salaryAi.setter
    def salaryAi(self, sal):
        self.increment = sal/self.salary


e = Employee()
print(e.salaryAi)
print(e.increment)
e.salaryAi = 20000
print(e.increment)
print(e.salaryAi)
