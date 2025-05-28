from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey, keys

class MenuController:
    def __init__(self, db):
        self.database = db
        self.username = ""
        self.currentIndex = 0
        suite = Menu("Main", [Menu("Create A Character", None), Menu("Manage My Characters", None),
                               Menu("Items And Inventory", None), Menu("Monsters And Loop", None), Menu("Quests", None)])
        
        self.menu = Menu("Welcome", [Menu("Register", [suite]), Menu("Login", [suite])])
        self.view = MenuDisplay()
        self.previousMenu = []

    def displayRightMenu(self):
        if self.menu.getTitle() == "Register" or self.menu.getTitle() == "Login":
            self.handleRegisterLogin()
        self.view.displayMenu(self.menu, self.currentIndex)

    def launchView(self):
        while True:
            self.displayRightMenu()
            key = getkey()
            if key == keys.UP:
                self.currentIndex = max(0, self.currentIndex - 1)
            elif key == keys.DOWN:
                maxIndex = len(self.menu.getSons()) - 1
                self.currentIndex = min(maxIndex, self.currentIndex + 1)
            if key == keys.ENTER:
                if self.menu.getSons():
                    self.previousMenu.append(self.menu)
                    self.menu = self.menu.getSons()[self.currentIndex]
                    self.currentIndex = 0
                else:
                    return
            if key == keys.ESCAPE:
                if not self.previousMenu:
                    return
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0

    def handleRegisterLogin(self):
        login = self.menu.getTitle() == "Login"
        username = []
        password = []
        message = None
        pwTurn = False
        while True:
            self.view.displayLoginRegister(login, username, password, pwTurn, message)
            message = None
            key = getkey()
            if key == keys.ESCAPE:
                if pwTurn == True:
                    pwTurn = False
                    password = []
                else:
                    self.menu = self.previousMenu.pop()
                    self.currentIndex = 0
                    return
            if key == keys.BACKSPACE:
                if pwTurn and password:
                    password.pop()
                if not pwTurn and username:
                    username.pop()
            if key == keys.ENTER:
                if not pwTurn:
                    if len(username) > 5:
                        pwTurn = True
                    else:
                        message = "Minimum 5 Characters"
                else:
                    if len(password)>5:
                        if login:
                            if self.database.execute_query("login_player", [''.join(username), ''.join(password)]):
                                self.previousMenu.append(self.menu)
                                self.menu = self.menu.getSons()[self.currentIndex]
                                self.currentIndex = 0
                                self.username = ''.join(username)
                            else:
                                message = "Incorrect Username or Password"
                                username = []
                                password = []
                                pwTurn = False
                        else:
                            if self.database.execute_query("add_player", [''.join(username), ''.join(password)]):
                                self.previousMenu.append(self.menu)
                                self.menu = self.menu.getSons()[self.currentIndex]
                                self.currentIndex = 0
                                self.username = ''.join(username)
                            else:
                                message = "Username Already In Use"
                                username = []
                                password = []
                                pwTurn = False
                    else:
                        message = "Minimum 5 Characters"

            if isinstance(key, str) and key.isalpha():
                if not pwTurn:
                    if len(username) < 30:
                        username.append(str(key))
                    else:
                        message = "Maximum Length Reached"
                else:
                    password.append(str(key))
            

    def handleCharacters(self):
        create = self.menu.getTitle() == "Create A Character"
        chosen = None
        
        if not create:
            chars = self.database.execute_query("get_charcacters", [self.username])
            index = 0
            
            while True:
                self.view.displayMenu(self.menu, index)
                key = getkey()
                if key == keys.UP:
                    index = max(0, index -1)
                if key == keys.DOWN:
                    maxIndex = len(chars) - 1
                    index = min(maxIndex, index + 1) 
                if key == keys.ENTER:
                    chosen = chars[index]
                    return
                if key == keys.ESCAPE:
                    self.menu = self.previousMenu.pop()
                    self.currentIndex = 0
        stats = []
        index = 0
        while True:
            if chosen:
                stats = self.database.execute_query("get_stats", [chosen])
            self.view.displayCharacter(chosen, stats)
            key = getkey()
            if key == keys.UP:
                index = max(0, index -1)
            if key == keys.DOWN:
                maxIndex = len(chars) - 1
            if key == keys.LEFT:
                stats 
            if key == keys.RIGHT:
                pass
            if key == keys.ENTER:
                pass
            if key == keys.ESCAPE:
                pass




            



