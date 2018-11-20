#!python2
#coding=utf-8

import sys
import random
from PyQt4 import QtGui, QtCore

L = 10
T = 10
U = 20

def getPos(x,y):
    return L+x*U, T+y*U

class MapWidget(QtGui.QWidget):
    def __init__(self, parent):
        self.chess_pos = []
        self.refreshPos()
        super(MapWidget, self).__init__(parent)

    def refreshPos(self):
        self.chess_pos = []
        for i in range(100):
            x = random.randint(0,19)
            y = random.randint(0,19)
            self.chess_pos.append((x,y))
    
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        # qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.begin(self)
        self.drawMySelf(event, qp)
        qp.end()
        
    def drawMySelf(self, event, qp):
        pen_black = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        brush_black = QtGui.QBrush(QtCore.Qt.black)
        brush_white = QtGui.QBrush(QtCore.Qt.white)
        qp.setPen(pen_black)
        for i in range(20):
            qp.drawLine(L+i*U, T, L+i*U, T+U*19)
            qp.drawLine(L, T+i*U, L+U*19, T+i*U)
        for i in range(len(self.chess_pos)):
            x, y = self.chess_pos[i]
            rx, ry = getPos(x,y)
            if i%2==0:
                qp.setBrush(brush_black)
            else:
                qp.setBrush(brush_white)
            qp.drawEllipse(rx-U*0.3,ry-U*0.3, U*0.6, U*0.6)

class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()
        self.resize(600,450)
        self.show()
    
    def initUI(self):
        self.setWindowTitle(u'交互式移动通信网络分析和规划软件')
        hbox = QtGui.QHBoxLayout()
        self.chess = MapWidget(self)
        hbox.addWidget(self.chess, stretch = 1)
        
        vbox = QtGui.QVBoxLayout()

        self.refreshButton = QtGui.QPushButton(u'分析')
        self.refreshButton.clicked.connect(self.refreshChess)
        vbox.addWidget(self.refreshButton, stretch=1)

        self.exitButton = QtGui.QPushButton(u'退出')
        self.exitButton.clicked.connect(self.close)
        vbox.addWidget(self.exitButton, stretch=1)

        hbox.addLayout(vbox, stretch=0)

        self.setLayout(hbox)
    
    def refreshChess(self):
        self.chess.refreshPos()
        self.chess.update()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()