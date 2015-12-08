#!/usr/bin/python

import re

# Day 7 circuit emulation

# all represent 16 bit "signals" (0-65535)  (watch for overflow?)


circuit = {}



class Gate:
    valOne = 0
    refOne = ''
    valTwo = 0
    refTwo = ''
    operation = ''

    def value():
        global circuit

        if refOne != '':
            valOne = circuit[refOne].value()
        if refTwo != '':
            valTwo = circuit[refTwo].value()

        if "AND" in operation:
            return valOne & valTwo
        elif "OR" in operation:
            return valOne | valTwo
        elif "LSHIFT" in operation:
            return valOne << valTwo
        elif "RSHIFT" in operation:
            return valOne >> valTwo
        elif "NOT" in operation:
            return ~valOne & 0xFFFF
        elif "assign" in operation:
            return valOne


def initCircuit():
    global circuit
    circuit = {}


# values in can either be a reference to a signal
# or a number (signal).  If alpha (a-z), then deref (if it exists)
# and return value.
def getValue(strIn):
    global circuit
    v = 0
    m = re.match("[0-9]{1,}", strIn)
    if m is not None:
        v = int(strIn)
    else:
        if strIn in circuit:
            v = circuit[strIn]
    return v


def day7a(filename):
    global circuit
    initCircuit()

    lineNum = 0
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            lineNum += 1

            print line.strip()

            if "AND" in line:
                print "and"
                m = re.match("([a-z0-9]{0,}) AND ([a-z0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                circuit[m.group(3)] = getValue(m.group(1)) & getValue(m.group(2))
            elif "OR" in line:
                print "or"
                m = re.match("([a-z]{0,}) OR ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                circuit[m.group(3)] = getValue(m.group(1)) | getValue(m.group(2))
            elif "LSHIFT" in line:
                print "ls"
                m = re.match("([a-z]{0,}) LSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                circuit[m.group(3)] = getValue(m.group(1)) << getValue(m.group(2))
            elif "RSHIFT" in line:
                print "ls"
                m = re.match("([a-z]{0,}) RSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                circuit[m.group(3)] = getValue(m.group(1)) >> getValue(m.group(2))
            elif "NOT" in line:
                print "not"
                m = re.match("NOT ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return
                circuit[m.group(2)] = (~getValue(m.group(1)) & 0xFFFF)
            else:
                print "assign"
                m = re.match("([a-z0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return 
                circuit[m.group(2)] = getValue(m.group(1))

    print circuit

    print "a = %d" % circuit['a']

#123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i


day7a("Day_07.test.input")
# day7a("Day_07.input")


# test()
