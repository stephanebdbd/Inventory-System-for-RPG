DROP TABLE IF EXISTS Battle;

CREATE TABLE IF NOT EXISTS Battle (
    BattleID    INT PRIMARY KEY AUTO_INCREMENT,
    QuestName   VARCHAR(50),

    FOREIGN KEY (QuestName) REFERENCES Quest(QuestName)
);


CREATE TABLE IF NOT EXISTS PlayersBattle(
    PlayerID    INT NOT NULL,
    BattleID    INT NOT NULL,
    PRIMARY KEY (PlayerID, BattleID),
    FOREIGN KEY (BattleID) REFERENCES Battle(BattleID),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)
);

CREATE TABLE IF NOT EXISTS MonstersBattle (
    MonsterID   INT NOT NULL,
    BattleID    INT NOT NULL,
    PRIMARY KEY (MonsterID, BattleID),
    FOREIGN KEY (BattleID)  REFERENCES Battle(BattleID),
    FOREIGN KEY (MonsterID) REFERENCES Monster(MonsterID)
);