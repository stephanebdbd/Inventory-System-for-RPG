from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from model.menu import Menu
from rich.text import Text
from rich.table import Table

class MenuDisplay:
    def __init__(self):
        self.console = Console()
        self.selected_style = Style(color="white", bgcolor="blue", bold=True)
        self.default_style = Style(color="cyan")
        self.panel_style = Style(color="magenta", bold=True)
        self.error_style = Style(color="red", bold=True)


    def displayMenu(self, currentMenu, selectedIndex):
        menu_title = currentMenu.getTitle()
        menu_items = [son.getTitle() for son in currentMenu.getSons()]

        body = []
        for idx, item in enumerate(menu_items):
            if idx == selectedIndex:
                body.append(f"[{self.selected_style}]→ {item}[/]")
            else:
                body.append(f"[{self.default_style}]  {item}[/]")

        panel = Panel(
            "\n".join(body),
            title=f"[bold yellow]{menu_title}[/bold yellow]",
            border_style=self.panel_style,
            width=70,
            padding=(1, 4))
        
        self.console.clear()
        self.console.print(panel)

    def displayLoginRegister(self, is_login_menu, username_chars, password_chars, pw_turn, message=None):
        username = ''.join(username_chars)
        password = '*' * len(password_chars)
        
        form_lines = [
            self.createLine("Username: " + username, not pw_turn),
            self.createLine("Password: " + password, pw_turn),
            Text("\nPress [ESC] to return")
        ]
        if message:
            form_lines.append(Text(f"\n{message}", style=self.error_style))

        title = "Login" if is_login_menu else "Registration"
        panel = Panel(
            Text.assemble(*form_lines),
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="magenta",
            width=50,
            padding=(1, 4))
        
        self.console.clear()
        self.console.print(panel)

    def createLine(self, text, is_selected):
        prefix = "→ " if is_selected else "  "
        style = self.selected_style if is_selected else self.default_style
        return Text(f"{prefix}{text}", style=style) + Text("\n")
    

    def displayCharacterCreation(self, character_name: str, stats: dict, selected_index: int, points_left: int, message: str = None):
        body = []
        
        prefix = "→ " if selected_index == 0 else "   "
        name_display = character_name if character_name else "[Unnamed]"
        body.append(f"{prefix}Name: {name_display}")
        body.append("")
        
        body.append(f"[bold]Points left:[/bold] {points_left}")
        body.append("")
        
        stat_names = list(stats.keys())
        for idx, stat in enumerate(stat_names, start=1):
            prefix = "→ " if idx == selected_index else "  "
            body.append(f"{prefix}{stat}: {stats[stat]}")
        
        body.extend([
            "",
        "[↑/↓] Move   [←/→] Change or edit",
        "[ENTER] Save [ESC] Cancel"
        ])
        
        if message:
            body.append(f"\n[red]{message}[/red]")
        
        panel = Panel(
            "\n".join(body),
            title="[bold yellow]Character Creation[/bold yellow]",
            border_style="magenta",
            width=50,
            padding=(1, 4)
        )
        
        self.console.clear()
        self.console.print(panel)


    def displayCharacterManagement(self, character: dict, stats: dict, selected_index: int, message : str):
        body = [
            f"Name: {character['Name']}",
            f"Class: {character['Class']}"
            ""
        ]
        
        stat_names = list(stats.keys())
        for idx, stat in enumerate(stat_names):
            prefix = "→ " if idx == selected_index else "  "
            body.append(f"{prefix}{stat}: {stats[stat]}")
        
        body.extend([
            "",
            "[←/→] Adjust stat",
            "[ENTER] Save changes",
            "[ESC] Return to list"
        ])

        if message:
            body.append(f"\n[red]{message}[/red]")
        
        panel = Panel(
            "\n".join(body),
            title="[bold yellow]Character Management[/bold yellow]",
            border_style="magenta",
            width=50,
            padding=(1, 4))
        
        self.console.clear()
        self.console.print(panel)


    
    def displayMyCharactersList(self, characters, index):
        characters_to_show = []
        for i, char in enumerate(characters):
            name = char.get("Name", f"Character {i}")
            if i == index:
                style = self.selected_style 
                chara_pointer  = "→ "
            else:
                style = self.default_style
                chara_pointer = "  "
            
            characters_to_show.append(Text(f"{chara_pointer}{name}", style=style))

        panel_title="[bold yellow]Select a Character to see his Inventory [/bold yellow]"
        self.displayPanel(panel_title, characters_to_show, 60, self.panel_style )


    def displayCharacterInventory(self, character, items, index, equipped_items: list):
        char_name = character.get("Name")
        lines = []

        for i, item in enumerate(items):
            name = item.get("Name")

        # les chhamps spécifiques
            if "AttackPower" in item:
                item_type = f"(Attack: {item.get('AttackPower')})"
            elif "Defense" in item:
                item_type = f"(Defense: {item.get('Defense')})"
            elif "Healing" in item:
                item_type = f"(Healing: {item.get('Healing')})"
            elif "Effect" in item:
                item_type = f"(Effect: {item.get('Effect')})"

            if item.get("ItemID") in equipped_items:                 
                item_in_equipment_marker = " [In Equipment] "    # pour indiquer qu elem est dans l equipemet du character
            else:
                item_in_equipment_marker = " "
            
            if i == index:
                style = self.selected_style
                item_pointer = "→ " 
            else:
                style = self.default_style
                item_pointer = " "

           
            
            lines.append(Text(f"{item_pointer}{name} - {item_type} ----- {item_in_equipment_marker}", style=style))
        
        lines.append(Text("\n[DELETE] pour supprimer l'objet sélectionné", style="bold red"))


        panel_title = f"[bold cyan]Inventory of {char_name}[/bold cyan]"
        self.displayPanel(panel_title, lines, 60, self.panel_style)




    def displayQuestList(self, quests, index):
        quest_lines = []  

        for i, quest in enumerate(quests):
            quest_name = quest.get("QuestName", "Quest unknown")   # dans le cas où on sait pas recupérer le name de la quest --> affiche quest unknown
            
            if i == index:
                style = self.selected_style
                quest_pointer = "-> "
            else:
                style = self.default_style
                quest_pointer = " "

            quest_lines.append(Text(f"{quest_pointer}{quest_name}", style=style) +Text("\n"))

        panel_title="[bold yellow] Quests List [/bold yellow]"
        self.displayPanel(panel_title, quest_lines, 60, self.panel_style)
        

    def displayQuestInfo(self, quest):
        name = quest.get("QuestName")
        description = quest.get("Description", "No description.")  #no description si y a pas de description
        experience = quest.get("Experience")
        gold = quest.get("Gold", 0)
        difficulty = quest.get("Difficulty")
        reward = quest.get("Item", None)

        #lignes à afficher
        lines = [ 
        Text(f"Name : {name}", style="bold cyan"),
        Text(f"Difficulty : {difficulty}", style="bold cyan"),
        Text(f"Experience : {experience}", style="bold cyan"),
        Text(f"Gold : {gold}", style="bold cyan"),
        ]

        lines.append(Text("\nDescription :", style="bold cyan"))
        lines.append(Text(description, style="cyan"))

        panel_title="[bold green] Quest information [/bold green]"
        self.displayPanel(panel_title, lines, 80, self.panel_style)


    
    def  displayAllMonsters(self, monsters, index):
        lines = []

        for i, monster in enumerate(monsters):
            monster_name = monster.get("MonsterName")

            if i == index:
                style = self.selected_style
                monster_pointer = "→ "
            else:
                style = self.default_style
                monster_pointer = " "
            
            lines.append(Text(f"{monster_pointer}{monster_name}", style=style) +Text("\n"))

        panel_title = "[bold red]Monsters[/bold red]"
        self.displayPanel(panel_title, lines, 60, "bright_magenta") 


    
    def displayMonsterInfo(self, monster, loots):
        lines = []

        lines.append(Text(f"Name: {monster.get('MonsterName')}", style="bold"))
        lines.append(Text(f"Attack: {monster.get('Attack')}"))
        lines.append(Text(f"Defense: {monster.get('Defense')}"))
        lines.append(Text(f"Life Points: {monster.get('LifePoints')}\n"))

        if loots:
            lines.append(Text("Loots:", style="bold underline"))
            for loot in loots:
                if loot["type"] == "item":
                    lines.append(Text(f"  {loot['ItemName']} x{loot['AmountItem']} ({loot['Probability']}%)"))
                else:
                    lines.append(Text(f"  Gold: {loot['GoldQuantity']} ({loot['GoldProbability']}%)"))
        else:
            lines.append(Text("No loot info available."))

        panel_title = "[bold red]Monster Details[/bold red]"
        self.displayPanel(panel_title, lines, 60, "bright_magenta")


    

    def displayNpcList(self, npcs, index):
        lines = []

        for i, npc in enumerate(npcs):
            npc_name = npc.get("npcName")

            if i == index:
                style = self.selected_style
                pointer = "→ "
            else:
                style = self.default_style
                pointer = "  "

            lines.append(Text(f"{pointer}{npc_name}", style=style) + Text("\n"))

        panel_title = "[bold green]NPC List[/bold green]"
        self.displayPanel(panel_title, lines, 60, "bright_magenta")


    
    def displayQuestListNpc(self, quests, index):
        lines = []

        for i, quest in enumerate(quests):
            quest_title = quest.get("QuestTitle") or quest.get("Title") or "Unnamed Quest"

            if i == index:
                style = self.selected_style
                pointer = "→ "
            else:
                style = self.default_style
                pointer = "  "

            lines.append(Text(f"{pointer}{quest_title}", style=style) + Text("\n"))

        panel_title = "[bold green]Quests List[/bold green]"
        self.displayPanel(panel_title, lines, 60, "bright_cyan")





    def displayPanel(self, title: str, lines: list, width, border_color: str = "bright_magenta",):
        """
        Affiche un panel générique avec un titre, 
        une liste de lignes et un style.
        """
        panel = Panel(
            Text.assemble(*[line + Text("\n") for line in lines]),
            title=title,
            border_style=border_color,
            width=width,
            padding=(1, 4),
        )
        self.console.clear()
        self.console.print(panel)


    def displayRanking(self, ranking_title: str, rows: list[dict]):
        """
        Show the ranking.
        """

        self.console.clear()

        columns = list(rows[0].keys())
        table = Table(show_header=True, header_style="bold magenta")

        for col in columns:
            table.add_column(col)

        for row in rows:
            table.add_row(*(str(row[col]) for col in columns))

        panel = Panel(table, title=f"[bold yellow]{ranking_title}[/bold yellow]", border_style="magenta")
        self.console.print(panel)






    def displayProfile(self, info: dict):
        """
        Render the players profile in a small table inside a Panel.
        Expects a dict with keys:
          - Username
          - Level
          - MoneyGold
          - InventorySlots
        """

        self.console.clear()

        table = Table(show_header=False, box=None, pad_edge=False)
        table.add_column(justify="right", style="cyan", no_wrap=True)
        table.add_column()

        table.add_row("Username:", str(info.get("Username", "")))
        table.add_row("Password:", str(info.get("Password", "")))
        table.add_row("Level:", str(info.get("Level", "")))
        table.add_row("Money:", str(info.get("MoneyGold", "")))
        table.add_row("Exp:", str(info.get("Experience", "")))
        table.add_row("Inventory Slots:", str(info.get("InventorySlots", "")))

        panel = Panel(
            table,
            title="[bold yellow]My Profile[/bold yellow]",
            border_style="magenta",
            padding=(1, 2),
            width=50,
        )
        self.console.print(panel)