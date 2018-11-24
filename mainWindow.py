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

# --------------------------------------------------------------#
        qp = QtGui.QPainter()
        qp.begin(self)

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        qp.drawLine(20, 40, 250, 40)

        pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(20, 80, 250, 80)

        pen.setStyle(QtCore.Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 120, 250, 120)

        pen.setStyle(QtCore.Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20, 160, 250, 160)

        pen.setStyle(QtCore.Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 200, 250, 200)

        pen.setStyle(QtCore.Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 5, 4])
        qp.setPen(pen)
        qp.drawLine(20, 240, 250, 240)

        qp.end()
# ---------------------------------------------------------------#        

        self.cb1 = QtGui.QCheckBox(u'覆盖情况', self)

        self.cb2 = QtGui.QCheckBox(u'下行最大速率', self)

        self.analysisButton = QtGui.QPushButton(u'分析')

        self.exitButton = QtGui.QPushButton(u'退出')
        self.exitButton.clicked.connect(QtGui.qApp.quit)

        vbox.addWidget(self.cb1)
        vbox.addWidget(self.cb2)
        vbox.addWidget(self.analysisButton)
        vbox.addStretch(1)
        vbox.addWidget(self.exitButton)

        # hbox.addWidget(qp)
        hbox.addStretch(1)
        hbox.addLayout(vbox, stretch=0)

        self.setLayout(hbox)

        self.show()
