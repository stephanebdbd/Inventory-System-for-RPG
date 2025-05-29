from view.enumMenu import Menus
from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey, keys
from database.db import Database

class MenuController:
    def __init__(self, db : Database):
        self.database = db
        self.username = ""
        self.currentIndex = 0
        suite = Menu("Main", [Menu("Create A Character", None), Menu("Manage My Characters", None),
                               Menu("Items And Inventory", None), Menu("Monsters And Loot", None), Menu("Quests", None)])
        
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
                    if len(password)>=5:
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
        create_mode = self.menu.getTitle() == "Create A Character"
        
        if create_mode:
            self.handleCreateCharacter()
        else:
            self.handleManageCharacters()

    def handleCreateCharacter(self):
        char_name = ""
        stats = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        points_left = 15
        selected_stat = 0
        stat_names = list(stats.keys())
        message = None
        
        while True:
            self.view.displayCharacterCreation(char_name, stats, selected_stat, points_left, message)
            message = None
            key = getkey()
            
            if key == keys.UP:
                selected_stat = max(0, selected_stat - 1)
            elif key == keys.DOWN:
                selected_stat = min(len(stats) - 1, selected_stat + 1)
            elif key == keys.LEFT:
                stat_name = stat_names[selected_stat]
                if stats[stat_name] > 8:
                    stats[stat_name] -= 1
                    points_left += 1
            elif key == keys.RIGHT:
                if points_left > 0:
                    stat_name = stat_names[selected_stat]
                    stats[stat_name] += 1
                    points_left -= 1
            elif key == keys.ENTER:
                # Name input
                self.view.displayNameInput(char_name, "Enter character name")
                name_key = getkey()
                
                if name_key == keys.ENTER:
                    if char_name.strip():
                        break  # Proceed to save
                    else:
                        message = "Name cannot be empty"
                elif name_key == keys.BACKSPACE:
                    char_name = char_name[:-1]
                elif name_key.isprintable():
                    char_name += name_key
            elif key == 's':
                if not char_name:
                    message = "Please set a name first (press ENTER)"
                else:
                    if self.saveCharacter(char_name, stats):
                        self.view.showMessage("Character created successfully!")
                        return True
                    else:
                        message = "Failed to create character"
            elif key == keys.ESCAPE:
                return False

    def handleManageCharacters(self):
        characters = self.database.execute_query("get_characters", [self.username])
        if not characters:
            self.view.showMessage("No characters found!")
            return
        
        selected_index = 0
        selected_character = None
        
        while not selected_character:
            self.view.displayCharacterList(characters, selected_index)
            key = getkey()
            
            if key == keys.UP:
                selected_index = max(0, selected_index - 1)
            elif key == keys.DOWN:
                selected_index = min(len(characters) - 1, selected_index + 1)
            elif key == keys.ENTER:
                selected_character = characters[selected_index]
            elif key == keys.ESCAPE:
                return
        
        stats = self.database.execute_query("get_stats", [selected_character['id']])
        if not stats:
            self.view.showMessage("Failed to load character stats")
            return
        
        selected_stat = 0
        stat_names = list(stats.keys())
        original_stats = stats.copy()
        
        while True:
            self.view.displayCharacterManagement(selected_character, stats, selected_stat)
            key = getkey()
            
            if key == keys.UP:
                selected_stat = max(0, selected_stat - 1)
            elif key == keys.DOWN:
                selected_stat = min(len(stats) - 1, selected_stat + 1)
            elif key == keys.LEFT:
                stat_name = stat_names[selected_stat]
                stats[stat_name] = max(1, stats[stat_name] - 1)
            elif key == keys.RIGHT:
                stat_name = stat_names[selected_stat]
                stats[stat_name] += 1
            elif key == 's':
                if stats != original_stats:
                    if self.updateCharacter(selected_character['id'], stats):
                        self.view.showMessage("Character updated successfully!")
                        original_stats = stats.copy()
                    else:
                        self.view.showMessage("Failed to update character")
            elif key == keys.ESCAPE:
                if stats != original_stats:
                    self.view.showMessage("Discarding unsaved changes")
                return