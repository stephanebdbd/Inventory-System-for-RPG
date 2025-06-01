USE rpg;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS CharacterSpells;
DROP TABLE IF EXISTS CharactersInventory;
DROP TABLE IF EXISTS PlayersBattle;
DROP TABLE IF EXISTS MonstersBattle;
DROP TABLE IF EXISTS NPCQuest;

DROP TABLE IF EXISTS InventoryItem;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Battle;
DROP TABLE IF EXISTS Characters;
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Quest;
DROP TABLE IF EXISTS Reward;
DROP TABLE IF EXISTS ItemDropped;
DROP TABLE IF EXISTS ItemReward;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS MonsterLoot;
DROP TABLE IF EXISTS Monster;
DROP TABLE IF EXISTS NPCInventory;
DROP TABLE IF EXISTS NPC;
DROP TABLE IF EXISTS Spell;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Armor;
DROP TABLE IF EXISTS Potion;
DROP TABLE IF EXISTS Weapon;
SET FOREIGN_KEY_CHECKS = 1;


SOURCE src/database/schema/players.sql;
SOURCE src/database/schema/class.sql;
SOURCE src/database/schema/items.sql;
SOURCE src/database/schema/rewards.sql;
SOURCE src/database/schema/monsters.sql;
SOURCE src/database/schema/spells.sql;
SOURCE src/database/schema/quests.sql;
SOURCE src/database/schema/npcs.sql;
SOURCE src/database/schema/battles.sql;
SOURCE src/database/schema/characters.sql;
SOURCE src/database/schema/inventory.sql;
