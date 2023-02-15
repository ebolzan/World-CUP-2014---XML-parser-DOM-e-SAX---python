# -*- coding: utf-8 -*-
#*-* coding: latin-1 *-*

import json

class HistoryGames:
    
    _instance = None

    def __init__(self) -> None:
        self.historyList = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        
        return cls._instance

    def addGame(self, value):
        self.historyList.append(value)
    
    def printS(self) -> None:
        i = 0
        for gameGroup in self.historyList:
            print(i, "\t \t ",gameGroup)
            i+=1

    def toJson(self):
        jsonString = json.dumps(self.historyList, cls=GameEncoder,  ensure_ascii=False)
        return(jsonString)
    
    def saveJsonInFile(self, filePath="frontend/index.html"):

        try:
            filedata = ""

            with open(filePath, 'r', encoding="utf-8") as file :
                filedata = file.read()
            javascript = "const games = "
            javascript += self.toJson()

            output = filedata.replace("#campion1", javascript)

            with open(filePath, "w", encoding="utf-8") as outfile:
                outfile.write(output)
        except Exception as ex:
            print(ex)
                
    
class Games:
    def __init__(self, faseGame, infoGeneral, teamA, TeamB, resultA, resultB) -> None:
        self.faseGame = faseGame
        self.infoGeneral = infoGeneral
        self.teamA = teamA
        self.teamB = TeamB
        self.resultA = resultA
        self.resultB = resultB
    

    def formatJson(self):
        stringOut =  "fase: {}, datetime: {}, timeA: {}, timeB: {}, resultA: {}, resultB: {}".format(self.faseGame, self.infoGeneral, self.teamA, self.teamB, self.resultA, self.resultB)
        return stringOut

    def __str__(self) -> str:
        return (self.infoGeneral.__str__())

    
class GameEncoder(json.JSONEncoder):
    def default(self, ob):
        if isinstance(ob, Games):
            return ob.formatJson()
        else:
            json.JSONEncoder.default(self, ob)
