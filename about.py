#!python2
#coding=utf-8

"""
新的配置文件对话框
"""

import sys, random
from PyQt4 import QtGui, QtCore

class About(QtGui.QWidget):

    def __init__(self):
        super(About, self).__init__()

        self.initUI()

    def initUI(self):

        version = QtGui.QLabel(u'\t\tVersion: 1.29.1')
        author = QtGui.QLabel(u'\t\tAuthor: 孙韶鑫')
        ID = QtGui.QLabel(u'\t\tID: 41524345')
        appName = QtGui.QLabel(u'交互式移动通信网络分析和规划软件')

        h1 = QtGui.QHBoxLayout()
        h1.addWidget(version)

        h2 = QtGui.QHBoxLayout()
        h2.addWidget(author)

        h3 = QtGui.QHBoxLayout()
        h3.addWidget(ID)

        h4 = QtGui.QHBoxLayout()
        h4.addWidget(appName)

        # 创建一个垂直框布局对象，并将水平框布局对象添加到垂直框布局对象中。
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(h4)
        vbox.addLayout(h1)
        vbox.addLayout(h2)
        vbox.addLayout(h3)
        # vbox.addStretch(1)

        # 设置主窗口的布局。
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 120)
        self.setWindowTitle(u'关于')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = About()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()