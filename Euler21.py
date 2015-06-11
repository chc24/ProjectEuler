#find sum of all aimcable numbers under 10k
import math

def checkAmicable(num1,num2):

    if num1 == num2:
        return False
    if (sumofDivisors(num1) == num2) & (sumofDivisors(num2) == num1):
        return True
    return False

def isPrime(num):

    for i in range(2,int(math.sqrt(num)+1)):
        if (num%i == 0):
            return False
    return True
def sumofDivisors(num):
    total = 0
    for i in range(1,int(num/2)+1):
        if (num%i) == 0:
            total += i
    return total
    
def amicableSum():

    amicablelist = []
    sumamicable = 0
    checkednums = []
    for i in range(2,10000):
        
        if isPrime(i) == True:
            print "skipped" , i
            continue
            
        for j in range(2,10000):
            
            if isPrime(j) == True:
                continue
            pair1 = (i,j)
            pair2 = (j,i)
            checkednums.append(pair1)
            
            if pair1 in checkednums or pair2 in checkednums:
                continue
            if checkAmicable(i,j) == True:
                if (pair1 not in amicablelist) & (pair2 not in amicablelist):
                    amicablelist.append(pair1)

    for pair in amicablelist:
        sumamicable += sum(pair)
    print amicablelist
    print sumamicable

amicableSum()


