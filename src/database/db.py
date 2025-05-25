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
        self.queries = {}

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
    
    def parseQueries(self, path):
        """Parse les queries et les fait correcspondre a une clef dans un dictionnaire"""
        with open(path, 'r', encoding='utf-8') as f:
            key = None
            query = []
            for line in f:
                stripped = line.strip()

                if not stripped:
                    continue
                elif line.startswith("--"):
                    if key and query:
                        self.queries[key] = ' '.join(query)
                        query = []
                    key = line.lstrip('-').strip()
                else:
                    query.append(stripped)

    def execute_query(self, queryKey, params=None):
        """Exécute une requête SQL générique."""
        query  = self.queries[queryKey]
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            self.connection.rollback()
            return None