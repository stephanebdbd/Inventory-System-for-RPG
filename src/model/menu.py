class Menu:
    def __init__(self, title, sons = None):
        self.meMenu = title
        self.mySons = sons

    def getSons(self):
        return self.mySons
    
    def getTitle(self):
        return self.meMenu
        
    def setSons(self, sons):
        self.mySons = sons