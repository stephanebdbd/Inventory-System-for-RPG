CREATE TABLE IF NOT EXISTS Player (
    PlayerID    INT AUTO_INCREMENT PRIMARY KEY,
    Username    VARCHAR(50) NOT NULL UNIQUE,
    Password    VARCHAR(50) NOT NULL,
    Level       INT DEFAULT 0,
    Experience  INT DEFAULT 0,
    MoneyGold   INT DEFAULT 0
);