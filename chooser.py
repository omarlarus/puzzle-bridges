import random

def createRange(values):  
    tot = sum([x[1] for x in values])  
    probs = [(x[0],x[1]/tot) for x in values]
    rangeArray = []
    prev = 0
    for p in probs:
        nextVal = prev + p[1]
        slot = (prev, nextVal)
        prev = nextVal
        rangeArray.append((p[0],slot))
    return rangeArray

def chooseFromRanges(ranges):
    r = random.random()
    choice = [x[0] for x in ranges if x[1][0] <= r and x[1][1] > r]
    return choice[0]

def inverseSequence(sequence):
    seq_max = max(sequence)
    seq_inverse = [(x,seq_max-x+1) for x in sequence]
    return seq_inverse
