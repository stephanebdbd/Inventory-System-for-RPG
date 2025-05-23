import csv
import json
import xml.etree.ElementTree as xmlTree
import sys
import os
from database import Database

Spells = {"ID": "id",
         "Nom": "name",
         "Coût en Mana": "mana",
         "Temps de Recharge": "cd",
         "Puissance d'Attaque": "ap"
         }
Players = {"ID": "id",
           "NomUtilisateur": "username",
           "Niveau": "level",
           "XP": "xp",
           "Monnaie": "currency",
           "SlotsInventaire": "inventorySlots"
           }
Items = {"Nom": "name",
         "Type": "type",
         "Propriétés": "effect",
         "Prix": "price"
         }
Monsters = {"monstre": "monster",
            "attaque": "attack",
            "defense": "defense",
            "drops": "drops",
            "nombre": "quantity",
            "probabilité": "probability",
            "vie": "lifePoints",
            "Or": "gold"
            }
Quests = {"quête": "quest",
          "Description": "description",
          "Difficulté": "difficulty",
          "Expérience": "exp",
          "Récompenses": "rewards",
          "Or": "gold",
          "Objets": "items"
          }
Characters = {"personnages": "characters",
              "Nom": "name",
            "Classe": "classe",
            "Vie": "lifePoints",
            "Mana": "mana",
            "Force": "strength",
            "Intelligence": "intelligence",
            "Agilite": "agility",
            "utilisateur": "username"
}
PNJs = {"Nom": "name",
        "Dialoque": "dialogue",
        "Quêtes": "quests",
        "Inventaire": "inventory"
        }

def importXML(file: str, db: Database):
    tree = xmlTree.parse(file)
    root = tree.getroot()
    if "monstres" in file:
        for monster in root.findall('monstre'):
            drops = []
            for item in monster.findall('drops'):
                drop = {}
                if item.tag is "Or":
                    drop["name"] = "gold"
                    drop["probability"] = item.findtext('probabilité')
                    drop["quantity"] = item.findtext('nombre')
                else:
                    drop["name"] = item.tag
                    drop["probability"] = item.findtext('probabilité')
                    drop["quantity"] = item.findtext('nombre')
                drop.append(drop)
            db.execute_query("add_monster", [int(monster.findtext('id')),
                           monster.findtext('nom'),
                           int(monster.findall('attaque')),
                           int(monster.findall('defense')),
                           int(monster.findall('vie')),
                           drops])
    if "quetes" in file:
        for quest in root.findall('quêtes'):
            rewards = []
            rewards.append(int(quest.findall('Or')))
            for rew in quest.findall('Récompenses'):
                if rew.tag != "Or":
                    rewards.append(rew)
            db.execute_query("add_quest", [quest.findtext('Description'),
                         quest.findtext('Nom'),
                           int(quest.findtext('Difficulté')),
                           int(quest.findall('Expérience')),
                           rewards])


def importCSV(file: str, db: Database):
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if "joueurs" in file:
            for row in reader:
                db.add_player(row["ID"],
                                row["Niveau"],
                                row["XP"], 
                                row["Monaie"],
                                row["SlotsInventaire"])
        if "objets" in file:
            for row in reader:
                db.execute_query("add_item", [row["Nom"],
                              row["Type"],
                              row["Propriétés"],
                              row["Prix"]])
        if "sorts" in file:
            for row in reader:
                db.execute_query("add_spell", [row["ID"],
                             row["Coût en Mana"],
                             row["Temps de Recharge"],
                             row["Puissance d'Attaque"]])


def importJSON(file: str, db: Database):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if "personnages" in file:
            for charater in data["personnages"]:
                db.execute_query("add_character", [charater["Nom"],
                                 charater["Classe"],
                                 charater["Vie"],
                                 charater["Mana"],
                                 charater["Force"],
                                 charater["intelligence"],
                                 charater["Agilite"],
                                 charater["utilisateur"]])
        if "pnjs" in file:
            for pnj in data["PNJs"]:
                db.execute_query("add_npc", [pnj["Nom"],
                           pnj["Dialogue"],
                           pnj["Quêtes"],
                           pnj["Inventaire"]])


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    db = Database(
        host="",
        user="",
        password="",
        database=""
    )
    db.connect()
    clear_screen()
    while True:
        print("** Enter [q] to leave, [r] to clear **\n")
        file = input("Enter file name: ")
        path = os.path.join(sys.argv[1], file)
        if "csv" in file:
            importCSV(path, db)
        if "xlm" in file:
            importXML(path, db)
        if "json" in path:
            importJSON(path, db)
        if file is "r":
            clear_screen()
        if file is "q":
            return

if __name__ == "__main__":
    main()