import uuid
from item import Item


class Inventory:
    def __init__(self):
        self.inventoryId = uuid.uuid4()
        self.equipedItems = []

    def getInventoryId(self):
        return self.inventoryId


    def getEquipedItems(self):
        return self.equipedItems
    
    def getEquipedItemsSize(self):
        return len(self.equipedItems)
    
    
    def addItem(self, item: Item):
        pass
    
    
    def showItemsList(self):
        if len(self.equipedItems) == 0:
            print("Empty Inventory")
        else:
            for item in self.equipedItems:
                print(item.getItemName(), end=" ")
