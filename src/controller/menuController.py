from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey, keys

class MenuController:
    def __init__(self):
        self.currentIndex = 0
        suite = Menu("Main")
        self.menu = Menu("Welcome", [Menu("Register", [suite]), Menu("Login", [suite])])
        self.view = MenuDisplay()
        self.previousMenu = []

    def displayRightMenu(self):
        if self.menu.getTitle() == "Register":
            self.handleRegister()
        if self.menu.getTitle() == "Login":
            self.handleLogin()
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

    def handleRegister(self):
        pass

    def handleLogin(self):
        pass
