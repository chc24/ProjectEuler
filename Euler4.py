
def isPalin(x):
    str1 = str(x)[:len(str(x))/2]
    if len(str(x))%2 == 0:
        str2 = str(x)[len(str(x))/2:]
    else:
        str2 = str(x)[len(str(x))/2+1:]

    if str1[::-1] == str2:
        return True
    else:
        return False

def findMax():
    palist = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if isPalin(i*j) == True:
                palist.append((i*j))
    print max(palist)
                

themax = findMax()
print themax
