class Menu:
    def __init__(self, name, sons):
        self.meMenu = name
        self.mySons = sons

    def getSons(self):
        return self.mySons
    
    def getMenu(self):
        return self.meMenu
        