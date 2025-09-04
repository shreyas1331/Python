class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        return("Good morning")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)

rohan = Employee("Shreyas",439595,"react")
print(rohan.name,rohan.salary,rohan.language)
print(rohan.greet())
rohan.greet()

# Function Call	Console Output
'''rohan.getInfo()	The language is react. The salary is 439595
print(rohan.getInfo())	The language is react. The salary is 439595 + None
The difference: None will only appear if you print the return value of the function, not if the function itself prints its own output'''