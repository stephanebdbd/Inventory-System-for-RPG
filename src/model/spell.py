
class Spell:
    
    def __init__(self, spell_id: str, name, cost, coolDown, power):
        self.spell_id = spell_id
        self.name = name
        self.cost = cost   #  cout en mana   voir fichier csv sorts
        self.coolDown = coolDown
        self.power = power

    def getSpell_id(self):
        return self.spell_id
    
    def getSpellName(self):
        return self.name
    
    def getCost(self):
        return self.cost
    
    def getCoolDown(self):
        return self.coolDown
    
    def getPower(self):
        return self.power