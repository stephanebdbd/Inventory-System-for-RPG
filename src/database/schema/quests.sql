CREATE TABLE IF NOT EXISTS Quest (
    QuestID         INT AUTO_INCREMENT PRIMARY KEY,
    Description     TEXT        NOT NULL,
    Difficulty      INT         NOT NULL,
    Exp             INT         NOT NULL,
    QuestName       VARCHAR(100) NOT NULL,
    RewardID        INT         NOT NULL UNIQUE,

    FOREIGN KEY (RewardID) REFERENCES Reward(RewardID)
);

