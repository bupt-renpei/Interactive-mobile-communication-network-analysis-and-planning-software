#!python2
#coding=utf-8

import sys, random
from PyQt4 import QtGui, QtCore
import configDialog, about, mainWindow

class MainProgram(QtGui.QMainWindow):

    def __init__(self):
        super(MainProgram, self).__init__()
        self.initUI()
        self.form_widget = mainWindow.MainWindow(self) 
        _widget = QtGui.QWidget()
        _layout = QtGui.QVBoxLayout(_widget)
        _layout.addWidget(self.form_widget)
        self.setCentralWidget(_widget)

    def initUI(self):

        self.statusBar().showMessage('Ready') # 设置状态栏

        # 设置"打开配置文件"动作
        openFile = QtGui.QAction(QtGui.QIcon('import.png'), u'&打开配置文件', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip(u'打开配置文件')
        openFile.triggered.connect(self.showFiledialog)

        # 设置"退出"动作
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), u'&退出', self) # 创建指定图标和'&Exit'标签的动作
        exitAction.setShortcut('Ctrl+Q') # 为该动作定义快捷键
        exitAction.setStatusTip(u'退出程序') # 当鼠标停留在菜单上时，在状态栏显示该菜单的相关信息
        exitAction.triggered.connect(QtGui.qApp.quit) # 选定特定的动作，发出触发信号

        # 设置"新的配置对话框"动作
        Configdialog = QtGui.QAction(QtGui.QIcon('openConfigdialog.png'), u'&新建配置', self)
        Configdialog.setShortcut('Ctrl+N') # 为该动作定义快捷键
        Configdialog.setStatusTip(u'打开配置对话框')
        Configdialog.triggered.connect(self.openConfigdialog)

        # 设置"关于"动作
        about = QtGui.QAction(QtGui.QIcon('about.png'), u'&关于', self)
        about.setStatusTip(u'该软件版本及作者的一些信息')
        about.triggered.connect(self.openAbout)

        # 设置"源文件链接"
        sourcesLink = QtGui.QAction(QtGui.QIcon('sourcesLink.png'), u'&查看源文件', self)
        sourcesLink.setStatusTip(u'打开 GitHub 查看源文件')
        sourcesLink.triggered.connect(self.openSourcesLink)

        # menuBar()方法创建菜单栏。我们创建了一个文件菜单，并将退出动作添加在其后。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu(u'&文件')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)

        fileMenu = menubar.addMenu(u'&配置')
        fileMenu.addAction(Configdialog)

        fileMenu = menubar.addMenu(u'&帮助')
        fileMenu.addAction(sourcesLink)
        fileMenu.addAction(about)

        self.resize(1110,740)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        # self.setGeometry(300, 300, 500, 300) # 设置窗口在屏幕上的位置与大小
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        self.setWindowTitle(u'交互式移动通信网络分析和规划软件') # 设置窗口Title
        self.show()

    def openConfigdialog(self):
        self.another = configDialog.ConfigDialog()
        self.another.show()
    
    def openAbout(self):
        self.another = about.About()
        self.another.show()

    def openSourcesLink(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/AbnerHub/Interactive-mobile-communication-network-analysis-and-planning-software-design'))

    def showFiledialog(self):
        # 第一个字符串参数指定标题，第二个字符串参数指定对话框的工作目录。
        # 默认情况下，文件过滤设置为所有文件（*）。
        fname = unicode(QtGui.QFileDialog.getOpenFileName(self, 'Open file', './', '.txt(*.txt)'))
        if fname:
            # print fname
            Data = []
            buildings = []
            building = []
            basestation = []
            datanumber = 0
            dataname = 'none'
            datacount = 0
            with open(fname, 'r') as f:
		        for line in f:
			        data = line.split()
			        Data.append(data)
		        print Data
        else:
            pass

def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainProgram()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()