#!/usr/bin/python

import itertools

def try_all_permutations(permutelist):
    X = 0
    Y = 0
    permuts = [[]]  #Create new List of Lists
    permuts.pop()   #Delete the empty list in this list
    for permut in itertools.permutations(permutelist):
        permuts.append(permut)

    for i in range(0,len(permuts)):
        Xlist = permuts[i][0:5]
        Ylist = permuts[i][5:9]
        for i in range(-1,-6,-1):
            X = X + Xlist[i] * 10**(abs(i)-1)
        for i in range(-1,-5,-1):
            Y = Y + Ylist[i] * 10**(abs(i)-1)

        if (33333 == X-Y):
            print "X:{0} Y:{1}".format(X, Y)
            print "{0}-{1} = {2}".format(X, Y, X-Y)
        X = 0
        Y = 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try_all_permutations(numbers)
