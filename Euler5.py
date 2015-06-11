import math
def smallMul():
    count = 9699690
    counting = True
    count2 = 0
    while counting:
        for i in range(20,1,-1):
            if count % i != 0:
                count += 9699690
                count2 += 1
        if count2 == 0:
            counting = False
        elif count2 > 0:
            count2 = 0
        print "found it" , count
        
smallMul()
