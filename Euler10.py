##First attempt, tried shortening O as much as possible
def isPrime(x,thelist):
    for i in thelist:
        if x%i == 0:
            return False
    return True

def primeGen():
    generating = True
    count = 3
    thelist = [2]
    total = 2
    while generating:
        if count > 2000000:
            generating = False
        elif isPrime(count,thelist) == True:
            total += count
            thelist.append(count)
        count += 2

    
    print total


##Second Attempt, using the Sieve of Eratosthenes


markarray = [0] * 2000000 ##array size 2000000 to label
count = 3 ##start with 3 since first prime is 2
total = 2 
while count < 2000000: ##exit after exceeding 2000000
    if markarray[count] == 0: ##First value to be 0 MUST  be a prime because the previous number was not
        total += count #add to sum
        increment = count #take that number and increment rest of multiples so we dont' have to check.
        while increment < 2000000: #when to stop
            markarray[increment] = 1 #flip to 1
            increment += count #increment
    count += 2 #move up by 2's 

print total
