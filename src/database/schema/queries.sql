--add_artefact
INSERT IGNORE INTO Artefact (ItemID, Effect)
VALUES (%s, %s);

--add_armor
INSERT IGNORE INTO Armor (ItemID, Defense, Effect)
VALUES (%s, %s, %s);

--add_character
INSERT INTO Characters (Username, Name, Class, LifePoints, Mana, Strength, Intelligence, Agility)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);

--add_character
INSERT INTO Characters (Name, Class, LifePoints, Mana, Strength, Intelligence, Agility, Username)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);

--add_class
INSERT IGNORE INTO Class (Name)
VALUES (%s);

--add_inventory
INSERT INTO Inventory () VALUES ();

--add_inventory_item
INSERT IGNORE INTO InventoryItem (InventoryID, ItemID, AmountItem)
VALUES (%s, %s, %s);

--delete_inventory_item
DELETE FROM InventoryItem
Where InventoryID = %s AND ItemID = %s;


--add_item
INSERT IGNORE INTO Item (Name, Type, Price)
VALUES (%s, %s, %s);

--add_item_reward
INSERT INTO ItemReward (ItemID, RewardID)
VALUES (%s, %s);

--add_item_dropped
INSERT INTO ItemDropped (LootID, ItemID, Probability, AmountItem)
VALUES (%s, %s, %s, %s)

--add_monster
INSERT INTO Monster (MonsterID, MonsterName, Attack, Defense, LifePoints)
VALUES (%s, %s, %s, %s, %s);

--add_monster_loot
INSERT INTO MonsterLoot (MonsterID, GoldQuantity, GoldProbability)
VALUES (%s, %s, %s);

--add_npc
INSERT INTO NPC (npcName, npcDialogue)
VALUES (%s, %s);

--add_npc_inventory
INSERT INTO NPCInventory (InventoryID, npcID)
VALUES (%s, %s);

--add_npc_quest
INSERT IGNORE INTO NPCQuest (npcID, QuestID)
VALUES (%s, %s);

--add_player
INSERT IGNORE INTO Player (Username, Level, Experience, MoneyGold, InventorySlots)
VALUES (%s, %s, %s, %s, %s);

--add_potion
INSERT IGNORE INTO Potion (ItemID, Healing, Effect)
VALUES (%s, %s, %s);

--add_quest
INSERT INTO Quest (Description, Difficulty, Exp, QuestName, RewardID)
VALUES (%s, %s, %s, %s, %s);

--add_reward
INSERT INTO Reward (GoldQuantity)
VALUES (%s);

--add_spell
INSERT INTO Spell (SpellID, SpellName, ManaCost, Cooldown, AttackPower, ClassName)
VALUES (%s, %s, %s, %s, %s, %s);

--add_weapon
INSERT IGNORE INTO Weapon (ItemID, AttackPower, Effect)
VALUES (%s, %s, %s);

--check_login_player
SELECT PlayerID
FROM Player 
WHERE Username = %s AND Password = %s;

--check_username
SELECT 1
FROM Player
WHERE Username = %s;

--edit_character
UPDATE Characters
SET LifePoints = %s,
    Mana = %s,
    Strength = %s,
    Intelligence = %s,
    Agility = %s
WHERE CharID = %s;

--find_item_id
SELECT ItemID
FROM Item
WHERE Name = %s;

--find_quest_id
SELECT QuestID
FROM Quest
WHERE QuestName = %s;

--get_all_classes
SELECT Name
FROM Class

--get_player
SELECT Username, Password, Level, Username,Experience, MoneyGold, InventorySlots
FROM Player
WHERE Username = %s

--get_all_items
SELECT i.Name, i.Price,
  CASE 
    WHEN w.ItemID IS NOT NULL THEN 'Weapon'
    WHEN a.ItemID IS NOT NULL THEN 'Armor'
    WHEN p.ItemID IS NOT NULL THEN 'Potion'
    WHEN ar.ItemID IS NOT NULL THEN 'Artefact'
    ELSE 'Other'
  END AS ItemType
FROM Item i
LEFT JOIN Weapon w ON i.ItemID = w.ItemID
LEFT JOIN Armor a ON i.ItemID = a.ItemID
LEFT JOIN Potion p ON i.ItemID = p.ItemID
LEFT JOIN Artefact ar ON i.ItemID = ar.ItemID;

--get_character_inventory
SELECT InventoryID 
FROM Inventory 
WHERE CharID = %s;

--get_characters
SELECT Name ,CharID, Class
From Characters
WHERE Username = %s;

--get_item
SELECT Name
From Item
WHERE ItemID = %s;

--get_itemID
SELECT ItemID, 
FROM Item 
WHERE Name = %s

--get_monster_loot
SELECT LootID, GoldQuantity, GoldProbability
FROM MonsterLoot
WHERE MonsterID = %s;

--get_all_npc
SELECT npcID, npcName, npcDialogue
FROM NPC;

--get_monster_items
SELECT
    id.ItemID,
    i.Name      AS ItemName,
    id.Probability,
    id.AmountItem
FROM ItemDropped AS id
JOIN Item AS i ON id.ItemID = i.ItemID
WHERE id.LootID = %s;


--get_monsters
SELECT MonsterName, MonsterID, Attack, LifePoints, Defense
FROM Monster;

--get_quests
SELECT QuestName
FROM Quest;

--get_quests_by_npc
SELECT q.QuestID     AS QuestID,
       q.QuestName   AS QuestTitle,
       q.Description AS Description,
       q.Difficulty  AS Difficulty,
       q.Exp         AS Exp
FROM Quest q
JOIN NPCQuest nq ON q.QuestID = nq.QuestID
JOIN NPC n       ON nq.npcID = n.npcID
WHERE n.npcName = %s
ORDER BY q.QuestName;


--get_all_npc_and_quests
SELECT Quest.QuestID, Quest.QuestName, Quest.Description, Quest.RewardXP, Quest.RewardGold
FROM NPC
JOIN NPCQuest ON NPC.npcID = NPCQuest.npcID
JOIN Quest ON NPCQuest.QuestID = Quest.QuestID
WHERE NPC.npcName = ?;

--get_stats
SELECT LifePoints,Mana, Strength,Intelligence,Agility 
FROM Characters
WHERE CharID = %s;

--register_player
INSERT INTO Player (Username, Password) 
VALUES (%s, %s);

--RANK1
SELECT j.Username, p.Class, COUNT(*) AS total
FROM Player j
JOIN Characters p ON j.Username = p.Username
GROUP BY j.Username, p.Class
ORDER BY total DESC
LIMIT 1;

--TOPGOLD
SELECT Username, MoneyGold
FROM Player
ORDER BY MoneyGold DESC
LIMIT 10;

--TOPITEM
SELECT
    CASE
        WHEN w.ItemID IS NOT NULL THEN 'Weapon'
        WHEN a.ItemID IS NOT NULL THEN 'Armor'
        WHEN p.ItemID IS NOT NULL THEN 'Potion'
        WHEN ar.ItemID IS NOT NULL THEN 'Artefact'
        ELSE 'Unknown'
    END AS type_objet,
    COUNT(*) AS nombre
FROM Quest q
JOIN Reward r ON q.RewardID = r.RewardID
JOIN ItemReward ir ON r.RewardID = ir.RewardID
JOIN Item i ON ir.ItemID = i.ItemID
LEFT JOIN Weapon w ON i.ItemID = w.ItemID
LEFT JOIN Armor a ON i.ItemID = a.ItemID
LEFT JOIN Potion p ON i.ItemID = p.ItemID
LEFT JOIN Artefact ar ON i.ItemID = ar.ItemID
WHERE q.Difficulty = 5
GROUP BY type_objet
ORDER BY nombre DESC
LIMIT 1;

--TOPMONSTER
SELECT 
    m.MonsterName, 
    m.LifePoints, 
    SUM(i.Price * id.AmountItem) AS total_loot_value
FROM Monster m
JOIN MonsterLoot ml ON m.MonsterID = ml.MonsterID
JOIN ItemDropped id ON ml.LootID = id.LootID
JOIN Item i ON id.ItemID = i.ItemID
GROUP BY m.MonsterID
ORDER BY total_loot_value DESC;

--TOPPNJ
SELECT 
    npc.npcName,
    SUM(it.Price * ii.AmountItem) AS valeur_totale
FROM NPC npc
JOIN NPCInventory ni ON npc.npcID = ni.npcID
JOIN InventoryItem ii ON ni.InventoryID = ii.InventoryID
JOIN Item it ON ii.ItemID = it.ItemID
GROUP BY npc.npcID
ORDER BY valeur_totale DESC
LIMIT 1;

--TOPQUEST
SELECT 
    q.QuestName, 
    q.Difficulty,
    r.GoldQuantity
FROM Quest q
JOIN Reward r ON q.RewardID = r.RewardID
WHERE q.Difficulty > 0
ORDER BY (r.GoldQuantity / q.Difficulty) DESC
LIMIT 1;
