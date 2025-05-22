from spell import Spell
    

"""
Represente une classe de personnage
- contient un certain nombre de sorts
"""
class CharClass:

    def __init__(self, name, spellList: list[Spell]):
        self.name = name
        self.spellList = spellList     #  une class peut detenir 0 à n spell

        for i in spellList:
            if not isinstance(i , Spell):
                raise Exception(i, " not a Spell instance")

    
    def getClassName(self):
        return self.name
    

    def getSpellList(self):
        return self.spellList
    