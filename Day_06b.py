#!/usr/bin/python

import re

# Day 6  Fire Hazard
# part b - dimmable!


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
                grid[(x, y)] += 1
            if operation == TURN_OFF:
                if grid[(x, y)] > 0:
                    grid[(x, y)] -= 1
            if operation == TOGGLE:
                grid[(x, y)] += 2
    return


def countGrid():
    global grid
    count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if grid[(x, y)] > 0:
                count += 1
    return count


def countBrightness():
    global grid
    count = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            count += grid[(x, y)]
    return count

# Example input
# turn on 489,959 through 759,964
# turn off 427,423 through 929,502
# toggle 756,965 through 812,992
def day6a(filename):
    global grid
    initGrid()
    lineNum = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            lineNum += 1
            # print line.strip()
            # m = re.match("turn on ([0-9]{0,3}),([0-9]{0,3}) through ([0-9]{0,3}),([0-9]{0,3}).*", line)
            m = re.match("([a-z ]{0,})([0-9]{0,3}),([0-9]{0,3}) through ([0-9]{0,3}),([0-9]{0,3}).*", line.strip())
            if m is None or len(m.groups()) != 5:
                print "input error line %d %s" % (lineNum, line)
                return 
            if m.group(1) == "turn on ":
                setGrid(TURN_ON, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
            if m.group(1) == "turn off ":
                setGrid(TURN_OFF, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
            if m.group(1) == "toggle ":
                setGrid(TOGGLE, int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))

    print "count is %d" % countGrid()
    print "brighness is %d" % countBrightness()


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

day6a("Day_06.input")
# day6a("Day_06.test.input")

# test()
