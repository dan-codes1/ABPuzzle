from random import * 

def getLen() : 
    len = input()
    while(len.isnumeric() == False) :
        print("Invalid input , Please enter a number :") 
        len = input()

    return len 

def generateDisks(len) :  #N^2
    largeDisks = [] 
    smallDisks = [] 
    insertIdx  = randrange( len - 1 )
    for i in range(len + 1) : 
        largeDisks.append(randrange(1,5)) # N + 1 
        smallDisks.append(randrange(1,4)) # N 
    smallDisks[insertIdx] = 0 
    return largeDisks , smallDisks

def finalConfig(a) :
    a.remove(0)
    retVal = sorted(a)
    retVal.append(0)
    return retVal
    # print("Target Configuration: " , test)

def calcDiff( smallDisks , finalConfig) : 
    retVal = []
    for i in range(len(smallDisks)) : 
        if smallDisks[i] == finalConfig[i] : 
            retVal[i] = 1
        else: 
            retVal[i] = 0
        return retVal

largeDisks , smallDisks = generateDisks(10)
print(smallDisks)
finalConfig(smallDisks)
print(smallDisks)
