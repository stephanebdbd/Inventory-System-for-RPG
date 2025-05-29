CREATE TABLE IF NOT EXISTS Quests (
    QuestID             INT AUTO_INCREMENT PRIMARY KEY,
    Descriptions         TEXT NOT NULL,
    QuestName           VARCHAR(50) NOT NULL,
    RewardID            INT NOT NULL,
    niveau_difficulte   INT DEFAULT 1,

    FOREIGN KEY (RewardID) REFERENCES Rewards(RewardID)
);

CREATE TABLE IF NOT EXISTS NPCQuest (
    npcID   INT NOT NULL,
    QuestID INT NOT NULL,

    PRIMARY KEY (npcID, QuestID),
    FOREIGN KEY (npcID)     REFERENCES NPC(npcID),
    FOREIGN KEY (QuestID)   REFERENCES Quests(QuestID)

);



CREATE TABLE IF NOT EXISTS ItemReward (
    ItemID      INT NOT NULL,
    RewardID    INT NOT NULL,

    PRIMARY KEY (ItemID, RewardID),
    FOREIGN KEY (ItemID)    REFERENCES Item(ItemID),
    FOREIGN KEY (RewardID)  REFERENCES Rewards(RewardID)
)