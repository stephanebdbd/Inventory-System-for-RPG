CREATE TABLE IF NOT EXISTS Monster (
    MonsterID INT PRIMARY KEY NOT NULL,
    Attack INT DEFAULT 10,
    Defense INT DEFAULT 10
    MonsterName VARCHAR(100) NOT NULL,
    LifePoints INT DEFAULT 100,
    DropedID INT NOT NULL,
    FOREIGN KEY (DropedID) REFERENCES RewardDroped(DropedID)
);

CREATE TABLE IF NOT EXISTS RewardDroped(
    DropedID INT AUTO_INCREMENT PRIMARY KEY,
    MonsterID INT NOT NULL,
    GoldQuantity INT DEFAULT 0,
    GoldProbability INT DEFAULT 0,
    --items & probability
);