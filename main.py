#!python2
#coding=utf-8

import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300) # 设置窗口在屏幕上的位置与大小

        self.setWindowTitle(u'交互式移动通信网络分析和规划软件') # 设置窗口Title

        self.statusBar().showMessage('Ready') # 设置状态栏

        # 设置"打开配置文件"动作
        importAction = QtGui.QAction(QtGui.QIcon('import.png'), u'&打开配置文件', self)
        importAction.setShortcut('Ctrl+O')
        importAction.setStatusTip(u'打开配置文件')

        # 设置"退出"动作
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), u'&退出', self) # 创建指定图标和'&Exit'标签的动作
        exitAction.setShortcut('Ctrl+Q') # 为该动作定义快捷键
        exitAction.setStatusTip(u'退出程序') # 当鼠标停留在菜单上时，在状态栏显示该菜单的相关信息
        exitAction.triggered.connect(QtGui.qApp.quit) # 选定特定的动作，发出触发信号

        # menuBar()方法创建菜单栏。我们创建了一个文件菜单，并将退出动作添加在其后。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu(u'&文件')
        fileMenu.addAction(importAction)
        fileMenu.addAction(exitAction)

        fileMenu = menubar.addMenu(u'&配置')

        fileMenu = menubar.addMenu(u'&帮助')

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()