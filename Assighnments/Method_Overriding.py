# METHOD OVERRIDING
# Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide
#a specific implementation of a method that is already provided by one of its super-classes or parent classes.

# A system for managing student enrollment in universities, demonstrating method overriding and inheritance.

# Super Class
class Makerere_University:
    def __init__(self):
        print("Welcome to Makerere University")

    def info(self):
        student_ID_NO = int(input("Enter student ID number for Makerere University: "))
        student_name = input("Enter Full Name: ")
        print(f"{student_name} you're now an enrolled student in Makerere University")
        print(f"Your Registration number is 23/U/{student_ID_NO}/PS")

# Child class
class UCU(Makerere_University):
    def __init__(self):
        print("\nWelcome to Uganda Christian University")

    def info(self):
        student_ID_NO = int(input("Enter student ID number for Uganda Christian University: "))
        student_name = input("Enter Full Name: ")
        print(f"{student_name}  you're now an enrolled student Uganda Christian University")
        print(f"Your Registration number is 23/UCU/{student_ID_NO}/PS")

# Grandchild class 
# Enrolled inherits from UCU 
class Enrolled(UCU):
    def __init__(self):
        print("\nYou're now an enrolled student in University.\nWelcome fresher")

# Creating objects
makerere = Makerere_University()
makerere.info()  # Input info for Makerere University

ucu = UCU()
ucu.info()       # Input info for UC

enrolled = Enrolled() 

#output

# Welcome to Makerere University
# Enter student ID number for Makerere University:  1560
# Enter Full Name:  Nannyombi Shakiran 
# Nannyombi Shakiran  you're now an enrolled student in Makerere University
# Your Registration number is 23/U/1560/PS

# Welcome to Uganda Christian University
# Enter student ID number for Uganda Christian University:  14580
# Enter Full Name:  Henry Sebaduka
# Henry Sebaduka  you're now an enrolled student Uganda Christian University
# Your Registration number is 23/UCU/14580/PS

# You're now an enrolled student in University.
# Welcome fresher