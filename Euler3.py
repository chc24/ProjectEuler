import math

def primeFactorize(x):
    divisible = []
    for i in range(1,int(math.sqrt(x) + 1)):
        if x%i == 0:
            divisible.append(i)
    divisible.reverse()
    for number in divisible:
        if isPrime(number) == True:
            return number
def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            return False
    return True

num = primeFactorize(600851475143)
print "the answer is" , num
