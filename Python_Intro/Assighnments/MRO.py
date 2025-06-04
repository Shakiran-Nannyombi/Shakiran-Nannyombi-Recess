# Real-Life MRO Example: Multi-Role Employee

class Employee:
    def work(self):
        print("Employee: Works on general tasks.")

class Manager(Employee):
    def work(self):
        print("Manager: Oversees team and manages projects.")

class Developer(Employee):
    def work(self):
        print("Developer: Writes and reviews code.")

class TechLead(Manager, Developer):
    pass

# Instances/Objects
e = Employee()
m = Manager()
d = Developer()
t = TechLead()

# Calling work() method on each instance
print("Employee:")
e.work()
print("\nManager:")
m.work()
print("\nDeveloper:")
d.work()
print("\nTechLead:")
t.work()  # Which work() is called?

# Showing Method Resolution Order
print("\nMethod Resolution Order for TechLead class:")
for cls in TechLead.mro():
    print(cls)

# Output

# Employee:
# Employee: Works on general tasks.

# Manager:
# Manager: Oversees team and manages projects.

# Developer:
# Developer: Writes and reviews code.

# TechLead:
# Manager: Oversees team and manages projects.

# Method Resolution Order for TechLead class:
# <class '__main__.TechLead'>
# <class '__main__.Manager'>
# <class '__main__.Developer'>
# <class '__main__.Employee'>
# <class 'object'>

# [Done] exited with code=0 in 0.107 seconds