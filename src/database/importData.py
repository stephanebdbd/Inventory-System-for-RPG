import csv
import json
import xml.etree.ElementTree as xmlTree
import sys
import os
from db import Database

config = {
    "host":     "localhost",
    "user":     "pietro",
    "password": "YildizMyGoat1!",
    "database": "rpgg",
}

sorted_spells = {
    "Archer":        [15, 26, 34, 54, 76],
    "Assassin":      [6, 11, 66, 69, 72],
    "Barbare":       [7, 21, 27, 82, 90],
    "Berserker":     [5, 24, 38, 85, 95],
    "Chasseur":      [16, 19, 53, 63, 70],
    "Chevalier":     [10, 13, 42, 48, 99],
    "Démoniste":     [18, 30, 46, 61, 75, 32],
    "Druide":        [3, 14, 25, 55, 83],
    "Enchanteresse": [12, 40, 49, 74, 86, 94],
    "Guerrier":      [35, 41, 58, 87, 89],
    "Illusionniste": [23, 33, 52, 68, 77, 73, 93, 92],
    "Mage":          [1, 2, 4, 8, 20, 22, 29, 39, 51, 65],
    "Moine":         [57, 60, 64, 81, 97],
    "Nécromancien":  [31, 44, 46, 71, 79],
    "Paladin":       [9, 17, 36, 43, 48, 67, 99, 100],
    "Prêtresse":     [3, 45, 50, 78, 80, 99],
    "Rôdeur":        [16, 28, 53, 84, 98],
    "Sorcière":      [18, 61, 62, 66, 75, 79, 59, 91],
    "Templier":      [10, 37, 42, 47, 96],
    "Voleur":        [6, 52, 56, 84, 88]
}


def importXML(file_path: str, db: Database):
    """
    Import monsters or quests from an XML file.
    """
    tree = xmlTree.parse(file_path)
    root = tree.getroot()
    filename = os.path.basename(file_path).lower()

    if "monstres" in filename:
        for monster in root.findall("monstre"):
            try:
                monster_id   = int(monster.findtext("id") or 0)
                monster_name = monster.findtext("nom") or ""
                attack_val   = int(monster.findtext("attaque") or 0)
                defense_val  = int(monster.findtext("defense") or 0)
                life_val     = int(monster.findtext("vie") or 0)
            except ValueError as e:
                print(f"Skipping malformed monster entry ({e}): {xmlTree.tostring(monster, encoding='unicode')}")
                continue

            db.execute_query(
                "add_monster",
                (monster_id, monster_name, attack_val, defense_val, life_val)
            )

            drops_node = monster.find("drops")
            loot_id = None

            if drops_node is not None:
                gold_node = drops_node.find("Or")
                if gold_node is not None:
                    nbr  = gold_node.findtext("nombre")
                    prob = gold_node.findtext("probabilité")

                    try:
                        gold_qty = int(nbr) if nbr else 0
                    except (ValueError, TypeError):
                        gold_qty = 0

                    try:
                        gold_prob = int(prob) if prob else 0
                    except (ValueError, TypeError):
                        gold_prob = 0

                    db.execute_query(
                        "add_monster_loot",
                        (monster_id, gold_qty, gold_prob)
                    )
                    loot_id = db.cursor.lastrowid

            if drops_node is not None and loot_id is None:
                db.execute_query(
                    "add_monster_loot",
                    (monster_id, 0, 0)
                )
                loot_id = db.cursor.lastrowid

            if drops_node is not None:
                for drop_elem in drops_node:
                    tag = drop_elem.tag
                    if tag == "Or":
                        continue
                    item_name = tag.replace("_", " ")
                    item_name = item_name.replace(" d ", " d'")
                    item_name = item_name.replace(" l ", " l'")
                    if "Monture" in item_name:
                        item_name = "Monture Volante (Hippogriffe en Peluche)"

                    nbr  = drop_elem.findtext("nombre")
                    prob = drop_elem.findtext("probabilité")

                    try:
                        amount_item = int(nbr) if nbr else 1
                    except (ValueError, TypeError):
                        amount_item = 1

                    try:
                        probability = int(prob) if prob else 0
                    except (ValueError, TypeError):
                        probability = 0

                    rows = db.execute_query("get_itemID", (item_name,))
                    if not rows:
                        print(f"Item '{item_name}' not found for monster '{monster_name}' (ID {monster_id})")
                        continue
                    item_id = rows[0]["ItemID"]

                    db.execute_query(
                        "add_item_dropped",
                        (loot_id, item_id, probability, amount_item)
                    )


    elif "quetes" in filename or "quêtes" in filename:
        for quest in root.findall("quête"):
            description = quest.findtext("Descripion") or ""
            quest_name  = quest.findtext("Nom") or ""
            try:
                difficulty = int(quest.findtext("Difficulté") or 0)
            except ValueError:
                difficulty = 0
            try:
                experience = int(quest.findtext("Expérience") or 0)
            except ValueError:
                experience = 0

            gold_text = quest.findtext("Récompenses/Or")
            try:
                gold_qty = int(gold_text) if gold_text else 0
            except ValueError:
                gold_qty = 0

            reward_id = db.execute_query("add_reward", (gold_qty,))

            db.execute_query(
                "add_quest",
                (description, difficulty, experience, quest_name, reward_id)
            )

            for obj_elem in quest.findall("Récompenses/Objets"):
                item_name = (obj_elem.text or "").strip()
                if not item_name:
                    continue

                existing = db.execute_query(
                    "get_itemID",
                    (item_name,)
                )
                if existing and len(existing) > 0:
                    item_id = existing[0]["ItemID"]
                else:
                    item_id = db.execute_query(
                        "add_item",
                        (item_name, "Unknown", 0)
                    )

                db.execute_query(
                    "add_item_reward",
                    (item_id, reward_id)
                )


def importCSV(file_path: str, db: Database):
    """
    Import players, items, or spells from CSV files.
    Special handling in 'joueurs.csv': 
      - Monnaie == "NaN" → 0
      - Monnaie == "Inf" → -1
      - Blank Niveau/XP → 0
      - Use NomUtilisateur as the Username
    """
    filename = os.path.basename(file_path).lower()
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if "joueurs" in filename:
            for row in reader:
                if all(k in row for k in ["NomUtilisateur", "Niveau", "XP", "Monnaie", "SlotsInventaire"]):
                    username = row["NomUtilisateur"].strip()
                    if not username:
                        print(f"Skipping empty username row: {row}")
                        continue

                    lvl_str = row["Niveau"].strip()
                    try:
                        level = int(lvl_str) if lvl_str else 0
                    except ValueError:
                        level = 0

                    xp_str = row["XP"].strip()
                    try:
                        xp = int(xp_str) if xp_str else 0
                    except ValueError:
                        xp = 0

                    money_str = row["Monnaie"].strip().lower()
                    if money_str == "nan":
                        money = 0
                    elif money_str == "inf":
                        money = -1
                    else:
                        try:
                            money = int(float(money_str))
                        except ValueError:
                            print(f"Invalid money '{money_str}' for user '{username}', defaulting to 0.")
                            money = 0

                    slots_str = row["SlotsInventaire"].strip()
                    try:
                        inv_slots = int(slots_str) if slots_str else 20
                    except ValueError:
                        inv_slots = 20

                    try:
                        db.execute_query(
                            "add_player",
                            (username, level, xp, money, inv_slots)
                        )
                    except Exception as e:
                        print(f"Erreur lors de l'insertion du joueur '{username}': {e}")

                else:
                    print(f"Skipping incomplete player row: {row}")

        if "objets" in filename:
            for row in reader:
                if not all(k in row for k in ["Nom", "Type", "Propriétés", "Prix"]):
                    print(f"Skipping row with missing columns: {row}")
                    continue

                raw_name  = row.get("Nom")
                raw_type  = row.get("Type")
                raw_prop  = row.get("Propriétés")
                raw_price = row.get("Prix")

                if raw_price is None:
                    raw_price = raw_prop[-2:].strip()
                    raw_prop  = raw_prop[:-2].strip()

                name_val  = raw_name.strip()
                type_val  = raw_type.strip()
                prop_val  = raw_prop.strip()
                price_val = raw_price.strip()

                name_lower = name_val.lower()
                type_lower = type_val.lower()
                if name_lower in ("nom", "om") and type_lower in ("type",):
                    continue

                if not (name_val and type_val and prop_val and price_val):
                    print(f"Skipping incomplete/empty field row: {row}")
                    continue

                try:
                    price_number = int(float(price_val.replace(" ", "").replace(" ", "")))
                except ValueError:
                    print(f"Skipping item '{name_val}' due to invalid price '{price_val}'")
                    continue

                t = type_val.lower()
                if t in ("arme, sword"):
                    subtype = "arme"
                elif t in ("armure",):
                    subtype = "armure"
                elif t in ("potion", "potions"):
                    subtype = "potion"
                elif t in ("artefact",):
                    subtype = "artefact"
                else:
                    print(f"Skipping '{name_val}' because Type='{type_val}' is unrecognized")
                    continue

                item_insert_result = db.execute_query("add_item", (name_val, subtype.capitalize(), price_number))
                if item_insert_result is None:
                    continue

                try:
                    item_id = int(item_insert_result)
                except (TypeError, ValueError):
                    item_id = db.cursor.lastrowid

                if not item_id:
                    print(f"Could not obtain item_id for '{name_val}', skipping.")
                    continue

                parts = prop_val.split(":", 1)
                if len(parts) == 2:
                    key_part   = parts[0].strip().lower()
                    value_part = parts[1].strip()
                else:
                    key_part   = "effet"
                    value_part = prop_val

                numeric_stat = 0
                effect_text  = None

                if subtype == "arme":
                    if "puissance" in key_part:
                        try:
                            numeric_stat = int(value_part)
                        except ValueError:
                            print(f"Skipping invalid AttackPower '{value_part}' on '{name_val}'")
                            continue
                    else:
                        numeric_stat = 0
                        effect_text  = value_part

                    db.execute_query("add_weapon", (item_id, numeric_stat, effect_text))

                elif subtype == "armure":
                    if "défense" in key_part:
                        try:
                            numeric_stat = int(value_part)
                        except ValueError:
                            print(f"Skipping invalid Defense '{value_part}' on '{name_val}'")
                            continue
                    else:
                        numeric_stat = 0
                        effect_text  = value_part

                    db.execute_query("add_armor", (item_id, numeric_stat, effect_text))

                elif subtype == "potion":
                    if "soin" in key_part:
                        try:
                            numeric_stat = int(value_part)
                        except ValueError:
                            print(f"Skipping invalid Healing '{value_part}' on '{name_val}'")
                            continue
                    else:
                        numeric_stat = 0
                        effect_text  = value_part

                    db.execute_query("add_potion", (item_id, numeric_stat, effect_text))

                else:
                    effect_text = value_part
                    db.execute_query("add_artefact", (item_id, effect_text))

        elif "sorts" in filename:
            for row in reader:
                if all(k in row for k in ["ID", "Coût en Mana", "Temps de Recharge", "Puissance d'Attaque"]):
                    try:
                        spell_id   = int(row["ID"])
                        name       = row["Nom"].strip()
                        mana_cost  = int(row["Coût en Mana"])
                        cooldown   = int(row["Temps de Recharge"])
                        power      = int(row["Puissance d'Attaque"])
                    except ValueError as e:
                        print(f"Skipping malformed spell row ({e}): {row}")
                        continue
                    spell_class = None
                    for class_name, id_list in sorted_spells.items():
                        if spell_id in id_list:
                            spell_class = class_name
                            break
                    try:
                        db.execute_query(
                            "add_spell",
                            (spell_id, name, mana_cost, cooldown, power, spell_class)
                        )
                    except Exception as e:
                        print(f"Erreur lors de l'insertion du sort {spell_id}: {e}")
                else:
                    print(f"Skipping incomplete spell row: {row}")


def importJSON(file_path: str, db: Database):
    """
    Import characters or NPCs from JSON files.
    For each “personnage”, we:
      1) INSERT IGNORE into Class(Name) so duplicates are skipped.
      2) INSERT into Characters using the existing Player(Username) FK,
         making sure the parameter order matches the table schema exactly.
    """
    filename = os.path.basename(file_path).lower()
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        if "personnages" in filename:
            for character in data.get("personnages", []):
                req_keys = ["Nom", "Classe", "Vie", "Mana", "Force", "Intelligence", "Agilite", "utilisateur"]
                if not all(k in character for k in req_keys):
                    print(f"Skipping incomplete character entry: {character}")
                    continue

                raw_name     = character["Nom"]
                raw_class    = character["Classe"]
                raw_life     = character["Vie"]
                raw_mana     = character["Mana"]
                raw_str      = character["Force"]
                raw_intel    = character["Intelligence"]
                raw_agility  = character["Agilite"]
                raw_user     = character["utilisateur"]

                try:
                    life_val = int(raw_life)
                except (ValueError, TypeError):
                    life_val = 0

                try:
                    mana_val = int(raw_mana)
                except (ValueError, TypeError):
                    mana_val = 0

                try:
                    strength_val = int(raw_str)
                except (ValueError, TypeError):
                    strength_val = 0

                try:
                    intel_val = int(raw_intel)
                except (ValueError, TypeError):
                    intel_val = 0

                try:
                    agility_val = int(raw_agility)
                except (ValueError, TypeError):
                    agility_val = 0
                try:
                    db.execute_query("add_class", (raw_class,))
                except Exception as e:
                    print(f"Error inserting Class '{raw_class}': {e}")
                try:
                    db.execute_query(
                        "add_character",
                        (
                            raw_name,
                            raw_class,
                            life_val,
                            mana_val,
                            strength_val,
                            intel_val,
                            agility_val,
                            raw_user
                        )
                    )
                except Exception as e:
                    print(f"Error inserting character '{raw_name}': {e}")

        elif "pnjs" in filename:
            for pnj in data.get("PNJs", []):
                raw_name = str(pnj.get("Nom", "")).strip()
                if not raw_name:
                    print(f"Skipping incomplete NPC entry: {pnj}")
                    continue

                dialogue_str = str(pnj.get("Dialogue", "")).strip()

                try:
                    db.execute_query("add_npc", (raw_name, dialogue_str))
                    npc_id = db.cursor.lastrowid
                except Exception as e:
                    print(f"Error inserting PNJ '{raw_name}': {e}")
                    continue

                for raw_q in pnj.get("Quêtes", []):
                    quest_name = str(raw_q).strip()
                    if not quest_name:
                        continue

                    quest_rows = db.execute_query("find_quest_id", (quest_name,))
                    if quest_rows and len(quest_rows) > 0:
                        quest_id = quest_rows[0]["QuestID"]
                        try:
                            db.execute_query("add_npc_quest", (npc_id, quest_id))
                        except Exception as e:
                            print(f"  Error linking PNJ '{raw_name}' → quest '{quest_name}': {e}")
                    else:
                        print(f"Quest '{quest_name}' not found for PNJ '{raw_name}'")

                inv_items = pnj.get("Inventaire", [])
                if inv_items:
                    try:
                        db.execute_query("add_inventory", ())
                        inv_id = db.cursor.lastrowid
                    except Exception as e:
                        print(f"  Error creating Inventory for PNJ '{raw_name}': {e}")
                        continue

                    try:
                        db.execute_query("add_npc_inventory", (inv_id, npc_id))
                    except Exception as e:
                        print(f"  Error linking Inventory → PNJ '{raw_name}': {e}")

                    for raw_item in inv_items:
                        item_name = str(raw_item).strip()
                        if not item_name:
                            continue

                        item_rows = db.execute_query("find_item_id", (item_name,))
                        if item_rows and len(item_rows) > 0:
                            item_id = item_rows[0]["ItemID"]
                            try:
                                db.execute_query("add_inventory_item", (inv_id, item_id, 1))
                            except Exception as e:
                                print(f"    Error adding item '{item_name}' to PNJ '{raw_name}' inventory: {e}")
                        else:
                            print(f"Item '{item_name}' not found (PNJ '{raw_name}').")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    if len(sys.argv) < 2:
        print("Usage: python import_data.py <directory_with_files>")
        return
    
    files = ["joueurs.csv", "objets.csv", "personnages.json", "sorts.csv", "quetes.xml", "monstres.xml", "pnjs.json"]

    db = Database(
        config["host"],
        config["user"],
        config["password"],
        config["database"]
    )
    db.connect()
    db.parseQueries("schema/queries.sql")
    clear_screen()

    print("Type the filename to import (or [q] to quit, [r] to clear).")
    for file in files:
        full_path = os.path.join(sys.argv[1], file)
        if not os.path.isfile(full_path):
            print(f"File not found: {full_path}")
            continue
        ext = file.lower().rsplit(".", 1)[-1]
        if ext == "csv":
            importCSV(full_path, db)
        elif ext == "xml":
            importXML(full_path, db)
        elif ext == "json":
            importJSON(full_path, db)
        else:
            print("Unsupported file type. Please provide .csv, .xml, or .json")

    db.disconnect()


if __name__ == "__main__":
    main()
