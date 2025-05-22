import csv
import xml
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
    pass
    


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
                db.add_item(row["Nom"],
                              row["Type"],
                              row["Propriétés"],
                              row["Prix"])
        if "sorts" in file:
            for row in reader:
                db.add_spell(row["ID"],
                             row["Coût en Mana"],
                             row["Temps de Recharge"],
                             row["Puissance d'Attaque"])


def importJSON(file: str, db: Database):
    print(file)
    pass

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