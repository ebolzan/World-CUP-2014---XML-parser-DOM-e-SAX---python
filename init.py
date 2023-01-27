# -*- coding: utf-8 -*-
__author__ = 'evandro'

from Group import Group
from GameInfo import GameInfo
from Final import Final

import xml.sax
from xml.sax.saxutils import escape, unescape, quoteattr
import random

#tuples save names of grupos, this is constants names
groupNames = ("A", "B", "C", "D", "E", "F", "G", "H")

print (groupNames)

class Game(xml.sax.ContentHandler):

    def __init__(self):
        self.current = ""
        self.time    = ""
        self.grupo   = ""

        #are used to save and choose all teams
        self.pote1 = []
        self.pote2 = []
        self.pote3 = []
        self.pote4 = []

        self.game  = False

        #keys
        self.is_stage_group = False
        self.is_stage_final = False

        self.list_game = ['data', 'horario', 'estadio', 'local']
        self.item_game = False

        #to save string list of games (date, time, place, arena)
        self.stage_group_games = []
        self.stage_final_games = []

        #get teams champions by group
        self.finals = Final()


    def startElement(self, tag, attributes):
        self.current = tag

        if tag == 'pote':
            self.grupo = attributes["numero"]
        #    print ("grupo " + self.grupo)

        #if tag == 'grupo':
        #    print ('Grupo : ',attributes['letra'])


        if tag == 'fase_de_grupos':
            self.is_stage_group = True

        if tag == 'fase_final':
            self.is_stage_final = True

        if tag == 'jogo':
            self.game = True
            #create new gameinfo
            self.gameinfo = GameInfo()

        if tag in self.list_game:
            self.item_game = True

    #overhide
    def characters(self, content):
        dado = escape(content)

        if self.current == 'selecao':
            self.time = content

        if self.grupo == '1' and self.current == 'selecao':

            #pote 1
            self.pote1.append(dado)

        if self.grupo == '2' and self.current == 'selecao':

            #pote 2
            self.pote2.append(dado)

        if self.grupo == '3' and self.current == 'selecao':

            #pote 3
            self.pote3.append(dado)

        if self.grupo == '4' and self.current == 'selecao':

            #pote 4
            self.pote4.append(dado)

        #print game group
        if self.is_stage_group and self.game and self.item_game:
            self.gameinfo.addInfo(content)
            self.gameinfo.addInfo(" ")

        #print game finals
        if self.is_stage_final and self.game and self.item_game:
            self.gameinfo.addInfo(content)
            self.gameinfo.addInfo(" ")

    def endElement(self, tag):
        #if self.current == 'selecao':
         #   print('selecao:  '+ self.time)

        #if self.current == 'pote':
          #  print('grupo:  '+ self.grupo)

        self.current = ""

        if tag == 'jogo':
            self.game = False
            if self.is_stage_final:
                self.stage_final_games.append(self.gameinfo)

            if self.is_stage_group:
                self.stage_group_games.append(self.gameinfo)


        if tag == 'fase_de_grupos':
            self.is_stage_group = False

        if tag == 'fase_final':
            self.is_stage_final = False

        if tag in self.list_game:
            self.item_game = False

    #unsort pote to put in each group
    def unsortPote(self):
         random.shuffle(self.pote2)
         random.shuffle(self.pote3)
         random.shuffle(self.pote4)


    def createGroups(self):
        self.unsortPote()

        #reverse
        self.pote1.reverse()
        #head in group
        self.groupA = [self.pote1.pop()]
        self.groupB = [self.pote1.pop()]
        self.groupC = [self.pote1.pop()]
        self.groupD = [self.pote1.pop()]
        self.groupE = [self.pote1.pop()]
        self.groupF = [self.pote1.pop()]
        self.groupG = [self.pote1.pop()]
        self.groupH = [self.pote1.pop()]


        for aux in range(1):
            try:
                self.groupA.append(self.pote2.pop())
                self.groupA.append(self.pote3.pop())
                self.groupA.append(self.pote4.pop())

                self.groupB.append(self.pote2.pop())
                self.groupB.append(self.pote3.pop())
                self.groupB.append(self.pote4.pop())

                self.groupC.append(self.pote2.pop())
                self.groupC.append(self.pote3.pop())
                self.groupC.append(self.pote4.pop())

                self.groupD.append(self.pote2.pop())
                self.groupD.append(self.pote3.pop())
                self.groupD.append(self.pote4.pop())

                self.groupE.append(self.pote2.pop())
                self.groupE.append(self.pote3.pop())
                self.groupE.append(self.pote4.pop())

                self.groupF.append(self.pote2.pop())
                self.groupF.append(self.pote3.pop())
                self.groupF.append(self.pote4.pop())

                self.groupG.append(self.pote2.pop())
                self.groupG.append(self.pote3.pop())
                self.groupG.append(self.pote4.pop())

                self.groupH.append(self.pote2.pop())
                self.groupH.append(self.pote3.pop())
                self.groupH.append(self.pote4.pop())

                #create group A
                gA = Group("A")
                gA.setGroup(self.groupA)
                listGA = self.stage_group_games[0:6]

                self.finals.setA(gA.createGames(listGA))

                #create group B
                gB = Group("B")
                gB.setGroup(self.groupB)
                listGB = self.stage_group_games[6:12]


                self.finals.setB(gB.createGames(listGB))

                #create group C
                gC = Group("C")
                gC.setGroup(self.groupC)
                listGC = self.stage_group_games[12:18]

                self.finals.setC(gC.createGames(listGC))

                #create group D
                gD = Group("D")
                gD.setGroup(self.groupD)
                listGD = self.stage_group_games[18:24]

                self.finals.setD(gD.createGames(listGD))

                #create group E
                gE = Group("E")
                gE.setGroup(self.groupE)
                listGE = self.stage_group_games[24:30]

                self.finals.setE(gE.createGames(listGE))

                #create group F
                gF = Group("F")
                gF.setGroup(self.groupF)

                listGF = self.stage_group_games[30:36]

                self.finals.setF(gF.createGames(listGF))

                #create group G
                gG = Group("G")
                gG.setGroup(self.groupG)
                listGG = self.stage_group_games[36:42]


                self.finals.setG(gG.createGames(listGG))

                #create group H
                gH = Group("H")
                gH.setGroup(self.groupH)
                listGH = self.stage_group_games[42:48]

                self.finals.setH(gH.createGames(listGH))

                #to pass list gamesfinals
                self.finals.setFinalGames(self.stage_final_games)

                self.finals.oitavas()

                self.finals.quartas()

                self.finals.semi()

                self.finals.final()

                self.finals.theBest()

            except IndexError:
                print("Erro: ", IndexError.__traceback__)
                print (aux)

#create an xmlReader
try:
    parser = xml.sax.make_parser()

    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = Game()

    parser.setContentHandler(handler)

    parser.parse("copa_do_mundo.xml")

    handler.createGroups()
except NameError:
    print(NameError)

