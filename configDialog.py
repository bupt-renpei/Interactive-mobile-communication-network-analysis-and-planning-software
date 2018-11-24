#!python2
#coding=utf-8

"""
新的配置文件对话框
"""

import sys, random
from PyQt4 import QtGui, QtCore

class ConfigDialog(QtGui.QWidget):

    def __init__(self):
        super(ConfigDialog, self).__init__()

        self.initUI()

    def initUI(self):
        
        thermalNoise = QtGui.QLabel(u'   热噪声')
        bandwidth = QtGui.QLabel(u'     带宽')
        frequency = QtGui.QLabel(u'     频率')
        RSRPthreshold = QtGui.QLabel(u'RSRP 门限')

        thermalNoiseEdit = QtGui.QLineEdit()
        bandwidthEdit = QtGui.QLineEdit()
        frequencyEdit = QtGui.QLineEdit()
        RSRPthresholdEdit = QtGui.QLineEdit()

        thermalNoiseUnit = QtGui.QLabel('dBm/Hz\t')
        bandwidthUnit = QtGui.QLabel('Hz\t')
        frequencyUnit = QtGui.QLabel('MHz\t')
        RSRPthresholdUnit = QtGui.QLabel('dBm\t')

        saveButton = QtGui.QPushButton(u'保存并退出')
        exitButton = QtGui.QPushButton(u'仅退出')
        exitButton.clicked.connect(self.close)

        # 创建水平框布局对象，添加伸缩因子和两个按钮。
        # 这个伸缩因子在窗口改变时会在其前面添加空白。
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(saveButton)
        hbox.addWidget(exitButton)

        h1 = QtGui.QHBoxLayout()
        h1.addWidget(thermalNoise)
        h1.addWidget(thermalNoiseEdit)
        h1.addWidget(thermalNoiseUnit)

        h2 = QtGui.QHBoxLayout()
        h2.addWidget(bandwidth)
        h2.addWidget(bandwidthEdit)
        h2.addWidget(bandwidthUnit)

        h3 = QtGui.QHBoxLayout()
        h3.addWidget(frequency)
        h3.addWidget(frequencyEdit)
        h3.addWidget(frequencyUnit)

        h4 = QtGui.QHBoxLayout()
        h4.addWidget(RSRPthreshold)
        h4.addWidget(RSRPthresholdEdit)
        h4.addWidget(RSRPthresholdUnit)

        # 创建一个垂直框布局对象，并将水平框布局对象添加到垂直框布局对象中。
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(h1)
        vbox.addLayout(h2)
        vbox.addLayout(h3)
        vbox.addLayout(h4)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 设置主窗口的布局。
        self.setLayout(vbox)

        self.resize(350,180)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
        self.setWindowTitle(u'新建配置')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = ConfigDialog()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()