#!python2
#coding=utf-8

"""
从 data.txt 中读入数据
"""

"""
import os
with open((os.path.join('testdata.txt')), 'r') as f:
	data = f.read()

strlist = data.split('md5=')
for item in strlist[1:]:
	try:
		list_link = item.split(' target=_blank')[0]
		print list_link
	except:
		pass
"""
import matplotlib.pyplot as plt

with open('testdata.txt', 'r') as f:
    X, Y, H, P = zip(*[[float(s) for s in line.split()] for line in f])

plt.plot(X, Y, H, P)
plt.show()