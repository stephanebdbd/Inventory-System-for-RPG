DROP TABLE IF EXISTS Inventaire;

CREATE TABLE IF NOT EXISTS Inventaire (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pnj_id INT,
    objet_id INT,
    quantite INT DEFAULT 1,
    AmountSlots INT DEFAULT 0,
    FOREIGN KEY (pnj_id) REFERENCES PNJ(id),
    FOREIGN KEY (objet_id) REFERENCES Objet(ObjetID)
);
