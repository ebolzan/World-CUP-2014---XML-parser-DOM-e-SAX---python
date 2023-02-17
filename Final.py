# -*-coding: utf-8 -*-
__author__ = 'evandro'

import random
from HistoryGames import *

class Final:

    def __init__(self):

        #list classified each group
        self.groupA = []
        self.groupB = []
        self.groupC = []
        self.groupD = []
        self.groupE = []
        self.groupF = []
        self.groupG = []
        self.groupH = []

        self.historyGames = HistoryGames.instance()

    
        #string list informations games
        self.games  = []

        #list classified oitavas = 16
        self.OiFinals = []

        #list classified quartas = 8
        self.QuFinals = []

        #list classified semi = 4
        self.SeFinals = []

        #list classified final = 2
        self.finals = []

        #champion name
        self.TheBest = ""

    def setA(self, value = []):
        self.groupA = value

    def setB(self, value = []):
        self.groupB = value

    def setC(self, value = []):
        self.groupC = value

    def setD(self, value = []):
        self.groupD = value

    def setE(self, value = []):
        self.groupE = value

    def setF(self, value = []):
        self.groupF = value

    def setG(self, value = []):
        self.groupG = value

    def setH(self, value = []):
        self.groupH = value

    def ver(self):
        print (self.groupA)

    def setFinalGames(self, games = []):
        self.games = games

    #generate random values, only(1 to 6)
    def randonResult(self):
        return random.randint(1, 6)

    def putPhaseTeam(self, team, phase):

        if phase == 'quartas':
            self.QuFinals.append(team)
        elif phase == 'semi':
            self.SeFinals.append(team)
        elif phase == 'final':
            self.finals.append(team)
        elif phase == 'gain':
            self.TheBest = team
        else:
            print ("none option choose")

    #receive two names teams, run result and save in list Quartas
    def createResult(self, index1, index2, phase):
        r1 = self.randonResult()
        r2 = self.randonResult()

        while r1 == r2:
            r1 = self.randonResult()
            r2 = self.randonResult()

        if r1 > r2:
            self.putPhaseTeam(index1, phase)
        else:
            self.putPhaseTeam(index2, phase)

        #print result
        return [r1.__str__() , r2.__str__()]


    def runGame(self, infoGeneral:str ,teamA:str, teamB:str, phaseName:str):

        result = self.createResult(teamA, teamB, phaseName)
        
        print (infoGeneral, teamA, result[0]," X ", result[1], teamB, sep="\n")

        PHASE = {
            "quartas": "oitavas",
            "semi": "quartas",
            "final": "semi",
            "gain": "final"
        }

        self.historyGames.addGame(Games(PHASE[phaseName], infoGeneral, teamA, teamB, result[0], result[1]))
                

    def oitavas(self):
        print ("---------------------------- Oitavas de Final ----------------------------")

        #a x h
        self.runGame(self.games[0],self.groupA[0], self.groupH[1], 'quartas')
        self.runGame(self.games[1], self.groupH[0], self.groupA[1], 'quartas')

        # b x G
        self.runGame(self.games[2], self.groupB[0], self.groupG[1], 'quartas')
        self.runGame(self.games[3], self.groupG[0], self.groupB[1], 'quartas')
       
        #c x f
        self.runGame(self.games[4],self.groupC[0], self.groupF[1], 'quartas')
        self.runGame(self.games[5], self.groupF[0], self.groupC[1], 'quartas')

        #d x e
        self.runGame(self.games[6], self.groupD[0], self.groupE[1], 'quartas')
        self.runGame(self.games[7], self.groupE[0], self.groupD[1], 'quartas')
     

    #8 teams are this phase
    def quartas(self):
        print ("---------------------------- Quartas de final ----------------------------")

        #0 - 7
        self.runGame(self.games[8],self.QuFinals[0], self.QuFinals[7], 'semi')

        #1- 6
        self.runGame(self.games[9],self.QuFinals[1], self.QuFinals[6], 'semi')

        #2 - 5
        self.runGame(self.games[10], self.QuFinals[2], self.QuFinals[5], 'semi')

        #3 - 4
        self.runGame(self.games[11], self.QuFinals[3], self.QuFinals[4], 'semi')


    #this phase have 4 team
    def semi(self):
        print ("---------------------------- Semifinais ----------------------------")

        #0 - 3
        self.runGame(self.games[12], self.SeFinals[0], self.SeFinals[3], 'final')

        #1 - 2
        self.runGame(self.games[13], self.SeFinals[1], self.SeFinals[2], 'final')


    def final(self):
        print ("---------------------------- Final ----------------------------")

        self.runGame(self.games[15], self.finals[0], self.finals[1], 'gain')


    def theBest(self):
        print("#################### champion #####################")
        print("#################### champion #####################")
        print("#################### champion #####################")
        print (self.TheBest)
        f = open('winner.txt', 'wb')
        f.write(self.TheBest.encode('utf-8'))
        print("#################### champion #####################")
        print("#################### champion #####################")
        print("#################### champion #####################")

        self.historyGames.addGame(Games("campion", "info", self.TheBest, self.TheBest, 0, 0))


        self.historyGames.saveJsonInFile()
