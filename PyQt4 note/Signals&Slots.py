#!python2
#coding=utf-8

"""
信号槽（Signals & Slots）
我们创建了一个QtGui.QLCDNumber和QtGui.QSlider对象，并通过拖动滑块按钮改变lcd的值。
发送者是发送信号的对象，接收者是接收信号的对象，槽（slot）是响应信号的方法。
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # 事件添加，将滑块按钮的valueChanged信号与lcd的display槽进行关联
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signals & slots')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()