def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x%i == 0:
            return False
    return True

def primeGen():
    generating = True
    count = 3
    thelist = [2]
    while generating:
        if len(thelist) > 10002:
            generating = False
        if isPrime(count) == True:
            thelist.append(count)
        count += 2
    print thelist[10000]

primeGen()
