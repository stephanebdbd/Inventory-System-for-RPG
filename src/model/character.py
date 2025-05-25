from character_class import Class
from player import Player
from inventory import Inventory
import uuid



class Character:

    def __init__(self, name: str, char_class: Class, lifePoints: int, mana: int, strength: int, intelligence: int, agility: int, playerUser: Player):
        self.characterId = uuid.uuid4()
        self.name = name
        self.lifePoints = lifePoints
        self.mana =  mana  # c est quoi ?
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.level = 0

        if not isinstance(char_class, Class):
            raise TypeError(charClass, "not a CharClass instance")
        
        if not isinstance(playerUser, Player):
            raise TypeError(playerUser, "not a Player instance")
        
        self.Class = char_class
        self.playerUsername = playerUser.getPlayerUsername()
        self.inventory = Inventory()  #chaque personnage a un inventaire


    def getName(self):
        return self.name
    
    def getLifePoints(self):
        return self.lifePoints
     
    def getStrength(self):
        return self.strength
    
    def getAgility(self):
        return self.agility
    
    def getIntelligence(self):
        return self.intelligence
    
    def getMana(self):
        return self.mana
    
    def getPlayerUser(self):
        return self.playerUsername
    
    def getLevel(self):
        return self.level
    
    
    def setName(self, newName):
        self.name = newName

    def setLifePoints(self, newLifePoints):
        self.lifePoints = newLifePoints
    
    def setStrength(self, newStrength):
        self.strength = newStrength
    
    def setAgility(self, newAgility):
        self.agility = newAgility
    
    def setIntelligence(self, newIntelligence):
        self.intelligence = newIntelligence
    
    def setMana(self, newMana):
        self.mana = newMana


    def levelUp(self):
        self.level += 1


