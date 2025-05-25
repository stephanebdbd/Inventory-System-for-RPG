from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay

class MenuController:
    def __init__(self):
        currentMenu = 0
        suite = Menu("Main")
        self.menu = Menu("Welcome", [Menu("Register", suite), Menu("Login", suite)])  
        self.view = MenuDisplay 


    def launchView(self):
        self.view(self.menu.getMenu())
