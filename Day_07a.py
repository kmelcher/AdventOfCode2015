#!/usr/bin/python

import re

# Day 7 circuit emulation

# all represent 16 bit "signals" (0-65535)  (watch for overflow?)


circuit = {}


def initCircuit():
    global circuit
    circuit = {}


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
                m = re.match("([a-z]{0,}) AND ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                if m.group(1) in circuit and m.group(2) in circuit:      
                    circuit[m.group(3)] = circuit[m.group(1)] & circuit[m.group(2)]
            elif "OR" in line:
                print "or"
                m = re.match("([a-z]{0,}) OR ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                if m.group(1) in circuit and m.group(2) in circuit:      
                    circuit[m.group(3)] = circuit[m.group(1)] | circuit[m.group(2)]
            elif "LSHIFT" in line:
                print "ls"
                m = re.match("([a-z]{0,}) LSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                if m.group(1) in circuit:      
                    circuit[m.group(3)] = circuit[m.group(1)] << int(m.group(2))
            elif "RSHIFT" in line:
                print "ls"
                m = re.match("([a-z]{0,}) RSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                if m.group(1) in circuit:      
                    circuit[m.group(3)] = circuit[m.group(1)] >> int(m.group(2))
            elif "NOT" in line:
                print "not"
                m = re.match("NOT ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return
                if m.group(1) in circuit:      
                    circuit[m.group(2)] = (~circuit[m.group(1)] & 0xFFFF)
            else:
                print "assign"
                m = re.match("([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return 
                circuit[m.group(2)] = int(m.group(1))

    print circuit
#123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i


day7a("Day_07.input")
# day6a("Day_06.test.input")

# test()
