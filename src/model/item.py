import uuid

"""
Represente un objet (classe parente)
"""
class Item:

    def __init__(self, name: str, itemType: str, itemProperties: str, price: int):
        self.itemId = uuid.uuid4()
        self.name = name
        self.itemType = itemType
        self.itemProperties = itemProperties
        self.price = price

    def getItemId(self):
        return self.itemId
    
    def getItemName(self):
        return self.name
    
    def getItemType(self):
        return self.itemType
    
    def getItemProperties(self):
        return self.itemProperties
    
    def getItemPrice(self):
        return self.price


"""---------------------------- Weapon --------------------------------------------"""

class Weapon(Item):
    def __init__(self, name, itemType, itemProperties, price, attackPower: int):
        super().__init__(name, itemType, itemProperties, price)
        self.itempType = "Arme"
        self.attackPower = attackPower

    def getAttackPower(self):
        return self.attackPower
    




"""---------------------------- Armor--------------------------------------------"""

class Armor(Item):
    def __init__(self, name, itemType, itemProperties, price, defense: int):
        super().__init__(name, itemType, itemProperties, price)
        self.itemType = "Armure"
        self.defense = defense

    
    def getDefense(self):
        return self.defense





"""---------------------------- Potion--------------------------------------------"""

class Potion(Item):
    def __init__(self, name, itemType, itemProperties, price, healing: int):
        super().__init__(name, itemType, itemProperties, price)
        self.itemType = "Potion"
        self.healing = healing


    def getHealing(self):
        return self.healing

    



"""---------------------------- artefact --------------------------------------------"""
class Artefact(Item):
    def __init__(self, name, itemType, itemProperties, price, effectDescription: str):
        super().__init__(name, itemType, itemProperties, price)
        self.itemType = "Artefact"
        self.effectDescription = effectDescription      #      !!!!  effectDescription = itemProperties voir fichier csv

    
    def getEffectDescription(self):
        return self.effectDescription

    
