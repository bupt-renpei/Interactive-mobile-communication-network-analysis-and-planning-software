#!python2
#coding=utf-8

"""
框布局（Box layout）
由布局类提供的布局管理更加的灵活和实用。它是将小部件放置在主窗口上的首先方法。
QtGui.QHBoxLayout和QtGui.QVBoxLayout是基本的布局类用于横向或纵向排列小部件。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # 创建两个按钮。
        okButton = QtGui.QPushButton('OK')
        cancelButton = QtGui.QPushButton('Cancel')

        # 创建水平框布局对象，添加伸缩因子和两个按钮。
        # 这个伸缩因子在窗口改变时会在其前面添加空白。
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建一个垂直框布局对象，并将水平框布局对象
        # 添加到垂直框布局对象中。
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置主窗口的布局。
        self.setLayout(vbox)



        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Box Layout')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()