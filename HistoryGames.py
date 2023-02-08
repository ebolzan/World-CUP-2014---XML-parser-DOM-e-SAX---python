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
    
    def saveJsonInFile(self, filePath="outfile.json"):

        try:
            with open(filePath, "w") as outfile:
                outfile.write(self.toJson())
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
        stringOut =  "fase: {}, datetime: {}, timeA: {}, timeB: {}".format(self.faseGame, self.infoGeneral, self.teamA, self.teamB)
        return stringOut

    def __str__(self) -> str:
        return (self.infoGeneral.__str__())

    
class GameEncoder(json.JSONEncoder):
    def default(self, ob):
        if isinstance(ob, Games):
            return ob.formatJson()
        else:
            json.JSONEncoder.default(self, ob)
