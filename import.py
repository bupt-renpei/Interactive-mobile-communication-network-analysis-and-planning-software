#!python2
#coding=utf-8

"""
从 data.txt 中读入数据
"""

class basestation(object):
    def __init__(self, number, xpos, ypos, height, power):
        self.number = number
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.power = power

basestation = []

"""
basestation = [
                [1, 443359, 4428792, 18, 24.2],
                [2, 444783, 4427964, 14, 24.2]
            ]
"""

# print basestation

infile = open('testdata.txt', 'r')

line = infile.readline()

while line:
    print line,


    line = infile.readline()

infile.close()


""" 读文件
with open('odom.txt', 'r') as f:
    data = f.readlines()  #txt中所有字符串读入data
 
    for line in data:
        odom = line.split()        #将单个数据分隔开存好
        numbers_float = map(float, odom) #转化为浮点数
        print numbers_float
"""