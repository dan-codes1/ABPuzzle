from random import * 
import copy 

def getLen() : 
    len = input()
    while(len.isnumeric() == False) :
        print("Invalid input , Please enter a number :") 
        len = input()

    return int(len)

def generateDisks(len) :  #N^2
    largeDisks = [] 
    smallDisks = [] 
    insertIdx  = randrange( len - 1 )
    for i in range(len) : 
        largeDisks.append(randrange(1,5)) # N + 1 
        smallDisks.append(randrange(1,4)) # N 
    smallDisks[insertIdx] = 0 
    return largeDisks , smallDisks

def finalConfig(a) :
    b = copy.deepcopy(a)
    b.remove(0)
    retVal = sorted(b)
    retVal.append(0)
    return retVal
    # print("Target Configuration: " , test)

def calcDiff( smallDisks , finalConfig ) : 
    print("Smaller Disks : " , smallDisks )
    print("Target        : " , finalConfig )
    print(" Legnth " , len(smallDisks))
    retVal = []
    for i in range(len(smallDisks)) : 
        if smallDisks[i] == finalConfig[i] : 
            retVal.append(0)
        else: 
            retVal.append(1)
    return retVal

def getIndex(a) :
    return a.index(0)


# Finish this later ig 

def calculateStep( idx , small , large ) : 
    if idx < 1 : 
        idx = len(small) - idx 
    step = large[idx]
    val = small[ idx + step ] 
    idxLeftArr  = diffArr
    idxRightArr = diffArr
    return 

def main() : 
    len = getLen()
    largeDisks , smallDisks = generateDisks(len)
    finalCFG = finalConfig(smallDisks)
    idx = getIndex(smallDisks)
    diffArr = calcDiff( smallDisks , finalCFG )
    print("Large : " , largeDisks)
    print("Small : " , smallDisks)
    print("Goal  : " , finalCFG  )


# if '__name__' == '__main__' : 
main()



