#!python2
#coding=utf-8

"""
字体对话框
我们创建了一个按钮以及一个标签。通过按钮，我们可以调用QtGui.QFontDialog对话框设置字体，从而改变标签的字体。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        vbox = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton('Dialog', self)
        btn.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lb1 = QtGui.QLabel('Knowledge only matters', self)
        self.lb1.move(130, 20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()

    def showDialog(self):

        # 弹出字体对话框，getFont()方法返回字体名和一个布尔值。当
        # 点击‘Ok’按钮时，该布尔值为True，否则为False。
        font, ok = QtGui.QFontDialog.getFont()

        if ok:
            # 改变标签的字体。
            self.lb1.setFont(font)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()