CREATE TABLE IF NOT EXISTS Monstre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    vie INT DEFAULT 100,
    attaque INT DEFAULT 10,
    defense INT DEFAULT 10
);
-- Table to store which monsters drop which objects
-- we will need it for query 6
CREATE TABLE IF NOT EXISTS Butin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    monstre_id INT,
    objet_id INT,
    FOREIGN KEY (monstre_id) REFERENCES Monstre(id),
    FOREIGN KEY (objet_id) REFERENCES Objet(id)
);
