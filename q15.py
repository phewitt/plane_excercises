#----------------------------------------#
# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#----------------------------------------#

val = raw_input()

def add(num, num_digits):
    result = 0
    for val in range(1,num_digits+1):
        result += int(str(num)*val)
    return result

print(add(val,4))
