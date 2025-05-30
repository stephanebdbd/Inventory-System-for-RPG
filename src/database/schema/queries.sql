--TOPGOLD
SELECT Username, MoneyGold
FROM Player
ORDER BY MoneyGold DESC
LIMIT 10;

--RANK1
SELECT j.Username, p.Class, COUNT(*) AS total
FROM Player j
JOIN Character p ON j.Username = p.Username
GROUP BY j.Username, p.Class
ORDER BY total DESC
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

--add_player
INSERT INTO Player (Username, Password) 
VALUES (%s, %s);

--login_player
SELECT PlayerID, Username, Level, Experience, MoneyGold 
FROM Player 
WHERE Username = %s AND Password = %s;

--get_characters

--add_character

--edit_character

--get_stats

--get_all_items

--get_character_inventory

--get_monsters

--get_monster_loot

--get_quests

