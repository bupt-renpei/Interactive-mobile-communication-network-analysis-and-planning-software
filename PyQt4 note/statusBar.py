#!python2
#coding=utf-8

"""
状态栏是窗口最下方的一行
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 调用QtGui.QMainWindow类的statusBar()方法获取
        # 状态栏。第一次调用statusBar()函数时，会创建状态栏。
        # 后续调用时会返回状态栏对象。showMessage()将指定
        # 的消息在状态栏中显示。
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()