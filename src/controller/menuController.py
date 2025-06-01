from model.menu import Menu
from view.menuDisplay import MenuDisplay
from getkey import getkey, keys
from database.db import Database
#******************************************🔻MENU🔻*****************************************************
class MenuController:
    #******************************************🔻CONSTRUCTURE🔻*****************************************************
    def __init__(self, db : Database):
        self.database = db
        self.username = ""
        self.currentIndex = 0
        self.top_queries = {
            "Top 10 players by Gold":                        "TOPGOLD",
            "Player with most characters of the same class": "RANK1",
            "Quest with highest Gold per Difficulty ratio":  "TOPQUEST",
            "NPC whose inventory has the highest cumulative Gold value": "TOPPNJ",
            "Most frequently rewarded itemtype in level 5 quests":      "TOPITEM",
            "Monsters with the best cumulative Gold loot relative to their LifePoints": "TOPMONSTER"
        }
        suite = [Menu("Main", [Menu("Create A Character", None), Menu("Manage My Characters", None),

                               Menu("Items And Inventory", None), Menu("Monsters And Loot", None), Menu("NPC",None),
                               
                               Menu("Quests", None), Menu("Rankings", [Menu("Top 10 players by Gold", None),
                                                                       Menu("Player with most characters of the same class", None),
                                                                       Menu("Quest with highest Gold per Difficulty ratio", None),
                                                                       Menu("NPC whose inventory has the highest cumulative Gold value", None),
                                                                       Menu("Most frequently rewarded itemtype in level 5 quests", None),
                                                                       Menu("Monsters with the best cumulative Gold loot relative to their LifePoints", None)]), Menu("Manage Profile", None)])]

        
        self.menu = Menu("Welcome", [Menu("Register", suite), Menu("Login", suite)])
        self.view = MenuDisplay()
        self.previousMenu = []
#******************************************🔻RIGHT_MENU🔻*****************************************************
    def displayRightMenu(self):
        if self.menu.getTitle() == "Register" or self.menu.getTitle() == "Login":
            self.handleRegisterLogin()
        if self.menu.getTitle() == "Create A Character" or self.menu.getTitle() == "Manage My Characters":
            self.handleCharacters()
        if self.menu.getTitle() == "Quests":
            self.handleQuests()
        if self.menu.getTitle() == "Items And Inventory" :
            self.handleCharacterInventory()
        if self.menu.getTitle() == "Monsters And Loot":
            self.handleMonster()

        if self.menu.getTitle() == "NPC":
            self.handleNpc()

        if self.menu.getTitle() in self.top_queries.keys():
            self.handleRankings()
        if self.menu.getTitle() == "Manage Profile":
            self.handleProfile()

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
#******************************************🔻AUTH🔻*****************************************************
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
                            result = self.database.execute_query("check_login_player", (''.join(username), ''.join(password)))
                            if result and len(result)>0:
                                self.previousMenu.append(self.menu)
                                self.menu = self.menu.getSons()[self.currentIndex]
                                self.currentIndex = 0
                                self.username = ''.join(username)
                                break
                            else:
                                message = "Incorrect Username or Password"
                                username = []
                                password = []
                                pwTurn = False
                        else:
                            id = self.database.execute_query("register_player", (''.join(username), ''.join(password)))
                            if id is None:
                                message = "Username Already In Use"
                                username = []
                                password = []
                                pwTurn = False
                            else:
                                self.previousMenu.append(self.menu)
                                self.menu = self.menu.getSons()[self.currentIndex]
                                self.currentIndex = 0
                                self.username = ''.join(username)
                                break
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
            
#******************************************🔻CHARACTERS🔻*****************************************************
    def handleCharacters(self):
        create_mode = self.menu.getTitle() == "Create A Character"
        
        if create_mode:
            self.handleCreateCharacter()
        else:
            self.handleManageCharacters()
#***********************🔻CREATE_CHARACTER🔻*********************************
    def handleCreateCharacter(self):
        classes = self.database.execute_query("get_all_classes")
        class_names = [ row['Name'] for row in classes ]
        char_name = ""
        stats = {
            "Class": class_names[0],
            "LifePoints": 10,
            "Mana": 10,
            "Strength": 10,
            "Intelligence": 10,
            "Agility": 10
        }
        points_left = 15
        selected_row = 0
        class_index = 0
        stat_names = list(stats.keys())
        message = None
        
        while True:
            self.view.displayCharacterCreation(char_name, stats, selected_row, points_left, message)
            message = None
            key = getkey()
            
            if key == keys.UP:
                selected_row = max(0, selected_row - 1)
            elif key == keys.DOWN:
                selected_row = min(len(stat_names), selected_row + 1)
            elif key == keys.LEFT:
                if selected_row == 0:
                    pass
                else:
                    stat_name = stat_names[selected_row -1 ]
                    if stat_name == "Class":
                        if class_index > 0:
                            class_index -= 1
                        else:
                            class_index = len(class_names) - 1
                        stats["Class"] = class_names[class_index]
                    else:
                        if stats[stat_name] > 8:
                            stats[stat_name] -= 1
                            points_left += 1
            elif key == keys.RIGHT:
                if selected_row == 0:
                    pass
                else:
                    stat_name = stat_names[selected_row -1]
                    if stat_name == "Class":
                        if class_index < len(class_names) - 1:
                            class_index += 1
                        else:
                            class_index = 0
                        stats["Class"] = class_names[class_index]
                    else:
                        if points_left > 0:
                            stats[stat_name] += 1
                            points_left -= 1
            elif key == keys.ENTER:
                if not char_name:
                    message = "Please set a name first (press ENTER)"
                else:
                    if self.database.execute_query("add_character", (char_name, stats["Class"], 
                                                                     stats["LifePoints"], stats["Mana"], stats["Strength"],
                                                                     stats["Intelligence"], stats["Agility"], self.username)):
                        self.menu = self.previousMenu.pop()
                        return True
                    else:
                        message = "Failed to create character"
            elif selected_row == 0 and isinstance(key, str) and key.isprintable():
                char_name += key

            elif key == keys.BACKSPACE and selected_row == 0:
                char_name = char_name[:-1]
            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return False
#******************🔻MANAGE_CHARACTER🔻******************************
    def handleManageCharacters(self):
        characters = self.database.execute_query("get_characters", (self.username, ))
        if not characters:
            self.view.showMessage("No characters found!")
            return
        
        selected_index = 0
        selected_character = None
        
        while not selected_character:
            self.view.displayMyCharactersList(characters, selected_index)
            key = getkey()
            
            if key == keys.UP:
                selected_index = max(0, selected_index - 1)
            elif key == keys.DOWN:
                selected_index = min(len(characters) - 1, selected_index + 1)
            elif key == keys.ENTER:
                selected_character = characters[selected_index]
            elif key == keys.ESCAPE:
                return
        
        stats_rows = self.database.execute_query("get_stats", (selected_character['CharID'], ))
        if not stats_rows:
            self.view.showMessage("Failed to load character stats")
            return
        
        selected_stat = 0
        stats = stats_rows[0]
        original_stats = stats.copy()
        stat_names = list(stats.keys())
        message = None
        while True:
            self.view.displayCharacterManagement(selected_character, stats, selected_stat, message)
            message = None
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
            elif key == keys.ENTER:
                if stats != original_stats:
                    if self.database.execute_query("edit_character", (stats["LifePoints"],stats["Mana"],stats["Strength"],
                                                                      stats["Intelligence"],stats["Agility"], selected_character["CharID"])):
                        message = "Character updated successfully!"
                        original_stats = stats.copy()
                    else:
                        message = "Failed to save the changes"
            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return
            
    
    #******************************************🔻Inventory🔻*****************************************************
    def handleCharacterInventory(self):
        """
        voir la liste de ses characters (d'un joueur)
        et acceder à l'inventory de un de ses characters
        """
        characters = self.database.execute_query("get_characters", (self.username, ))
        index = 0

        while True:
            self.view.displayMyCharactersList(characters, index)
            key = getkey()

            if key == keys.UP:
                index = max(0, index - 1)

            elif key == keys.DOWN:
                index = min(len(characters) - 1, index + 1)
            
            elif key == keys.ENTER:
                char_selected = characters[index]
                inventory = self.database.execute_query("get_character_inventory",(char_selected["CharID"], ))
                item_index = 0

                while True:
                    self.view.displayCharacterInventory(char_selected, inventory, item_index)
                    item_key = getkey()

                    if item_key == keys.UP:
                        item_index = max(0, item_index - 1)

                    elif item_key == keys.DOWN:
                        item_index = min(len(inventory) - 1, item_index + 1)

                    elif item_key == keys.DELETE and inventory:
                        item_to_delete = inventory[item_index]
                        self.database.execute_query("delete_inventory_item", (item_to_delete["InventoryID"], item_to_delete["ItemID"] ))
                               
                        inventory = self.database.execute_query("get_character_inventory", (char_selected["CharID"],))
                        # Ajuste index su longueur dépassé de la liste
                        item_index = min(item_index, len(inventory) - 1 if inventory else 0)

            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return  


<<<<<<< HEAD
    #******************************************🔻Monster🔻*****************************************************
=======
>>>>>>> 3580aa7214a7be9e27d4da4474fe3000c2dc330c
    def handleMonster(self):
        """
        voir l'ensemble des monstres du jeu
        et en clickant sur l'un, voir ses infos
        """
        monsters = self.database.execute_query("get_monsters")
        index = 0
        
        while True:
            self.view.displayAllMonsters(monsters, index)
            key = getkey()

            if key == keys.UP:
                index = max(0, index - 1)
            elif key == keys.DOWN:
                index = min(len(monsters) - 1, index + 1)
            elif key == keys.ENTER:
                monster_selected = monsters[index]
                monster_id = monster_selected["MonsterID"]

                raw_loots = self.database.execute_query("get_monster_loot", (monster_id,))
                if raw_loots is None:
                    raw_loots = []

                combined_loots = []
                for loot_row in raw_loots:
                    combined_loots.append({
                        "type":         "gold",
                        "GoldQuantity": loot_row["GoldQuantity"],
                        "GoldProbability": loot_row["GoldProbability"]
                    })

                    loot_id = loot_row["LootID"]
                    item_rows = self.database.execute_query("get_monster_items", (loot_id,))
                    if item_rows:
                        for item_row in item_rows:
                            combined_loots.append({
                                "type":        "item",
                                "ItemName":    item_row["ItemName"],
                                "Probability": item_row["Probability"],
                                "AmountItem":  item_row["AmountItem"]
                            })

                while True:
                    self.view.displayMonsterInfo(monster_selected, combined_loots)
                    key2 = getkey()
                    if key2 == keys.ESCAPE:
                        break
                
            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return

    #******************************************🔻Quests🔻*****************************************************

    def handleQuests(self):
        """
        voir TOUTES les quests du jeu
       
        et voir les infos d'une quest 
        quand on click
        """
        
        quests =  self.database.execute_query("get_quests")  
        index = 0

        while True:
            self.view.displayQuestList(quests, index)
            key = getkey()

            if key == keys.DOWN:
                max_index = len(quests) - 1
                index = min(max_index, index + 1)

            elif key == keys.UP:
                index = max(0, index-1)

            elif key == keys.ENTER:
                quest_chosen = quests[index]
                self.view.displayQuestInfo(quest_chosen)  #  montrer les infos d'une quete lorsqu'on click dessus

            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return
    #******************************************🔻rankings🔻*****************************************************
    def handleRankings(self):
        ranking = self.database.execute_query(self.top_queries[self.menu.getTitle()])
        self.view.displayRanking(self.menu.getTitle(), ranking)
        while True:
            key = getkey()
            if key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                return


    def handleNpc(self):
        """
        Affiche la liste des NPCs.
        
        Quand l'utilisateur sélectionne un NPC, 
        quand on click, affiche les quêtes associées à ce NPC.
        """
        npcs = self.database.execute_query("get_all_npc")
        index = 0

        while True:
            self.view.displayNpcList(npcs, index)
            key = getkey()

            if key == keys.DOWN:
                index = min(len(npcs) - 1, index + 1)

            elif key == keys.UP:
                index = max(0, index - 1)

            elif key == keys.ENTER:
                npc_chosen = npcs[index]
                npc_name = npc_chosen['npcName']
                # Récupérer les quêtes associées à ce NPC
                quests = self.database.execute_query("get_quests_by_npc", (npc_name,))
                self.handleNpcQuests(quests)  # les quests proposés par un npc

            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return
            


    def handleNpcQuests(self, quests):
        """
        voir les quetes proposées par un npc
        et quand on click sur une quete, voir les 
        infos de la quete
        """
        index = 0

        while True:
            self.view.displayQuestListNpc(quests, index)
            key = getkey()

            if key == keys.DOWN:
                index = min(len(quests) - 1, index + 1)

            elif key == keys.UP:
                index = max(0, index - 1)

            elif key == keys.ENTER:
                quest_chosen = quests[index]
                self.view.displayQuestInfo(quest_chosen)

            elif key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return
                

    #******************************************🔻Profile🔻*****************************************************
    def handleProfile(self):
        result = self.database.execute_query("get_player", (self.username,))
        player_info = result[0]
        self.view.displayProfile(player_info)
        while True:
            key = getkey()
            if key == keys.ESCAPE:
                self.menu = self.previousMenu.pop()
                self.currentIndex = 0
                return
