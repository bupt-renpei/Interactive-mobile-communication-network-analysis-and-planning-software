#!python2
#coding=utf-8

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # QtGui.QAction是关于菜单栏、工具栏或自定义快捷键动作的抽象。
        # 创建指定图标和'&Exit'标签的动作。
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        # 为该动作定义快捷键。
        exitAction.setShortcut('Ctrl+Q')
        # 当鼠标停留在菜单上时，在状态栏显示该菜单的相关信息。
        exitAction.setStatusTip('Exit application')
        # 选定特定的动作，发出触发信号。该信号与QtGui.QApplication部件的quit()方法
        # 相关联，这将会终止应用程序。
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        # menuBar()方法创建菜单栏。我们创建了一个文件菜单，并将退出动作添加在其后。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()