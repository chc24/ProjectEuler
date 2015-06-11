
def powerTwo(num):

    power = str(2**num)
    total = 0
    for _num in power:
        total += int(_num)
    print total


powerTwo(1000)
