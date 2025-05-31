from controller.menuController import MenuController
from database.db import Database

config = {
    "host": "localhost",
    "user": "pietro",
    "password": "YildizMyGoat1!",
    "database": "rpgg",
}

def main():
    db = Database(config["host"], config["user"], config["password"], config["database"])
    db.connect()
    db.parseQueries("database/schema/queries.sql")
    menu = MenuController(db)
    menu.launchView()
    db.disconnect()
    

if __name__ == '__main__':
    main()