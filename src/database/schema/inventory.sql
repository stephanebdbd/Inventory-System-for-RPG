DROP TABLE IF EXISTS Inventory;

-- parent class of inventories
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY UNIQUE
);

CREATE TABLE IF NOT EXISTS CharacterInventory (
    InventoryID INT NOT NULL,
    CharID      INT NOT NULL,
    AmountSlots INT DEFAULT 0,

    PRIMARY KEY (CharID, InventoryID),
    FOREIGN KEY (InventoryID)   REFERENCES Inventory(InventoryID),
    FOREIGN KEY (CharID)        REFERENCES Characters(CharID)
);

CREATE TABLE IF NOT EXISTS NPCInventory (
    InventoryID INT NOT NULL,
    npcID       INT NOT NULL,

    PRIMARY KEY (InventoryID, npcID),
    FOREIGN KEY (InventoryID)   REFERENCES Inventory(InventoryID),
    FOREIGN KEY (npcID)         REFERENCES NPC(npcID)
);

CREATE TABLE IF NOT EXISTS InventoryItem (
    InventoryID INT NOT NULL,
    ItemID      INT NOT NULL,
    AmountItem  INT NOT NULL DEFAULT 1,

    PRIMARY KEY (InventoryID, ItemID),
    FOREIGN KEY (InventoryID)   REFERENCES Inventory(InventoryID),
    FOREIGN KEY (ItemID)        REFERENCES Item(ItemID)
);