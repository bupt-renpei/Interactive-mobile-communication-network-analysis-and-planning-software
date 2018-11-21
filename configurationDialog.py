#!python2
#coding=utf-8

"""
新的配置文件对话框
"""

import sys, random
from PyQt4 import QtGui, QtCore

class configurationDialog(QtGui.QWidget):

    def __init__(self):
        super(configurationDialog, self).__init__()

        self.initUI()

    def initUI(self):

        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        # 创建网格布局对象，并设置部件之间的间距。
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        # 添加部件到网格中，并指定跨越的行。
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = configurationDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()