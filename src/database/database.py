import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host="localhost", user="root", password="", database="rpg_db"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
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
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connexion fermée.")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            self.connection.rollback()
            return None

    """ -------------------------------PLAYERS----------------------------------------- """

    def try_connect(self, username, mdp):
        self.execute_query("SELECT id, password_hash FROM players WHERE username = %s", (username,))
        user_data = self.cursor.fetchone()
        if not user_data:
            return False
        
        stored_hash = user_data["password_hash"]
        if not self.verify_password(mdp, stored_hash):
            return False

        return True

    def try_register(self, username, mdp):
        self.execute_query("SELECT id FROM players WHERE username = %s", (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            return False
        self.execute_query("INSERT INTO players (username) ")

    def add_player(self, username):
        self.execute_query("INSERT INTO players (username) VALUES (%s)", (username,))

    #getters
    
    def get_player(self, player_id):
        self.execute_query("SELECT * FROM players WHERE id = %s", (player_id,))
        return self.cursor.fetchone()

    
    """ -------------------------------ITEMS----------------------------------------- """

    #setters

    def add_item(self, name, item_type, power, price):
        self.execute_query(
            "INSERT INTO items (name, type, power, price) VALUES (%s, %s, %s, %s)",
            (name, item_type, power, price)
        )
    
    #getters

    def get_item(self, name):
        pass

    
    
    def search_items(self, item_type):
        self.execute_query("SELECT * FROM items WHERE type = %s", (item_type,))
        return self.cursor.fetchall()
    

    """ -------------------------------CHARACTERS----------------------------------------- """

    