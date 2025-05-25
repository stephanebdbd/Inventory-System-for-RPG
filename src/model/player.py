

class Player:
    
    def __init__(self, playerId: int, username: str, level: int, experience: int, gold: int, slotsInventory: int ):
        self.playerId = playerId
        self.username = username
        self.experience = experience
        self.gold = gold
        self.level = level
        #self.charactersList = []   Recupérer via la db ses personnages -  un player a 1 ou plusieurs characters voir diagramme 
        self.slotsInventory = slotsInventory

        """
        for i in self.chractersList:
            if not isinstance(i, Character):
                raise Exception(" not a Character instance")
        """
    
    def getPlayerId(self):
        return self.playerId
    

    def getPlayerUsername(self):
        return self.username
    
    def getPlayerExperience(self):
        return self.experience
    
    def getPlayerLevel(self):
        return self.level
    
    def getPlayerGold(self):
        return self.gold
    
    def getPlayerSlotsInventory(self):
        return self.slotsInventory
    
    
    def getCharactersList(self):
        return self.charactersList
    

    def setPlayerUsername(self, newUsername):
        self.username = newUsername

    def setPlayerExperience(self, newExp):
        self.experience = newExp

    
    def earnGold(self, gold_earned):
        self.gold += gold_earned
    

    def levelUp(self):    # augmenter le niveau du joueur
        self.level += 1

    def expUP(self):     # augmenter l'exp du joueur
        self.experience += 1

    """
    def createCharacter(self, name, charClass, lifePoints, mana, strength, intelligence, agility):
        pass 
        
    """
