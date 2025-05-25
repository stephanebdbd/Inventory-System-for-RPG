CREATE TABLE IF NOT EXISTS PNJ (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,  -- Name of the NPC
    lieu VARCHAR(100)           -- Their location (optional)
);
