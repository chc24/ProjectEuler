import math
from operator import *
def pyGen():
    triplist = []
    foundlist = []
    searching = True
    while searching:
        for i in range(1,1000):
            for j in range(1,1000):
                if isTrip(i,j) == True:
                    thesum = int(math.sqrt(i**2+j**2))
                    if (i+j+thesum) == 1000:
                            print i,j,thesum
                            print i*j*thesum
                            searching = False
                        
        searching = False
    



def isTrip(i,j):
    a = i**2
    b = j**2
    c = math.sqrt(a+b)
    if c == int(c):
        return True
    else:
        return False


pyGen()
