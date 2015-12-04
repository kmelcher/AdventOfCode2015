#!/usr/bin/python

# Day 3


def day3a(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            dict = {}
            x = 0
            y = 0
            if (x, y) in dict:
                dict[(x, y)] += 1
            else:
                dict[(x, y)] = 1
            for i in range(0, len(line)):
                print "char=%s" % line[i]
                if line[i] == '^':
                    y += 1
                if line[i] == 'v':
                    y -= 1
                if line[i] == '>':
                    x += 1
                if line[i] == '<':
                    x -= 1
                print "x=%d y=%d" % (x, y)
                if (x, y) in dict:
                    dict[(x, y)] += 1
                else:
                    dict[(x, y)] = 1
            print "num visits is %d" % len(dict)


def day3b(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            dict = {}
            x = 0
            y = 0
            if (x, y) in dict:
                dict[(x, y)] += 1
            else:
                dict[(x, y)] = 1
            for i in range(0, len(line)):
                print "char=%s" % line[i]
                if line[i] == '^':
                    y += 1
                if line[i] == 'v':
                    y -= 1
                if line[i] == '>':
                    x += 1
                if line[i] == '<':
                    x -= 1
                print "x=%d y=%d" % (x, y)
                if (x, y) in dict:
                    dict[(x, y)] += 1
                else:
                    dict[(x, y)] = 1
            print "num visits is %d" % len(dict)


day3b("Day_03a.test.input")
