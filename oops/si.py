# INHERITANCE: its a way of creating new class from an existing class

class Employee:
    company = "google"

    def showDetails(self):
        print("employee")


class Programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"the language is {self.language} ")

    def showDetails(self):
        print("programmer")


w = Employee()
w.showDetails()
p = Programmer()
print(p.company)
print(p.language)
