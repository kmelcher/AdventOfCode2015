#!/usr/bin/python

import re

# Day 5  Naughty or Nice?


def isNice(line):
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
            if isNice(line):
                print "%s %s" % (line, "Nice")
                niceCount += 1
            else:
                print "%s %s" % (line, "naughty")

        print "Nice Count = %d" % niceCount


day5a("Day_05a.input")  # answer: 236
