import uuid




class Monster:
    def __init__(self, attack, defense, lifePoints):
        self.monsterId = uuid.uuid4()
        self.attack = attack
        self.defense = defense
        self.lifePoints = lifePoints

    
    def getMonsterId(self):
        return self.monsterId
    

    def getMonsterAttack(self):
        return self.attack
    
    def getMonsterDefense(self):
        return self.defense
    

    def getMonsterLifePoints(self):
        return self.lifePoints
    

    """
    GERER LA PARTIE AVEC LA REWARD TABLE....
    
    """
    


    

