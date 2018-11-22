#!python2
#coding=utf-8

"""
复选框（QtGui.QCheckBox)
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        cb = QtGui.QCheckBox('Show title', self)
        cb.move(20, 20)
        # 由于我们在后面设置了窗口标题，因此需要选中该复选框。
        cb.toggle()
        # 将自定义的changeTitle()方法与stateChanged信号关联。
        # changeTitle()方法将会切换窗口标题。
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Check Box')
        self.show()

    # 复选框的状态将通过参数state传入到changeTitle()方法中。如果
    # 复选框被选中，我们设置窗口的标题；否则，我们将窗口标题设置为空。
    def changeTitle(self, state):

        if state == QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()