from controller.menuController import MenuController
from database.db import Database
# mysql -h 192.168.135.218 -u pietro -p rpgg
config = {
    "host": "127.0.0.1",
    "user": "pietro",
    "password": "yildizmygoat",
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