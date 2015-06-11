from math import *
def facSum(num):

    mul = str(factorial(num))
    total = 0
    for digit in mul:
        total += int(digit)

    print total


facSum(100)
