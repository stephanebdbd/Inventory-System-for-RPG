from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey

class MenuController:
    def __init__(self):
        self.currentIndex = 0
        suite = Menu("Main")
        self.menu = Menu("Welcome", [Menu("Register", suite), Menu("Login", suite)])
        self.view = MenuDisplay()
        self.previousMenu = []

    def displayRightMenu(self):
        self.view(self.menu.getMenu(self.menu, self.currentIndex))


    def launchView(self):
        self.displayRightMenu(self.currentIndex)
        key = getkey()
        if key == 'up':
            self.currentIndex += 1
        if key == 'down':
            self.currentIndex -= 1
        if key == 'enter':
            if self.menu.getSons():
                self.previousMenu.append(self.menu)
                self.menu = self.menu.getSons()[self.currentMenu]
                self.currentMenu = 0
        if key == "escape":
            if not self.previousMenu:
                return
            self.menu = self.previousMenu.pop()
            self.currentIndex = 0
