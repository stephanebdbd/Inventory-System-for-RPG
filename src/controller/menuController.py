from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey, keys

class MenuController:
    def __init__(self, db):
        self.database = db
        self.username = ""
        self.currentIndex = 0
        suite = Menu("Main")
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
                else:
                    self.menu = self.previousMenu.pop()
                    self.currentIndex = 0
                    return
            if key == keys.DELETE:
                if pwTurn:
                    password.pop()
                else:
                    username.pop()
            if key == keys.ENTER:
                if pwTurn == False:
                    pwTurn == True
                else:
                    if login:
                        if self.database.execute_query("login_player", [username.join(), password.join()]):
                            self.previousMenu.append(self.menu)
                            self.menu = self.menu.getSons()[self.currentIndex]
                            self.currentIndex = 0
                            self.username = username.join()
                        else:
                            message = "Incorrect Username or Password"
                            username = []
                            password = []
                            pwTurn = False
                    else:
                        if self.database.execute_query("add_player", [username.join(), password.join()]):
                            self.previousMenu.append(self.menu)
                            self.menu = self.menu.getSons()[self.currentIndex]
                            self.currentIndex = 0
                            self.username = username.join()
                        else:
                            message = "Username Already Used"
                            username = []
                            password = []
                            pwTurn = False
            else:
                if not pwTurn:
                    if username < 30:
                        username.append(str(key))
                    else:
                        message = "Maximum Length Reached"
                else:
                    password.append(str(key))
            
