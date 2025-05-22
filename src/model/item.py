import uuid

class Item:

    def __init__(self, name, price):
        self.itemId = uuid.uuid4()
        self.name = name
        self.price = price

    def getItemId(self):
        return self.itemId
    
    def getItemName(self):
        return self.name
    
    def getItemPrice(self):
        return self.price
    





    #  IMPLEMENTER LES CLASSES ENFANTS DE ITEM:   WEAPON    ARMOR      POTION   ARTEFACT