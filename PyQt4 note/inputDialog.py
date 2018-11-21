#!python2
#coding=utf-8

"""
输入对话框
输入的值可以是字符串、数字或者列表中的某一项。
我们创建了一个按钮和一个行输入编辑框。按钮用于显示输入对话框并获取输入值，用户输入的数据将会在行输入编辑框中显示。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):

        # 创建输入对话框，并获取用户输入。
        # 第一个字符串时对话框标题，第二个字符串是对话框显示的消息内容
        # 对话框返回用户输入的文本和一个布尔值。当点击‘Ok’按钮时，布尔值为True。
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            # 将接收自对话框的内容在行编辑输入框中显示。
            self.le.setText(str(text))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()