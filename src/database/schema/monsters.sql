CREATE TABLE IF NOT EXISTS Monster (
    MonsterID   INT PRIMARY KEY,
    MonsterName VARCHAR(100) NOT NULL,
    Attack      INT NOT NULL DEFAULT 10,
    Defense     INT NOT NULL DEFAULT 10,
    LifePoints  INT NOT NULL DEFAULT 100
);

CREATE TABLE IF NOT EXISTS MonsterLoot (
    LootID          INT AUTO_INCREMENT PRIMARY KEY,
    MonsterID       INT NOT NULL,
    GoldQuantity    INT NOT NULL DEFAULT 0,
    GoldProbability INT NOT NULL DEFAULT 0,
    FOREIGN KEY (MonsterID) REFERENCES Monster(MonsterID)
);

CREATE TABLE IF NOT EXISTS ItemDropped (
    LootID      INT NOT NULL,
    ItemID      INT NOT NULL,
    Probability INT NOT NULL DEFAULT 0,
    AmountItem  INT NOT NULL DEFAULT 1,

    PRIMARY KEY (LootID, ItemID),
    FOREIGN KEY (ItemID) REFERENCES Item(ItemID),
    FOREIGN KEY (LootID) REFERENCES MonsterLoot(LootID)
);