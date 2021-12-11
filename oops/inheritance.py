class Employee:
    company = "google"

    def showDetails(self):
        print("employee")


class Programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"the language is {self.language} ")

    @staticmethod
    def showDetails():
        print("programmer")


w = Employee()
p = Programmer()
print(p.company)
print(p.language)
p.showDetails()
