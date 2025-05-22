import csv
import xml
import sys
import os

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
           "Monnaie": "golds",
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
          "Descriptiopn": "description",
          "Difiiculté": "difficulty",
          "Expérience": "exp",
          "Récompenses": "rewards",
          "0r": "gold",
          "Objets": "items"
          }


def importXML(file: str, path: str):
    print(file)
    pass

def importCSV(file: str, path: str):
    print(file)
    pass

def importJSON(file: str, path: str):
    print(file)
    pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    path = sys.argv[1]
    while True:
        print("** Enter [q] to leave, [r] to clear **\n")
        file = input("Enter file name: ")
        if "csv" in file:
            importCSV(file, path)
        if "xlm" in file:
            importXML(file, path)
        if "json" in file:
            importJSON(file, path)
        if file is "r":
            clear_screen()
        if file is "q":
            return

if __name__ == "__main__":
    main()