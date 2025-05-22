from character_class import CharClass
from player import Player


class Character:

    def __init__(self, name, charClass, lifePoints, mana, strength, intelligence, agility, playerUser):
        self.name = name
        self.lifePoints = lifePoints
        self.mana =  mana  # c est quoi ?
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.level = 0

        if not isinstance(charClass, CharClass):
            raise TypeError(charClass, "not a CharClass instance")
        
        if not isinstance(playerUser, Player):
            raise TypeError(playerUser, "not a Player instance")
        
        self.charClass = charClass
        self.playerUser = playerUser.getPlayerUsername()


    def getCharName(self):
        return self.name
    
    def getCharLifePoints(self):
        return self.lifePoints
    
    def getCharStrength(self):
        return self.strength
    
    def getCharAgility(self):
        return self.agility
    
    def getCharIntelligence(self):
        return self.intelligence
    
    def getCharMana(self):
        return self.mana
    
    def getPlayerUser(self):
        return self.playerUser
    
    def getCharLevel(self):
        return self.level
    
    
    def setCharName(self, newName):
        self.name = newName

    def setCharLifePoints(self, newLifePoints):
        self.lifePoints = newLifePoints
    
    def setCharStrength(self, newStrength):
        self.strength = newStrength
    
    def setCharAgility(self, newAgility):
        self.agility = newAgility
    
    def setCharIntelligence(self, newIntelligence):
        self.intelligence = newIntelligence
    
    def setCharMana(self, newMana):
        self.mana = newMana


    def levelUp(self):
        self.level += 1

    