from character import Character

class Player:
    
    def __init__(self, playerId: int, username: str, level: int, experience: int, gold: int, slotsInventory: int ):
        self.playerId = playerId
        self.username = username
        self.experience = experience
        self.gold = gold
        self.level = level
        self.charactersList = []   #  un player a 1 ou plusieurs characters voir diagramme  ?  est ce toujours le cas
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
    
    def getPlayerGold(self):
        return self.gold
    

    def getPlayerLevel(self):
        return self.level
    
    def getCharactersList(self):
        return self.charactersList
    

    def setPlayerUsername(self, newUsername):
        self.username = newUsername

    def setPlayerExperience(self, newExp):
        self.experience = newExp

    
    def setPlayerGold(self, newGold):
        self.gold = newGold
    

    def setPlayerLevel(self):
        self.level += 1

    
    def createCharacter(self, name, charClass, lifePoints, mana, strength, intelligence, agility):
        newCharacter = Character(name, charClass, lifePoints, mana, strength, intelligence, agility, self.username)
        self.charactersList.append(newCharacter)


    
