from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from model.menu import Menu
from rich.text import Text

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
            width=50,
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
    
    def displayCharacter(self, character, stats):
        pass
