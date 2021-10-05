class Employee:
    company = "caterpillar"
    salary = 220
    location = "pune"

    # def changeSalary(self, sal):
    #     self.__class__salary = sal  # __class__ method is known as Dunder Method

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)
