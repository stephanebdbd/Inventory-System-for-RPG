import uuid
from item import Item

class Inventory:
    def __init__(self, equipedItems: list[Item] ):
        self.inventoryId = uuid.uuid4()
        self.equipedItems = equipedItems


    def getInventoryId(self):
        return self.inventoryId


    def getEquipedItems(self):
        return self.equipedItems
    
    def getEquipedItemsSize(self):
        return len(self.equipedItems)
    

    def addItem(self, item: Item):
        self.equipedItems.append(item)
    

    def showItemsList(self):
        if len(self.equipedItems) == 0:
            print("Empty Inventory")
        else:
            for item in self.equipedItems:
                print(item.getItemName(), end=" ")