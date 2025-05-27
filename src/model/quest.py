import uuid


class Quest:
    def __init__(self, name: str, description: str, difficulty: int, experience: int, status: str):
        self.questId = uuid.uuid4()
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = status
        self.experience = experience
        #self.reward = Reward()


    def getQuestId(self):
        return self.questId
    

    def getName(self):
        return self.name
    

    def getDescription(self):
        return self.getDescription
    

    def getDifficulty(self):
        return self.difficulty
    
    def getStatus(self):
        return self.status
    

    def getExperience(self):
        return self.experience
    

    def setStatus(self, newStatus):
        self.status = newStatus

    """
    def isFinished(self) -> bool 

    """



    def __str__(self):
        return f" Quest Name: {self.name} \n Task Description: {self.description} \n Difficulty: {self.difficulty} \n  Experience needed: {self.experience}"