import uuid
from inventory import Inventory
from quest import Quest
from character import Character


class NPC:

    def __init__(self, name: str, dialogue: str, inventory: Inventory, quest: Quest):
        self.npcId = uuid.uuid4()
        self.name = name
        self.dialogue = dialogue
        
        if not isinstance(inventory, Inventory):
            raise TypeError(inventory, "not a Inventory instance")
        
        if not isinstance(quest, Quest):
            raise TypeError(quest, "not a Quest instance")

        self.inventory = inventory   #  Instance de Inventory ou pas ????
        self.quest = quest


    def getId(self):
        return self.npcId

    def getName(self):
        return self.name
    

    def getDialogue(self):
        return self.dialogue
    

    def getInventory(self):
        return self.inventory
    

    """
    def proposeQuest(self, character: Character) ????


    def tradeItem(self, character: Character)
    
    """