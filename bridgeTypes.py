import numpy
import random

def possibleBridges(matrix, x, y):
    bridges = []
    if x < matrix.shape[0] - 2:
        bridges.append(bridgeRight)
    if x >= 2:
        bridges.append(bridgeLeft)
    if y < matrix.shape[1] - 2:
        bridges.append(bridgeTop)
    if y >= 2:
        bridges.append(bridgeDown)
    return bridges

def addBridge (matrix, start, end):
    '''Add 1 or 2 (randomly) bridge(s) to island's counter '''
    bridgesCount = random.randint(1, 2)
    matrix[start[0]][start[1]] += bridgesCount
    matrix[end[0]][end[1]] += bridgesCount

def bridgeBuilderHoriz (matrix,start,end,bridge):

    #bridge too long
    if end[1] not in range(0,matrix.shape[1]):
        return 

    # start and end have to be islands or nothing, not bridge
    if matrix[start[0]][start[1]] < 0 or matrix[end[0]][end[1]] < 0:
        return    

    bridgeArray = matrix[bridge[0]][bridge[1]:bridge[2]]

    #checks if bridge is clear
    for b in bridgeArray:
        if b != 0:
            return

    bridgeArray.fill(-1)   
    addBridge(matrix, start, end) 


def bridgeRight (matrix,row,col,bridgeLen):
    start = (row,col)
    end = (row,col+bridgeLen)
    bridge = (row,start[1]+1,end[1])
    bridgeBuilderHoriz (matrix,start,end,bridge)

def bridgeLeft (matrix,row,col,bridgeLen):
    start = (row,col)
    end = (row,col-bridgeLen)
    bridge = (row,end[1]+1,start[1])
    bridgeBuilderHoriz (matrix,start,end,bridge)

def bridgeBuilderVert (matrix,start,end,bridge):
    #bridge too long
    if end[0] not in range(0,matrix.shape[0]):
        return 
    
    # start and end have to be islands or nothing, not bridge
    if matrix[start[0]][start[1]] < 0 or matrix[end[0]][end[1]] < 0:
        return    

    bridgeArray = [b for b in matrix[bridge[1]:bridge[2]]]

    #checks if bridge is clear
    for b in bridgeArray:
        if b[bridge[0]] != 0:
            return       

    #and set the path
    for b in bridgeArray:     
        b[bridge[0]] = -1

    addBridge(matrix, start, end) 

def bridgeTop (matrix,row,col,bridgeLen):
    start = (row,col)
    end = (row-bridgeLen,col)
    bridge = (col,end[0]+1,start[0])
    bridgeBuilderVert (matrix,start,end,bridge)

def bridgeDown (matrix,row,col,bridgeLen):
    start = (row,col)
    end = (row+bridgeLen,col)
    bridge = (col,start[0]+1,end[0])
    bridgeBuilderVert (matrix,start,end,bridge)
