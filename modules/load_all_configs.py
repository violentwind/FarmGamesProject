import json
import os
from typing import List, Dict, Any

from modules.logger_config import main_logger


def load_all_configs() -> List[Dict[str, Any]]:
    """
    Loads the required fields from the configuration files for all games.

    This function searches through the 'games' directory, finds all subdirectories, and
    attempts to load the 'bot_name' and 'last_access_time' fields from each 'config.json' file.
    It returns a list of dictionaries containing only these fields for each game.

    Returns:
    List[Dict[str, Any]]: A list of dictionaries, each containing the 'bot_name' and 'last_access_time' for a game.
    """
    game_configs = []
    games_directory = os.path.join(os.path.dirname(__file__), '..', 'games')

    # Перевіряємо, чи існує директорія ігор
    if not os.path.exists(games_directory):
        main_logger.error(f"Games directory not found: {games_directory}")
        return game_configs

    # Список директорій, які потрібно пропустити
    exclude_dirs = {"__pycache__"}

    for game_folder in os.listdir(games_directory):
        game_path = os.path.join(games_directory, game_folder)

        # Перевіряємо, що це директорія і що вона не у списку виключених
        if not os.path.isdir(game_path) or game_folder in exclude_dirs:
            continue

        config_file = os.path.join(game_path, "config.json")

        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as file:
                    config = json.load(file)

                    # Витягуємо лише необхідні поля
                    bot_info = {
                        'bot_name': config.get('bot_name', 'Unknown'),
                        'last_access_time': config.get('last_access_time', 'N/A')
                    }
                    main_logger.info(f"Configuration loaded successfully for {config_file}")
                    game_configs.append(bot_info)
            except json.JSONDecodeError as e:
                main_logger.error(f"JSONDecodeError: Failed to parse {config_file}: {e}")
            except Exception as e:
                main_logger.error(f"Unexpected error loading configuration for {config_file}: {e}")
        else:
            main_logger.warning(f"No config.json found in {game_path}")

    if not game_configs:
        main_logger.warning("No valid game configurations were found.")

    return game_configs
