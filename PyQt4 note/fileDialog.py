#!python2
#coding=utf-8

"""
文件对话框
我们创建了一个菜单栏，一个居中的文本输入框以及状态栏。菜单项将创建一个QtGui.QFileDialog文件选择对话框用于选择文件，该文件的内容将被加载到文本输入框中。
由于我们将文本输入框居中放置，因此基于QtGui.QMainWindow。
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile) 

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        # 第一个字符串参数指定标题，第二个字符串参数指定对话框的工作目录。
        # 默认情况下，文件过滤设置为所有文件（*）。
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')

        f = open(fname, 'r')

        with f:
            # 读取文件内容，并在文本编辑对话框中显示。
            data = f.read()
            self.textEdit.setText(data)
        
        f.close()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()