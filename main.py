#!python2
#encoding=utf-8

class building(object):
    def __init__(self):
        return super(building, self).__init__()

class basestation(object):
    def __init__(self, number, xpos, ypos, height, power):
        self.number = number
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.power = power
        return super(basestation, self).__init__()