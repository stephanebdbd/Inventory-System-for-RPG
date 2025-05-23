CREATE TABLE IF NOT EXISTS Quete (
    id INT AUTO_INCREMENT PRIMARY KEY,--each quest will take a unique ID (1,2,3...)
    nom_quete VARCHAR(100) NOT NULL,--the name of the quest
    niveau_difficulte INT NOT NULL,--
    or_recompense INT NOT NULL--the amount of gold 
);
