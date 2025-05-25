from spell import Spell



"""
Represente une classe de personnage
- contient certains sorts
"""

class Class:
    def __init__(self, name, spellList: list[Spell]):
        self.name = name
        self.spellList = spellList

        for i in spellList:
            if not isinstance(i, Spell):
                raise TypeError(i, " not a Spell instance")
            
        

    def getClassName(self):
        return self.name
    

    def getSpellList(self):
        return self.spellList
