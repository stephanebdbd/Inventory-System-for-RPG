CREATE TABLE IF NOT EXISTS Characters (
    CharID          INT PRIMARY KEY AUTO_INCREMENT,
    PlayerID        INT NOT NULL,
    Name            VARCHAR(15) NOT NULL,
    ClassName       VARCHAR(50) NOT NULL,
    LifePoints      INT DEFAULT 0,
    Mana            INT DEFAULT 0,
    Strength        INT DEFAULT 0,
    Intelligence    INT DEFAULT 0,
    Agility         INT DEFAULT 0,
    Gold            INT DEFAULT 0,
    userName        VARCHAR(25) NOT NULL,
    FOREIGN KEY (PlayerID)  REFERENCES Player(PlayerID),
    FOREIGN KEY (ClassName) REFERENCES Class(ClassName)
);


CREATE TABLE IF NOT EXISTS Spell (
    SpellID     INT PRIMARY KEY AUTO_INCREMENT,
    SpellName   VARCHAR(25) NOT NULL,
    ManaCost    INT DEFAULT 0,
    LoadingTime INT DEFAULT 0,
    AttackPower INT DEFAULT 0
);


CREATE TABLE IF NOT EXISTS PlayerSpell (
    SpellID     INT NOT NULL,
    PlayerID    INT NOT NULL,

    PRIMARY KEY (SpellID, PlayerID),
    FOREIGN KEY (SpellID)   REFERENCES Spell(SpellID),
    FOREIGN KEY (PlayerID)  REFERENCES Player(PlayerID)
);