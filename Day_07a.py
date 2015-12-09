#!/usr/bin/python

import re

# Day 7 circuit emulation

# all represent 16 bit "signals" (0-65535)  (watch for overflow?)


circuit = {}

class Gate:
    name = ''
    valOne = 0
    refOne = ''
    valTwo = 0
    refTwo = ''
    operation = ''
    evaluated = False

    def Print(self):
        return "Gate name=%s v1=%d r1=%s v2=%d r2=%s op=%s" % \
            (self.name, self.valOne, self.refOne, 
            self.valTwo, self.refTwo, self.operation)

    def Print2(self):
        if self.refOne != '':
            out = self.refOne
        else:
            out = "%d" % self.valOne

        if self.operation == 'NOT':
            out = "NOT " + out + ' -> ' + self.name
            return out
        elif self.operation == "ASSIGN":
            out = out + ' -> ' + self.name
            return out
        else:
            out = out + " " + self.operation + " "

        if self.refTwo != '':
            out = out + self.refTwo + " -> " + self.name
        else:
            out = out + "%d"%self.valTwo + " -> " + self.name
        return out
            

    def initRefs(self, strIn):
        val = 0
        ref = ''
        m = re.match("[0-9]{1,}", strIn)
        if m is not None:
            val = int(strIn)
        else:
            ref = strIn
        #print "initRef [%s] %d" % (ref, val)
        return (ref, val)

    def __init__(self, name, operation, arg1, arg2):
        global circuit

        #print "Gate ctor name=%s op=%s [%s] [%s]" % (name, operation, arg1, arg2)

        self.name = name
        (self.refOne, self.valOne) = self.initRefs(arg1)
        (self.refTwo, self.valTwo) = self.initRefs(arg2)
        self.operation = operation
        circuit[name] = self
        #print self.Print()


    def value(self):
        global circuit

        if self.evaluated:
            print "already have value %d for %s" % (self.calcedValue, self.name)
            return self.calcedValue


        print "getting value for %s" % self.Print()
        if self.refOne != '':
            self.valOne = circuit[self.refOne].value()
        if self.refTwo != '':
            self.valTwo = circuit[self.refTwo].value()
        #print "2 getting value for ", self.Print()
        #print self


        if "AND" in self.operation:
            #print "v1=%d v2=%d" % (self.valOne, self.valTwo)
            self.calcedValue = self.valOne & self.valTwo
        elif "OR" in self.operation:
            self.calcedValue = self.valOne | self.valTwo
        elif "LSHIFT" in self.operation:
            self.calcedValue =  (self.valOne << self.valTwo)  & 0xFFFF
        elif "RSHIFT" in self.operation:
            self.calcedValue =  self.valOne >> self.valTwo 
        elif "NOT" in self.operation:
            self.calcedValue =  ~self.valOne & 0xFFFF
        elif "ASSIGN" in self.operation:
            self.calcedValue =  self.valOne  & 0xFFFF
        else:
            return 0/0

        self.evaluated = True
        return self.calcedValue


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

            #print line.strip()

            if "AND" in line:
                #print "and"
                m = re.match("([a-z0-9]{0,}) AND ([a-z0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                Gate(m.group(3), "AND", m.group(1), m.group(2))

            elif "OR" in line:
                #print "or"
                m = re.match("([a-z]{0,}) OR ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                Gate(m.group(3), "OR", m.group(1), m.group(2))
            elif "LSHIFT" in line:
                #print "ls"
                m = re.match("([a-z]{0,}) LSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                Gate(m.group(3), "LSHIFT", m.group(1), m.group(2))
            elif "RSHIFT" in line:
                #print "rs"
                m = re.match("([a-z]{0,}) RSHIFT ([0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 3:
                    print "input error line %d %s" % (lineNum, line)
                    return
                Gate(m.group(3), "RSHIFT", m.group(1), m.group(2))
            elif "NOT" in line:
                #print "not"
                m = re.match("NOT ([a-z]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return
                Gate(m.group(2), "NOT", m.group(1), "")
            else:
                #print "assign"
                m = re.match("([a-z0-9]{0,}) -> ([a-z]{0,}).*", line.strip())
                #print m.groups()
                if m is None or len(m.groups()) != 2:
                    print "input error line %d %s" % (lineNum, line)
                    return 
                Gate(m.group(2), "ASSIGN", m.group(1), "")


    # part1: print "a=", circuit['a'].value()    # 16076

    # part 2 override b with value from a
    Gate('b', "ASSIGN", "16076", "")
    print "a=", circuit['a'].value()    # 2797


day7a("Day_07.input")
#day7a("Day_07.test.input")

def test():
    print "d=", circuit['d'].value()
    print "e=", circuit['e'].value()
    print "f=", circuit['f'].value()
    print "g=", circuit['g'].value()
    print "h=", circuit['h'].value()
    print "i=", circuit['i'].value()
    print "x=", circuit['x'].value()
    print "y=", circuit['y'].value()


# test()
