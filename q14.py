#----------------------------------------#
# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#----------------------------------------#

vals = raw_input()

d = { 'upper': 0, 'lower': 0 }
for c in vals:
    if c.isupper():
        d['upper']+=1
    elif c.islower():
        d['lower']+=1

print('UPPER CASE ' + str(d['upper']))
print('LOWER CASE ' + str(d['lower']))