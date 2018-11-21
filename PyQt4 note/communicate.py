#!python2
#coding=utf-8

"""
信号发射
我们创建了一个名为closeApp的信号，该信号在鼠标按下时发送，并且该信号与QtGui.QMainWindow的close()方法关联。
"""

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):

    # 通过QtCore.pyqtSignal创建外部类Communicate
    # 的一个属性，从而创建一个信号。
    closeApp = QtCore.pyqtSignal()

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        # 将自定义信号与QtGui.QMainWindow的close()方法关联。
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 当在窗口上按下鼠标时，发送closeApp信号。
    def mousePressEvent(self, event):

        self.c.closeApp.emit()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()