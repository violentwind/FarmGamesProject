import json
import tkinter as tk
from tkinter import messagebox


class StartMenu:
    def __init__(self, config_path="config/config.json"):
        self.root = tk.Tk()
        self.root.title("Farm Games Project Launcher")
        self.selected_games = []

        # Завантаження конфігураційного файлу з іграми
        try:
            with open(config_path, "r") as file:
                config = json.load(file)
                self.games = config["games"]
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return

        # Створення чекбоксів для кожної гри
        self.checkbuttons = []
        self.vars = []
        for game in self.games:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(self.root, text=game["bot_name"], variable=var)
            chk.pack(anchor='w')
            self.checkbuttons.append(chk)
            self.vars.append(var)

        # Кнопка для запуску вибраних ігор
        self.start_button = tk.Button(self.root, text="Start", command=self.start_selected_games)
        self.start_button.pack()

    def start_selected_games(self):
        self.selected_games = [game for game, var in zip(self.games, self.vars) if var.get()]
        if not self.selected_games:
            messagebox.showwarning("No game selected", "Please select at least one game to launch.")
        else:
            self.root.quit()

    def run(self):
        self.root.mainloop()
        return self.selected_games

if __name__ == "__main__":
    menu = StartMenu()
    selected_games = menu.run()
    print(f"Selected games: {selected_games}")
