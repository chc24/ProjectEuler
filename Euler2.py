fib1 = 1
fib2 = 2
nextfib = fib1+fib2
solving = True
count = 0
while solving:
    if nextfib > 4000000:
        solving = False
    if fib1%2 == 0:
        count += fib1
    nextfib = fib1+fib2
    fib1 = fib2
    fib2 = nextfib
    
   
    print count
print count
