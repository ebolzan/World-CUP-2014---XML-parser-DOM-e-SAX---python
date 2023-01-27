#coding: utf-8
__author__ = 'evandro'

#class to save all informations about game {date, time, adress, arena}
class GameInfo:

    def __init__(self):
        self.info = ""

    def addInfo(self, info):
        self.info += info

    def __str__(self):
        return self.info
