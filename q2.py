#----------------------------------------#

# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

#----------------------------------------#

# Functions
def recursive_factorial(x):
    if x == 0:
        return 1
    else:
        return x * recursive_factorial(x - 1)

def iterative_factorial(x):
    result = 1
    for i in range(1,x):
            result *= i+1
    return result

# Program
print('please input an integer value:')
val = raw_input()
print('recursive factorial: ' + str(recursive_factorial(int(val))))
print('iterative factorial: ' + str(iterative_factorial(int(val))))