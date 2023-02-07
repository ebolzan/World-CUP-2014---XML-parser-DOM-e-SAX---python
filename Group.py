# -*- coding: utf-8 -*-
__author__ = 'evandro'

import random
import operator
from GameInfo import GameInfo
from HistoryGames import HistoryGames, Games

#class make games of groups
class Group():
    def __init__(self, name):

        #group name var
        self.name = name

        self.listTeam = []

        #all team start in 0 points
        self.indexTeam = {0: 0, 1: 0, 2: 0, 3: 0 }

    def showGroup(self):
        print('Group')
        for team in self.listTeam:
            print(team)


    def getWinnersGroup(self):
        sorted_x = sorted(self.indexTeam.items(), key=operator.itemgetter(1))
        first  = sorted_x[3]
        second = sorted_x[2]

        winners = [self.listTeam[first[0]], self.listTeam[second[0]]]

        return winners

    def setGroup(self, team):
        self.listTeam = team

    def randonResult(self):
        return random.randint(1, 6)

    def createResult(self, index1, index2):
        r1 = self.randonResult()
        r2 = self.randonResult()

        while r1 == r2:
            r1 = self.randonResult()
            r2 = self.randonResult()

        if r1 > r2:
            self.indexTeam[index1] = self.indexTeam[index1] + 3
        else:
            self.indexTeam[index2] = self.indexTeam[index2] + 3

        return [r1.__str__(),r2.__str__()]


    def createGames(self, infoGames = ['date', 'time', 'adress','arena']):
        print ("------------------Jogos do grupo "+self.name +"--------------------- ")

        historyGroup = HistoryGames.instance()


        #game1
        print (infoGames[0].__str__())
        print (self.listTeam[0])
        resultGame = self.createResult(0, 1)
        print(resultGame[0], " X ",resultGame[1])
        print(self.listTeam[1])
        print("\n")

        game1 = Games(self.name, infoGames[0], self.listTeam[0], self.listTeam[1], resultGame[0], resultGame[1])

        #game2
        print (infoGames[1].__str__())
        print (self.listTeam[2])
        resultGame = self.createResult(2, 3)
        print(resultGame[0], " X ",resultGame[1])
        print(self.listTeam[3])
        print("\n")

        game2 = Games(self.name, infoGames[1], self.listTeam[2], self.listTeam[3], resultGame[0], resultGame[1])

        #game3
        print (infoGames[2].__str__())
        print (self.listTeam[0])
        resultGame = self.createResult(0, 2)
        print(resultGame[0], " X ",resultGame[1])
        print(self.listTeam[2])
        print("\n")

        game3 = Games(self.name, infoGames[2], self.listTeam[0], self.listTeam[2], resultGame[0], resultGame[1])

        #game4
        print (infoGames[3].__str__())
        print (self.listTeam[2])
        resultGame = self.createResult(2, 1)
        print(resultGame[0], " X ",resultGame[1])
        print (self.listTeam[1])
        print("\n")

        game4 = Games(self.name, infoGames[3], self.listTeam[2], self.listTeam[1], resultGame[0], resultGame[1])

        #game5
        print (infoGames[4].__str__())
        print (self.listTeam[0])
        resultGame = self.createResult(0, 3)
        print(resultGame[0], " X ",resultGame[1])
        print (self.listTeam[3])

        game5 = Games(self.name, infoGames[4], self.listTeam[0], self.listTeam[3], resultGame[0], resultGame[1])

        #game6
        print (infoGames[5].__str__())
        print (self.listTeam[1])
        resultGame = self.createResult(1, 3)
        print(resultGame[0], " X ",resultGame[1])
        print (self.listTeam[3])
        print("\n")

        game6 = Games(self.name, infoGames[5], self.listTeam[1], self.listTeam[3], resultGame[0], resultGame[1])

        historyGroup.addGame([game1, game2, game3, game4, game5, game6])

        historyGroup.printS()

        return (self.getWinnersGroup())