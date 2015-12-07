#!/usr/bin/python

import re

# Day 6  Fire Hazard


grid = {}

TURN_ON = "on"
TURN_OFF = "off"
TOGGLE = "tog"


def initGrid():
    global globvar
    for x in range(0, 1000):
        for y in range(0, 1000):
            grid[(x, y)] = 0


def setGrid(operation, x1, y1, x2, y2):
    global globvar
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if operation == TURN_ON:
                grid[(x, y)] = 1
            if operation == TURN_OFF:
                grid[(x, y)] = 0
            if operation == TOGGLE:
                if grid[(x, y)] == 0:
                    grid[(x, y)] = 1
                else:
                    grid[(x, y)] = 0
    return


def countGrid():
    global grid
    count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[(x, y)] > 0:
                count += 1
    return count


# Example input
# turn on 489,959 through 759,964
# turn off 427,423 through 929,502
# toggle 756,965 through 812,992
def day6a(filename):
    initGrid()

    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            i = 1


def test():
    initGrid()
    setGrid(TURN_ON, 0, 0, 2, 2)
    print "count is %d" % countGrid()
    initGrid()
    print "count is %d" % countGrid()
    setGrid(TURN_ON, 0, 0, 999, 999)
    print "count is %d" % countGrid()
    setGrid(TURN_OFF, 0, 0, 2, 2)
    print "count is %d" % countGrid()
    setGrid(TOGGLE, 0, 0, 999, 999)
    print "count is %d" % countGrid()
    initGrid()
    setGrid(TURN_ON, 0, 0, 999, 0)
    print "count is %d" % countGrid()

#day6a("Day_06.input")  # answer: 236

test()