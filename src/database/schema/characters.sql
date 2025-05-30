CREATE TABLE IF NOT EXISTS Character (
    CharID          INT PRIMARY KEY AUTO_INCREMENT,
    Name            VARCHAR(15) NOT NULL,
    Class           VARCHAR(25) NOT NULL,
    LifePoints      INT NOT NULL DEFAULT 0,
    Mana            INT NOT NULL DEFAULT 0,
    Strength        INT NOT NULL DEFAULT 0,
    Intelligence    INT NOT NULL DEFAULT 0,
    Agility         INT NOT NULL DEFAULT 0,
    Username        VARCHAR(25) NOT NULL,

    FOREIGN KEY (Username)  REFERENCES Player(Username),
    FOREIGN KEY (Class)     REFERENCES Class(Name)
);

CREATE TABLE IF NOT EXISTS CharacterSpells (
    SpellID INT NOT NULL,
    CharID  INT NOT NULL,

    PRIMARY KEY (SpellID, CharID),
    FOREIGN KEY (SpellID)   REFERENCES Spell(SpellID),
    FOREIGN KEY (CharID)    REFERENCES Character(CharID)
);