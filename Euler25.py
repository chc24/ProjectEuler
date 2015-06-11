#Generate the first Fibonacci Number that has 4 digits

def genFib():
    n1 = 1
    n2 = 1

    while (n1+n2) <= 10**999:
        temp = n1
        n1 = n2
        n2 = n1+n2

    print n1+n2        
        

genFib()
