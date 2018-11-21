#!python2
#coding=utf-8

"""
调色板对话框
我们创建了一个按钮和一个QtGui.QFrame对象。QtGui.QFrame对象的背景颜色设置为黑色，通过使用QtGui.QColorDialog，我们可以修改起背景颜色。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        # 初始化QtGui.QFrame的背景颜色。
        col = QtGui.QColor(0, 0, 0)

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):

        # 弹出调色板对话框。
        col = QtGui.QColorDialog.getColor()

        # 检测颜色值是否有效。如果点击‘Cancel’按钮，返回无效的颜色值；
        # 如果颜色值有效，则改变QtGui.QFrame的背景颜色。
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()