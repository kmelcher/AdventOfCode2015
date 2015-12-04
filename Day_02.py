#!/usr/bin/python

import re

# part 1(a)  
#  1000 lines of input

# parse intput in the form of "12x3x33"
def parseDimensions(line):
    m = re.match("([0-9]*)x([0-9]*)x([0-9]*)", line)
    if len(m.groups()) == 3:
        return (int(m.group(1)),int(m.group(2)),int(m.group(3)))

def day2a(filename):
    sum = 0;
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            #print "line=%s" % line
            (l,w,h) = parseDimensions(line)
            #print "%d x %d x %d" % (l, w, h)
            size = 2*l*w + 2*l*h + 2*w*h
            
            # find min area of l, w, h
            min = l*w;
            if (l*h < min):
                min = l*h
            if (w*h < min):
                min = w*h
            #print "size = %d" % size
            #print "size with extra = %d" % (size+min)
            sum = sum + size + min
    print "sum is %d" % sum

    
    
#     
def day2b(filename):
    sum = 0;
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            #print "line=%s" % line
            dims = parseDimensions(line)
            #print dims
            dims = sorted(dims)
            #print dims
            perimeter = dims[0] + dims[1] + dims[0] + dims[1]
            vol = dims[0] * dims[1] * dims[2]
            #print "vol=%d"% vol
            length = perimeter+vol
            #print "len=%d"%length
            sum += length
            
    print "sum is %d" % sum

    
#day2a("Day_02a.input")        
day2b("Day_02b.input")        
