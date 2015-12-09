#!/usr/bin/python

import re

# Day 8: Matchsticks ---
# https://docs.python.org/2/howto/regex.html

#The only escape sequences used are 
#   \\ (which represents a single backslash), 
#   \" (which represents a lone double-quote character), and 
#   \x plus two hexadecimal characters (which represents a single character with that ASCII code).
def analyze(line):
    fileSpace = len(line)
    print "line in    [%s]" % line
    memSpace = 0

    # remove outer quotes
    p = re.compile('^\"|\"$')
    (line, count) = p.subn('', line)
    print "line out 1 [%s]" % line

    # remove escaped quotes
    p = re.compile('\\\"')
    (line, count) = p.subn('X', line)
    print "line out 2 [%s]" % line

    # remove hex lits
    p = re.compile('\\\\x..')
    (line, count) = p.subn('X', line)
    print "line out 3 [%s]" % line

    # remove double backslash
    p = re.compile('\\\\')
    (line, count) = p.subn('x', line)
    print "line out 4 [%s]" % line

    memSpace = len(line)

    return (fileSpace, memSpace)

def day8a(filename):

    lineNum = 0
    totalFileSpace = 0
    totalMemSpace = 0

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            lineNum += 1
            line = line.strip()

            (fileSpace, memSpace) = analyze(line)
            print "file=%3d mem=%3d %s" % (fileSpace, memSpace, line)
            totalFileSpace += fileSpace
            totalMemSpace += memSpace
    print "file=%3d mem=%3d diff=%d" % (totalFileSpace, totalMemSpace, totalFileSpace-totalMemSpace)

day8a("Day_08.test.input")
