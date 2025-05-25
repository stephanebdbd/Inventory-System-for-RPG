CREATE TABLE IF NOT EXISTS Battle (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    PlayerID INT,
    MonsterID INT,
    Result VARCHAR(10),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (MonsterID) REFERENCES Monstre(id)
);

-- Juve is a finished club