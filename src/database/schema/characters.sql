CREATE TABLE IF NOT EXIST player(
    PlayerID
);

CREATE TABLE Character(
    CharID       INT PRIMARY KEY AUTO_INCREMENT,
    LifePoints   INT DEFAULT 0,
    Strength     INT DEFAULT 0,
    Agility      INT DEFAULT 0,
    Intelligence INT DEFAULT 0,
    Mana         INT DEFAULT 0,
    CharLevel    INT DEFAULT 0,
);

CREATE TABLE Class(
    Name    VARCHAR(50)     NOT NULL,
);