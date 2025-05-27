DROP TABLE IF EXISTS Inventory;

CREATE TABLE IF NOT EXISTS Inventory ();
-- parent class of inventories

CREATE TABLE IF NOT EXISTS CharacterInventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    CharID INT NOT NULL,
    AmountSlots INT DEFAULT 0,
    FOREIGN KEY (CharID) REFERENCES Characters(CharID),
);

CREATE TABLE IF NOT EXISTS NPCInventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    npcID INT NOT NULL,
    FOREIGN KEY (npcID) REFERENCES NPC(npcID),
);

CREATE TABLE IF EXISTS InventoryItem ()
-- linking tables between items and individual inventories by items counted by tuples
-- as characters can possess many of a same item
