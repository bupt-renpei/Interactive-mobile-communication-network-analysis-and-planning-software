#!python2
#coding=utf-8

"""
事件发送者
我们创建了两个按钮。在buttonClicked()方法中，我们通过调用sender()方法来判断哪个按钮被按下。
我们通过调用sender()方法来判断信号源，并在应用程序的状态栏上显示哪个按钮被按下。
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        btn1 = QtGui.QPushButton('Button1', self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton('Button2', self)
        btn2.move(150, 50)

        # 将两个按钮关联到相同的槽（slot）。
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # 通过调用sender()方法判断信号源。
    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()