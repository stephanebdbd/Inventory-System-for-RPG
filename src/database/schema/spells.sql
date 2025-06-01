CREATE TABLE IF NOT EXISTS Spell (
    SpellID     INT PRIMARY KEY,
    SpellName   VARCHAR(25) NOT NULL,
    ClassName   VARCHAR(25) NOT NULL,
    ManaCost    INT NOT NULL DEFAULT 0,
    Cooldown INT NOT NULL DEFAULT 0,
    AttackPower INT NOT NULL DEFAULT 0,
    FOREIGN KEY (ClassName)     REFERENCES Class(ClassName)
);