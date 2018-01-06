import numpy
import random
from bridgeTypes import *
from chooser import *

#possibleBridges = [bridgeLeft,bridgeRight,bridgeDown,bridgeTop]
#possibleBridges = [bridgeLeft,bridgeRight,bridgeTop]

def countIslands(matrix):    
    islandArray = [x for x in matrix.ravel() if x > 0 ]
    return len(islandArray)

def getRandomIsland(matrix):
    islands = []
    for x in range(0,matrix.shape[0]):
        for y in range(0,matrix.shape[1]):
            if matrix[x][y] > 0:
                islands.append((x,y))
    if len(islands) == 0:
        return (None,None)
    return random.choice(islands)


def createIslands(matrix, island_x, island_y, lenRanges):
    '''return the number of new islands created'''
    if island_x is None:
        island_x = random.randint(0, matrix.shape[0]-1)
        island_y = random.randint(0, matrix.shape[1]-1)

    posBridges = possibleBridges(matrix, island_x, island_y)
    numBridges = random.randint(1, len(posBridges))

    #TODO ottimizzare per non ripetere gli stessi ponti
    for b in range(0,numBridges):
        bridgeFunction = random.choice(posBridges)
        #print(island_x,island_y,bridgeFunction.__name__)        
        bLen = chooseFromRanges(lenRanges)
        bridgeFunction(matrix,island_x,island_y,bLen)        

def buildMatrix(dimensions, numBridges):
    matrix = numpy.zeros((dimensions, dimensions))    
    
    #bridge lenghts, predilige i ponti corti
    sequence = [l for l in range(2,matrix.shape[0])]    
    seq_inverse = inverseSequence(sequence)
    ranges = createRange(seq_inverse)

    countLoop = 0 # per sicurezza
    while countIslands(matrix) <= numBridges and countLoop < 5000:
        island = getRandomIsland(matrix)    
        createIslands(matrix,island[0],island[1],ranges)
        countLoop += 1
    print (matrix)
    return matrix

