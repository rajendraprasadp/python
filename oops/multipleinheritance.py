class Employee:
    company = "google"

    def showDetails(self):
        print("employee")


class Freelancer:
    name = "raj"
    company = "aamazon"


class Programmer(Employee, Freelancer):
    language = "python"

    def getLanguage(self):
        print(f"the language is {self.language} ")

    def showDetails(self):
        print("programmer")
        super().showDetails()


e = Employee()
p = Programmer()
f = Freelancer()
p.showDetails()
