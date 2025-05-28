CREATE TABLE IF NOT EXISTS Monster (
    MonsterID   INT PRIMARY KEY NOT NULL,
    MonsterName VARCHAR(100) NOT NULL,
    Attack      INT DEFAULT 10,
    Defense     INT DEFAULT 10
    LifePoints  INT DEFAULT 100
);

CREATE TABLE IF NOT EXISTS MonsterLoot (
    LootID          INT AUTO_INCREMENT PRIMARY KEY,
    MonsterID       INT NOT NULL,
    GoldQuantity    INT DEFAULT 0,
    GoldProbability INT DEFAULT 0,

    FOREIGN KEY (MonsterID) REFERENCES Monster(MonsterID)
);

CREATE TABLE IF NOT EXISTS ItemsDropped (
    LootID      INT NOT NULL,
    ItemID      INT NOT NULL,
    Probability INT DEFAULT 0,
    AmountItem  INT DEFAULT 1 NOT NULL,

    PRIMARY KEY (LootID, ItemID),
    FOREIGN KEY (ItemID) REFERENCES Item(ItemID),
    FOREIGN KEY (LootID) REFERENCES MonsterLoot(LootID)
)