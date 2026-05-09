# SINGLE INHERITENCE

class Parent:   #Parent class
    def func1(self):
        print("this is parent function")

class Child(Parent):   #Base class
    def func2(self):
        print("this is base class")

# DRIVER CODE
obj=Child()
obj.func1()
obj.func2()

'''The Child class inherits the method func1() from Parent.
It also has its own method func2().
This shows how one class can extend another using single inheritance.'''




# MULTIPLE INHERTIENCE
# BASE CLASS 1
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
# BASE CLASS 2
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
# DERIVED CLASS
class Son(Mother,Father):
    def parents(self):
        print("Father : ",self.fathername)
        print("Mother : ",self.mothername)

# DRIVER CODE
s1=Son()
s1.fathername="ram"
s1.mothername="sita"
s1.parents()

'''Son inherits from both Mother and Father.
It can access both mothername and fathername.
This demonstrates how a class can combine functionalities from multiple sources.'''



# MULTILEVEL INHERITENCE
# BASE CLASS
class GrandFather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername
# INTERMEDIATE CLASS    
class Father(GrandFather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        GrandFather.__init__(self,grandfathername)
# DERIVED CLASS
class Son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
        Father.__init__(self,fathername,grandfathername)

    def print_name(self):
        print("grandfather name : ",self.grandfathername)
        print("father name : ",self.fathername)
        print("son name : ",self.sonname)

s1=Son("shreyas","sanjay gupta","isher das")
s1.print_name()


# HIERARCHIAL INHERITENCE

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()