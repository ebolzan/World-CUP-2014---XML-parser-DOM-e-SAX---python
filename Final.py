# -*-coding: utf-8 -*-
__author__ = 'evandro'

import random

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
        print (r1.__str__() + " X " + r2.__str__())

    def oitavas(self):
        print ("---------------------------- Oitavas de Final ----------------------------")

        #a x h
        print (self.games[0].__str__())
        print (self.groupA[0])
        self.createResult(self.groupA[0], self.groupH[1], 'quartas')
        print (self.groupH[1])
        print("\n")

        print (self.games[1].__str__())
        print (self.groupH[0])
        self.createResult(self.groupH[0], self.groupA[1], 'quartas')
        print (self.groupA[1])
        print("\n")

        # b x G
        print (self.games[2].__str__())
        print (self.groupB[0])
        self.createResult(self.groupB[0], self.groupG[1], 'quartas')
        print (self.groupG[1])
        print("\n")

        print (self.games[3].__str__())
        print (self.groupG[0])
        self.createResult(self.groupG[0], self.groupB[1], 'quartas')
        print (self.groupB[1])
        print("\n")

        #c x f
        print (self.games[4].__str__())
        print (self.groupC[0])
        self.createResult(self.groupC[0], self.groupF[1], 'quartas')
        print (self.groupF[1])
        print("\n")

        print (self.games[5].__str__())
        print (self.groupF[0])
        self.createResult(self.groupF[0], self.groupC[1], 'quartas')
        print (self.groupC[1])
        print("\n")

        #d x e
        print (self.games[6].__str__())
        print (self.groupD[0])
        self.createResult(self.groupD[0], self.groupE[1], 'quartas')
        print (self.groupE[1])
        print("\n")

        print (self.games[7].__str__())
        print (self.groupE[0])
        self.createResult(self.groupE[0], self.groupD[1], 'quartas')
        print (self.groupD[1])
        print("\n")

    #8 teams are this phase
    def quartas(self):
        print ("---------------------------- Quartas de final ----------------------------")

        #0 - 7
        print (self.games[8].__str__())
        print (self.QuFinals[0])
        self.createResult(self.QuFinals[0], self.QuFinals[7], 'semi')
        print (self.QuFinals[7])
        print("\n")

        #1- 6
        print (self.games[9].__str__())
        print (self.QuFinals[1])
        self.createResult(self.QuFinals[1], self.QuFinals[6], 'semi')
        print (self.QuFinals[6])
        print("\n")

        #2 - 5
        print (self.games[10].__str__())
        print (self.QuFinals[2])
        self.createResult(self.QuFinals[2], self.QuFinals[5], 'semi')
        print (self.QuFinals[5])
        print("\n")

        #3 - 4
        print (self.games[11].__str__())
        print (self.QuFinals[3])
        self.createResult(self.QuFinals[3], self.QuFinals[4], 'semi')
        print (self.QuFinals[4])
        print("\n")

    #this phase have 4 team
    def semi(self):
        print ("---------------------------- Semifinais ----------------------------")

        #0 - 3
        print (self.games[12].__str__())
        print (self.SeFinals[0])
        self.createResult(self.SeFinals[0], self.SeFinals[3], 'final')
        print (self.SeFinals[3])
        print("\n")

        #1 - 2
        print (self.games[13].__str__())
        print (self.SeFinals[1])
        self.createResult(self.SeFinals[1], self.SeFinals[2], 'final')
        print (self.SeFinals[2])
        print("\n")


    def final(self):
        print ("---------------------------- Final ----------------------------")

        print (self.games[15].__str__())
        print (self.finals[0])
        self.createResult(self.finals[0], self.finals[1], 'gain')
        print (self.finals[1])
        print("\n")

    def theBest(self):
        print("#################### champion #####################")
        print("#################### champion #####################")
        print("#################### champion #####################")
        print (self.TheBest)
        f = open('winner.txt', 'w')
        f.write(self.TheBest.encode('utf-8'))
        print("#################### champion #####################")
        print("#################### champion #####################")
        print("#################### champion #####################")
