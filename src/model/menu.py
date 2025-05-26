class Menu:
    def __init__(self, name, sons = None):
        self.meMenu = name
        self.mySons = sons

    def getSons(self):
        return self.mySons
    
    def getMenu(self):
        return self.meMenu
        
    def setSons(self, sons):
        self.mySons = sons