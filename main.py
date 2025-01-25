from random import randrange
import copy

def getLen():
    length = input("Enter the length of the disk arrays: ")
    while not length.isnumeric():
        print("Invalid input, please enter a number:")
        length = input()

    return int(length)

def generateDisks(length):  # Generate large and small disks
    largeDisks = []
    smallDisks = []
    insertIdx = randrange(length - 1)
    for i in range(length):
        largeDisks.append(randrange(1, 5))  # Large disks labeled from 1 to 4
        smallDisks.append(randrange(1, 4))  # Small disks labeled from 1 to 3
    smallDisks[insertIdx] = 0  # Place a "0" randomly in small disks
    return largeDisks, smallDisks

def finalConfig(smallDisks):
    b = copy.deepcopy(smallDisks)
    b.remove(0)  # Remove the 0 temporarily
    retVal = sorted(b)  # Sort the rest
    retVal.append(0)  # Append 0 at the end
    return retVal

def getIndex(a):
    return a.index(0)  # Find the index of the uncovered large disk

def moveDisk(smallDisks, idxFrom, idxTo):
    """Move a small disk from one index to another."""
    smallDisks[idxTo] = smallDisks[idxFrom]
    smallDisks[idxFrom] = 0  # Set the original position to uncovered (0)

 

def bestFitSearch(largeDisk, smallDisk, goalConfig):
    """Perform the best fit search to solve the puzzle."""

    while smallDisk != goalConfig:
        zeroIdx = getIndex(smallDisk)  # Get the index of the uncovered large disk
        spacesToMove = largeDisk[zeroIdx] # Wherever the 0 is in the small disk we want the equivalent in large disk
        smallDisk.insert(spacesToMove, 0)
        if smallDisk == goalConfig:
            break
    

def main():
    length = getLen()
    largeDisks, smallDisks = generateDisks(length)
    finalCFG = finalConfig(smallDisks)

    print("Initial Configuration:")
    print("Large Disks: ", " ".join(map(str, largeDisks)))
    print("Small Disks: ", " ".join(map(str, smallDisks)))
    print("Goal Configuration: ", " ".join(map(str, finalCFG)))

    bestFitSearch(largeDisks, smallDisks, finalCFG)

if __name__ == "__main__":
    main()
