import json
import logging
import os

def generate_config():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Отримуємо абсолютний шлях до кореневої директорії проекту
    games_config_dir = os.path.join(base_dir, "config", "games_config") # Директория з конфігураційними файлами ігор
    general_config_file = os.path.join(base_dir, "config", "config.json") # Ім'я файлу для загального конфігураційного файлу

    if not os.path.exists(games_config_dir):
        logging.log(logging.ERROR,"Games config directory not found.")
        return

    games = []

    for filename in os.listdir(games_config_dir):
        if filename.endswith("_config.json"):
            with open(os.path.join(games_config_dir, filename), "r") as file:
                game_data = json.load(file)
                selected_data = {
                    "bot_name": game_data.get("bot_name"),
                    "bot_id": game_data.get("bot_id"),
                    "launch_button_icon": game_data.get("launch_button_icon")
                }
                games.append(selected_data)

    if games:
        with open(general_config_file, "w") as file:
            json.dump({"games": games}, file, indent=4)
            logging.log(logging.INFO,"Configuration file generated.")
    else:
        logging.log(logging.ERROR,"No games found to add to the config file.")


if __name__ == "__main__":
    generate_config()
