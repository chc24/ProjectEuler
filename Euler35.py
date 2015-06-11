import itertools

def rotateNum(num):
    digits = [int(x) for x in str(num)]
    n_digits = len(digits)
    n_power = n_digits - 1
    permutations = itertools.permutations(digits)
    permutation_list = [sum(v * (10 ** (n_power - i)) for i,v in enumerate(item)) for item in permutations]
    return permutation_list

def isCircular(num, markarray):

    circularlist = rotateNum(num)
    circular = True
    for item in circularlist:
        if markarray[i] == 1:
            circular = False
    return circular
            




    
circularlist = []
markarray = [0] * 1000000 ##array size 1000000

count = 3 ##start with 3 since first prime is 2
while count < 1000000: ##exit after exceeding 2000000
    if markarray[count] == 0: ##First value to be 0 MUST  be a prime because the previous number was not        
        increment = count #take that number and increment rest of multiples so we dont' have to check.
        while increment < 1000000: #when to stop
            markarray[increment] = 1 #flip to 1
            increment += count #increment
    count += 2 #move up by 2's


for i in range(len(markarray)):
    if markarray[i] == 0:
        print i
        if isCircular(i, markarray):
            print i
            circularlist.append(i)
print len(circularlist)
