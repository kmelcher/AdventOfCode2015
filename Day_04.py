#!/usr/bin/python

import hashlib

# Day 4


def day4a(puzzleInput):
    i = 0
    while True:
        key = puzzleInput + str(i)
        m = hashlib.md5()
        m.update(key)
        hash = m.hexdigest()
        #print "input %s hash %s" % (key, hash)

        matchCount = 0
        numZeros = 6
        for pos in range(0, numZeros):
            if hash[pos] == "0":
                matchCount += 1
            else:
                break

        if matchCount == numZeros:
            print "input %s index %d hash %s" % (key, i, hash)
            break
        i += 1

#day4a("abcdef")
#day4a("pqrstuv")
day4a("ckczppom")
