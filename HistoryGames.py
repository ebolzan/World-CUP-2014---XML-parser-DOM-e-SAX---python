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
        for gameUnit in self.historyList:
            for fase, game in gameUnit.items():
                print (game)
                
    
class Games:
    def __init__(self, faseGame, infoGeneral, teamA, TeamB, resultA, resultB) -> None:
        self.faseGame = faseGame
        self.infoGeneral = infoGeneral
        self.teamA = teamA
        self.teamB = TeamB
        self.resultA = resultA
        self.resultB = resultB

    def __str__(self) -> str:
        return (self.infoGeneral.__str__())
    

