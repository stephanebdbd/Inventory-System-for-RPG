import sqlparse
from sqlparse.tokens import Comment
import sys

def main():
    path = "queries.sql"
    with open(path, 'r', encoding='utf-8') as f:
        key = None
        query = []
        for line in f:
            if line.startswith('--'):
                if key:
                    print(key)
                    querys = ' '.join(query)
                    print(querys)
                key = line.strip("--").strip()
            else:
                query.append(line.strip())
    

if __name__ == "__main__":
    main()




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