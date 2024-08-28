import tkinter as tk
from tkinter import messagebox
from typing import List, Dict, Any


class StartMenu:
    def __init__(self, configs: List[Dict[str, Any]]) -> None:
        """
        Initialize the StartMenu with the list of game configurations.

        Parameters:
        configs (List[Dict[str, Any]]): A list of dictionaries, each containing game configuration data.
        """
        self.root = tk.Tk()
        self.root.title("Farm Games Project Launcher")

        self.games = configs
        self.selected_games = []

        # Dictionary to store the BooleanVars linked to each game's bot_name
        self.game_vars = {game['bot_name']: tk.BooleanVar() for game in self.games}

        # Create check buttons for each game
        for game in self.games:
            chk = tk.Checkbutton(self.root, text=game["bot_name"], variable=self.game_vars[game['bot_name']])
            chk.pack(anchor='w')

        # Add a start button to launch the selected games
        self.start_button = tk.Button(self.root, text="Start", command=self.start_selected_games)
        self.start_button.pack()

    def start_selected_games(self) -> None:
        """
        Collect selected games and quit the menu.

        This method checks which games have been selected and stores them in the
        'selected_games' attribute. If no games are selected, a warning message is displayed.
        """
        self.selected_games = [
            game for game in self.games if self.game_vars[game['bot_name']].get()
        ]
        if not self.selected_games:
            messagebox.showwarning("No game selected", "Please select at least one game to launch.")
        else:
            self.root.quit()

    def run(self) -> List[Dict[str, Any]]:
        """
        Run the Tkinter main loop and return the selected games.

        Returns:
        List[Dict[str, Any]]: A list of dictionaries containing the configurations of the selected games.
        """
        self.root.mainloop()
        return self.selected_games
