import mysql.connector
from mysql.connector import Error
import bcrypt

class Database:
    def __init__(self, host="localhost", user="root", password="", database="rpg_db"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Établit une connexion à la base de données."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Connexion à MySQL réussie !")
        except Error as e:
            print(f"Erreur de connexion : {e}")

    def disconnect(self):
        """Ferme la connexion."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connexion fermée.")

    def execute_query(self, query, params=None):
        """Exécute une requête SQL générique."""
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            self.connection.rollback()
            return None

    """ ------------------------------- PLAYERS ----------------------------------------- """
    
    def try_connect(self, username: str, mdp: str) -> None: 
        self.execute_query("SELECT id, password_hash FROM players WHERE username = %s", (username,))
        user_data = self.cursor.fetchone()
        if not user_data:
            return False
        
        stored_hash = user_data["password_hash"]
        if not self.verify_password(mdp, stored_hash):
            return False

        return True

    def try_register(self, username: str, mdp: str) -> None:
        self.execute_query("SELECT id FROM players WHERE username = %s", (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            return False
        self.execute_query("INSERT INTO players (username) ")
        #pas fini zeb

    def add_player(self, username: str) -> None:
        self.execute_query("INSERT INTO players (username) VALUES (%s)", (username,))

    def get_player(self, player_id: int): #jsp cque ca retourne, une liste?? dunno
        self.execute_query("SELECT * FROM players WHERE id = %s", (player_id,))
        return self.cursor.fetchone()

    def update_player_currency(self, player_id: int, amount: int) -> None:
        pass

    def update_player_level(self, player_id: int, new_level: int) -> None:
        pass

    """ ----------------------------- INVENTORY ---------------------------------------- """

    def add_item(self, name: str, item_type: str, power: str, price: int) -> None:
        self.execute_query(
            "INSERT INTO items (name, type, power, price) VALUES (%s, %s, %s, %s)",
            (name, item_type, power, price)
        )

    def get_item(self, name):
        pass

    def search_items(self, item_type: str): #same dunno
        self.execute_query("SELECT * FROM items WHERE type = %s", (item_type,))
        return self.cursor.fetchall()

    def add_item_to_inventory(self, player_id: int, item_id: int, quantity: int) -> None:
        pass

    def remove_item_from_inventory(self, player_id: int, item_id: int, quantity: int) -> None:
        pass

    def get_inventory(self, player_id: int) -> list:
        pass

    def equip_item(self, character_id: int, item_id: int) -> None:
        pass

    """ ------------------------------ MONSTERS ---------------------------------------- """

    def add_monster(self, name: str, attack: int, defense: int, hp: int, loot_table_id: int) -> None:
        pass

    def get_monster(self, monster_id: int) -> dict:
        pass

    def get_monster_loot(self, monster_id: int) -> list:
        pass

    """ ------------------------------ BATTLES ----------------------------------------- """

    def start_battle(self, player_id: int, monster_id: int) -> int:
        pass

    def log_battle_damage(self, battle_id: int, damage_dealt: int, damage_received: int) -> None:
        pass

    def end_battle(self, battle_id: int, winner: str) -> None:
        pass

    """ ----------------------------- REWARDS ----------------------------------------- """

    def add_reward(self, quest_id: int, item_id: int, quantity: int):
        pass

    def assign_reward(self, player_id: int, reward_id: int):
        pass

    """ ------------------------------- NPCS ------------------------------------------- """

    def add_npc(self, name: str, dialogue: str, location: str):
        pass

    def get_npc(self, npc_id: int) -> dict:
        pass

    def get_npc_quests(self, npc_id: int) -> list:
        pass

    """ ------------------------------ QUESTS ------------------------------------------ """

    def start_quest(self, player_id: int, quest_id: int):
        pass

    def complete_quest(self, player_id: int, quest_id: int):
        pass

    def get_active_quests(self, player_id: int) -> list:
        pass

    def get_quest_details(self, quest_id: int) -> dict:
        pass

    """ ----------------------------- CLASSES ----------------------------------------- """

    def set_class(self, classe):
        pass

    def get_classes(self):
        pass

    def get_spells(self, classe):
        pass

    def add_class_ability(self, class_name: str, ability_name: str, mana_cost: int) -> None:
        pass

    def get_class_abilities(self, class_name: str) -> list:
        pass

    def update_character_class(self, character_id: int, new_class: str) -> None:
        pass

    """ --------------------------- UTILITY METHODS ----------------------------------- """

    def verify_password(self, input_password: str, stored_hash: str) -> None:
        pass