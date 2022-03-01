def betterSubset(bSet):
    if bSet == []:
        yield bSet
    else:
        first = bSet[0]
        xSet = betterSubset(bSet[1:])
        for ySet in xSet:
            yield ySet
            yield [first] + ySet

def subsetHelper(hSet, setSize):
    for subset in betterSubset(hSet):
        if len(subset) == setSize:
            yield subset

def test():
    ourSet = [0,1,2,3,4]
    for size in range(len(ourSet)):
        for subset in subsetHelper(ourSet, size):
            print(subset)

test()

'''
output:
[]
[0]
[1]
[2]
[3]
[4]
[0, 1]
[0, 2]
[1, 2]
[0, 3]
[1, 3]
[2, 3]
[0, 4]
[1, 4]
[2, 4]
[3, 4]
[0, 1, 2]
[0, 1, 3]
[0, 2, 3]
[1, 2, 3]
[0, 1, 4]
[0, 2, 4]
[1, 2, 4]
[0, 3, 4]
[1, 3, 4]
[2, 3, 4]
[0, 1, 2, 3]
[0, 1, 2, 4]
[0, 1, 3, 4]
[0, 2, 3, 4]
[1, 2, 3, 4]
'''
