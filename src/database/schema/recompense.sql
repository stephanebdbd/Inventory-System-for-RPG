CREATE TABLE IF NOT EXISTS Recompense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quete_id INT,
    objet_id INT,
    FOREIGN KEY (quete_id) REFERENCES Quete(id),
    FOREIGN KEY (objet_id) REFERENCES Objet(ObjetID)
);
