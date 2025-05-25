CREATE TABLE IF NOT EXISTS Butin (
    id INT AUTO_INCREMENT PRIMARY KEY,
   
    objet_id INT,
     monstre_id INT,
    FOREIGN KEY (monstre_id) REFERENCES Monstre(id),
    FOREIGN KEY (objet_id) REFERENCES Objet(ObjetID)
);
