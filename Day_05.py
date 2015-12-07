#!/usr/bin/python

import re

# Day 5  Naughty or Nice?


def isNice5a(line):
    # at least 3 vowels
    m = re.match(".*([aeiou]).*([aeiou]).*([aeiou]).*", line)
    if m is None:
        return False
    if len(m.groups()) < 3:
        return False

    # letter twice in a row
    # should be a regex to do this...
    dblCount = 0
    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            dblCount += 1
    if dblCount == 0:
        return False

    # does not contain ab, cd, pq, or xy
    m = re.search("ab|cd|pq|xy", line)
    if m is not None:
        return False

    return True


def day5a(filename):
    with open(filename, 'r') as infile:
        niceCount = 0
        lines = infile.readlines()
        for line in lines:
            if isNice5a(line):
                print "%s %s" % (line, "Nice")
                niceCount += 1
            else:
                print "%s %s" % (line, "naughty")

        print "Nice Count = %d" % niceCount

# ----------------------------------------


def isNice5b(line):
    # pair of letters duplicated, but not overlapping
    #  abxab OK, aaa not ok

    # 0 based indexing

    print ("[%s] len=%d" % (line, len(line)))
    match = 0
    for firstPairStart in range(0, len(line)-2):
        testPat = line[firstPairStart]+line[firstPairStart+1]
        if line.count(testPat) >= 2:
            match += 1
    if match == 0:
        return False

    # matching letter
    #  xyx

    for i in range(0, len(line)-2):
        print "%s vs %s" % (line[i], line[i+2])
        if line[i] == line[i+2]:
            return True

    return False


def day5b(filename):
    with open(filename, 'r') as infile:
        niceCount = 0
        naughtyCount = 0
        lines = infile.readlines()
        for line in lines:
            if isNice5b(line.strip()):
                print "%s %s" % (line, "Nice")
                niceCount += 1
            else:
                print "%s %s" % (line, "naughty")
                naughtyCount += 1
        print "Nice Count = %d" % niceCount
        print "Naughty Count = %d" % naughtyCount


#day5a("Day_05a.input")  # answer: 236
#day5b("Day_05b.test.input")  # answer: 236
day5b("Day_05a.input")  # answer: 236

# 49 too low
