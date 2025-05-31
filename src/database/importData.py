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

            for drop_elem in monster.findall("drops/item"):
                tag = drop_elem.tag.lower()
                if tag == "or":
                    try:
                        gold_qty  = int(drop_elem.findtext("quantité") or 0)
                        gold_prob = float(drop_elem.findtext("probabilité") or 0)
                    except ValueError as e:
                        print(f"Skipping malformed gold drop ({e}): {xmlTree.tostring(drop_elem, encoding='unicode')}")
                        continue

                    db.execute_query(
                        "add_monster_gold_drop",
                        (monster_id, gold_qty, gold_prob)
                    )
                else:
                    try:
                        item_id     = int(drop_elem.findtext("item_id") or 0)
                        quantity    = int(drop_elem.findtext("quantité") or 0)
                        probability = float(drop_elem.findtext("probabilité") or 0)
                    except ValueError as e:
                        print(f"Skipping malformed item drop ({e}): {xmlTree.tostring(drop_elem, encoding='unicode')}")
                        continue

                    db.execute_query(
                        "add_monster_item_drop",
                        (monster_id, item_id, quantity, probability)
                    )

    elif "quetes" in filename or "quêtes" in filename:
        for quest in root.findall("quête"):
            description = quest.findtext("Description") or ""
            quest_name  = quest.findtext("Nom") or ""
            try:
                difficulty = int(quest.findtext("Difficulté") or 0)
            except ValueError:
                difficulty = 0
            try:
                experience = int(quest.findtext("Expérience") or 0)
            except ValueError:
                experience = 0

            gold_reward = quest.findtext("Or")
            try:
                gold_qty = int(gold_reward) if gold_reward else 0
            except ValueError:
                gold_qty = 0

            db.execute_query(
                "add_quest",
                (description, quest_name, difficulty, experience, gold_qty)
            )

            for rew in quest.findall("Récompenses/item"):
                try:
                    item_id     = int(rew.findtext("item_id") or 0)
                    quantity    = int(rew.findtext("quantité") or 0)
                    probability = float(rew.findtext("probabilité") or 0)
                except ValueError as e:
                    print(f"Skipping malformed quest reward ({e}): {xmlTree.tostring(rew, encoding='unicode')}")
                    continue

                db.execute_query(
                    "add_quest_item_reward",
                    (quest_name, item_id, quantity, probability)
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

                if raw_name is None or raw_type is None or raw_prop is None or raw_price is None:
                    print(f"Skipping malformed row (None found): {row}")
                    continue

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
                if t in ("armer", "sword", "arm e", "arme"):
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
                        mana_cost  = int(row["Coût en Mana"])
                        cooldown   = int(row["Temps de Recharge"])
                        power      = int(row["Puissance d'Attaque"])
                    except ValueError as e:
                        print(f"Skipping malformed spell row ({e}): {row}")
                        continue

                    try:
                        db.execute_query(
                            "add_spell",
                            (spell_id, mana_cost, cooldown, power)
                        )
                    except Exception as e:
                        print(f"Erreur lors de l'insertion du sort {spell_id}: {e}")
                else:
                    print(f"Skipping incomplete spell row: {row}")


def importJSON(file_path: str, db: Database):
    """
    Import characters or NPCs from JSON files.
    """
    filename = os.path.basename(file_path).lower()
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        if "personnages" in filename:
            for character in data.get("personnages", []):
                req_keys = ["Nom", "Classe", "Vie", "Mana", "Force", "Intelligence", "Agilite", "utilisateur"]
                if all(k in character for k in req_keys):
                    try:
                        name     = character["Nom"]
                        cls      = character["Classe"]
                        life     = int(character["Vie"])
                        mana     = int(character["Mana"])
                        strength = int(character["Force"])
                        intel    = int(character["Intelligence"])
                        agility  = int(character["Agilite"])
                        username = character["utilisateur"]
                    except (ValueError, TypeError) as e:
                        print(f"Skipping malformed character ({e}): {character}")
                        continue

                    try:
                        db.execute_query(
                            "add_character",
                            (username, name, cls, life, mana, strength, intel, agility)
                        )
                    except Exception as e:
                        print(f"Erreur lors de l'insertion du personnage '{name}': {e}")
                else:
                    print(f"Skipping incomplete character entry: {character}")

        elif "pnjs" in filename:
            for pnj in data.get("PNJs", []):
                if "Nom" in pnj and "Dialogue" in pnj:
                    name     = pnj["Nom"]
                    dialogue = pnj["Dialogue"]
                    try:
                        db.execute_query(
                            "add_npc",
                            (name, dialogue)
                        )
                    except Exception as e:
                        print(f"Erreur lors de l'insertion du PNJ '{name}': {e}")
                else:
                    print(f"Skipping incomplete NPC entry: {pnj}")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    if len(sys.argv) < 2:
        print("Usage: python import_data.py <directory_with_files>")
        return

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
    while True:
        file = input("Enter file name: ").strip()
        if file.lower() == "q":
            break
        if file.lower() == "r":
            clear_screen()
            continue

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
