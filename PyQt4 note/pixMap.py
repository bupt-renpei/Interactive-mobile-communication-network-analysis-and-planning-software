#!python2
#coding=utf-8

"""
我们在窗口上显示了一幅图片
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        # 创建图片控件，使用图片的文件名作为参数
        pixmap = QtGui.QPixmap('test.jpg')

        # 将图片控件放入标签控件中
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Pixmap')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()