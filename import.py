#!python2
#coding=utf-8

"""
从 data.txt 中读入数据
"""

import re

class basestation(object):
    # basestation(1, 443359,4428792,18,24.2)
    def __init__(self, number, xpos, ypos, height, power):
        self.number = number
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.power = power

basestation = {}

with open('testdata.txt', 'r') as infile:
    i = 0
    data = infile.readlines()
    print data
    for line in data:
        print line,
        if 'basestation' in line:
            basestation.append(str(i+1))
        else:
            basestation[i-1][1] = line
        print basestation
        i += 1
        # print line.strip()


""" 读文件
with open('odom.txt', 'r') as f:
    data = f.readlines()  #txt中所有字符串读入data
 
    for line in data:
        odom = line.split()        #将单个数据分隔开存好
        numbers_float = map(float, odom) #转化为浮点数
        print numbers_float
"""