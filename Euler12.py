#first triangle number to have more than 500 divisors

def countDivisors(num):
    total = 0
    for i in range(1,int(num/2)+1):
        if (num%i) == 0:
            total += 1
    return total+1
    

def triGen():
    
    count = 1
    trinum = 0
    while countDivisors(trinum) <= 500:

        trinum += count
        count += 1
    print trinum


triGen()

    
