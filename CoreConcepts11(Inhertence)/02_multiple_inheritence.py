class Employee:
    company = "ITC"
    name = "from employee class"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "from coder class"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")



class Programmer(Employee, Coder):
    company = "from programmer class"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()