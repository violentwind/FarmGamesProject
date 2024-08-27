import tkinter as tk
from tkinter import messagebox

class StartMenu:
    def __init__(self, configs: list[dict[str, any]]) -> None:
        """Initialize the StartMenu with the list of game configurations."""
        self.root: tk.Tk = tk.Tk()
        self.root.title("Farm Games Project Launcher")
        self.selected_games: list[dict[str, any]] = []
        self.games: list[dict[str, any]] = configs

        self.check_buttons: list[tk.Checkbutton] = []
        self.vars: list[tk.BooleanVar] = []
        for game in self.games:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.root, text=game["bot_name"], variable=var)
            chk.pack(anchor='w')
            self.check_buttons.append(chk)
            self.vars.append(var)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_selected_games)
        self.start_button.pack()

    def start_selected_games(self) -> None:
        """Collect selected games and quit the menu."""
        self.selected_games = [game for game, var in zip(self.games, self.vars) if var.get()]
        if not self.selected_games:
            messagebox.showwarning("No game selected", "Please select at least one game to launch.")
        else:
            self.root.quit()

    def run(self) -> list[dict[str, any]]:
        """Run the Tkinter main loop and return the selected games."""
        self.root.mainloop()
        return self.selected_games
