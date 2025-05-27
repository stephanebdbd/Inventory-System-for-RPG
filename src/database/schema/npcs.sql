CREATE TABLE IF NOT EXISTS PNC (
    npcID INT AUTO_INCREMENT PRIMARY KEY,
    npcName VARCHAR(100) NOT NULL,  -- Name of the NPC
    dialogue VARCHAR(100)           -- Their location (optional)
    -- npc inventorys
);
