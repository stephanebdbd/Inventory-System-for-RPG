CREATE TABLE IF NOT EXISTS Quest (
    QuestID         INT AUTO_INCREMENT PRIMARY KEY,
    Descriptions    TEXT        NOT NULL,
    Difficulty      INT         NOT NULL,
    Exp             INT         NOT NULL,
    QuestName       VARCHAR(50) NOT NULL,
    RewardID        INT         NOT NULL UNIQUE,

    FOREIGN KEY (RewardID) REFERENCES Reward(RewardID)
);