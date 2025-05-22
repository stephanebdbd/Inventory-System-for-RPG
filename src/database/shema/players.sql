CREATE TABLE Player(
    PlayerID    INT PRIMARY KEY AUTO_INCREMENT,
    Username    VARCHAR(50)     NOT NULL UNIQUE,
    Exp         INT DEFAULT 0,
    Gold        INT DEFAULT 0,
    level INT DEFAULT 0,
);

CREATE TABLE Class(
    Name    VARCHAR(50)     NOT NULL,
);