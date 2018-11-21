#!python2
#coding=utf-8

"""
绝对定位（Absolute positioning）
程序员为每个部件以像素为单位制定其位置和大小。当使用绝对定位时，需要了解以下的限制：

当窗口大小改变时，部件的大小和位置不会发生变化；
在不同平台上，应用程序可能显示效果不一致；
在应用程序中改变字体可能会破坏布局；
当要改变布局时，需要完全重做所有的布局，这是相当繁琐以及费时的。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QtGui.QLabel('ZetCode', self)
        lbl1.move(15, 10)

        lbl2 = QtGui.QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QtGui.QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()