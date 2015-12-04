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
            x = {}
            y = {}
            x[0] = x[1] = 0
            y[0] = y[1] = 0
            dict[(0, 0)] = 1
            for i in range(0, len(line)):
                santa = i % 2
                #print "char=%s santa=%d" % (line[i], santa)
                if line[i] == '^':
                    y[santa] += 1
                if line[i] == 'v':
                    y[santa] -= 1
                if line[i] == '>':
                    x[santa] += 1
                if line[i] == '<':
                    x[santa] -= 1
                #print "x=%d y=%d" % (x[santa], y[santa])
                if (x[santa], y[santa]) in dict:
                    dict[(x[santa], y[santa])] += 1
                else:
                    dict[(x[santa], y[santa])] = 1
            print "num visits is %d" % len(dict)


day3b("Day_03a.input")
