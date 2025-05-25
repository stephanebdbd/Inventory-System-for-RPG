CREATE TABLE IF NOT EXISTS Quests (
    QuestID INT AUTO_INCREMENT PRIMARY KEY,
    Description TEXT NOT NULL,
    QuestName VARCHAR(50) NOT NULL,
    RewardID INT NOT NULL,

    FOREIGN KEY (RewardID) REFERENCES Reward(RewardID)
);

CREATE TABLE IF NOT EXISTS Reward (
    RewardID INT AUTO_INCREMENT PRIMARY KEY,
    GoldQuantity INT DEFAULT 0,
    Experience INT DEFAULT 0,
    -- plusieurs items
);