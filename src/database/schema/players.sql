CREATE TABLE IF NOT EXISTS Player (
    PlayerID    INT PRIMARY KEY,
    Username    VARCHAR(50) NOT NULL UNIQUE,
    Level       INT DEFAULT 0,
    Experience  INT DEFAULT 0,
    MoneyGold   INT DEFAULT 0
);