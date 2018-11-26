#!python2
#coding=utf-8

"""
从 data.txt 中读入数据
"""

Data = []
with open('testdata.txt', 'r') as f:
		for line in f:
			data = line.split()
			Data.append(data)
		print Data[1][1]