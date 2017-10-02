#----------------------------------------#

# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

#----------------------------------------#

# Classes
class myClass(object):
    def __init__(self):
        self.input = ""

    def getString(self):
        self.input = raw_input()

    def printString(self):
        print(self.input)
    
# Functions
def test():
    t = myClass()
    print('please input a string:')
    t.getString()
    print('\nthis is your string:')
    t.printString()

# Program
test()