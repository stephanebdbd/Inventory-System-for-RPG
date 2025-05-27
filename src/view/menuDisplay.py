from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from model.menu import Menu

class MenuDisplay:
    def __init__(self):
        self.console = Console()
        self.selected_style = Style(color="white", bgcolor="blue", bold=True)
        self.default_style = Style(color="cyan")
        self.panel_style = Style(color="magenta", bold=True)

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

    def displayLoginRegister(self, ):
        pass