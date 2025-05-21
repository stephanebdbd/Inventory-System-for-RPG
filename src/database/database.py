import mysql.connector


#tamer 
class Database :
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
        self.cursor = None
        self.connect()
        self.create_tables()
    
    def connect(self):
        pass
        
    def getSpellLis(self):
        pass

