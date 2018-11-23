#!python2
#coding=utf-8

"""
主窗口：地图和右侧复选框及按钮的部分
"""

import sys, random
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QWidget):

    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout()
        vbox = QtGui.QVBoxLayout()

        pixmap = QtGui.QPixmap('test.jpg')

        # 将图片控件放入标签控件中
        picture = QtGui.QLabel(self)
        picture.setPixmap(pixmap)

        self.cb1 = QtGui.QCheckBox(u'覆盖情况', self)

        self.cb2 = QtGui.QCheckBox(u'下行最大速率', self)

        self.refreshButton = QtGui.QPushButton(u'分析')

        self.exitButton = QtGui.QPushButton(u'退出')
        self.exitButton.clicked.connect(QtGui.qApp.quit)

        vbox.addWidget(self.cb1)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.refreshButton)
        vbox.addStretch(1)
        vbox.addWidget(self.exitButton)

        hbox.addWidget(picture)
        hbox.addStretch(1)
        hbox.addLayout(vbox, stretch=0)

        self.setLayout(hbox)
