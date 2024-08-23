import logging

from launcher.launcher import launch_telegram, open_telegram_chat
from scripts.generate_config import generate_config
from start_menu.start_menu import StartMenu
from modules.error_handling import setup_logging


def load_game_class(game_module_name, game_class_name):
    try:
        # Динамічно імпортуємо модуль гри
        module = __import__(f"games.{game_module_name}", fromlist=[game_class_name])
        logging.log(logging.INFO, f"Successfully imported module: games.{game_module_name}")

        # Динамічно отримуємо клас гри з модуля
        game_class = getattr(module, game_class_name)
        logging.log(logging.INFO, f"Successfully loaded class: {game_class_name} from module: {game_module_name}")

        return game_class

    except ImportError as ie:
        logging.log(logging.ERROR, f"ImportError: Failed to import module games.{game_module_name}: {ie}")
    except AttributeError as ae:
        logging.log(logging.ERROR,
                    f"AttributeError: Module {game_module_name} does not have class {game_class_name}: {ae}")
    except Exception as e:
        logging.log(logging.ERROR,
                    f"Unexpected error when loading class {game_class_name} from {game_module_name}: {e}")

    return None

def main():
    setup_logging()

    generate_config()

    menu = StartMenu()
    selected_games = menu.run()

    if not selected_games:
        logging.log(logging.ERROR, "No games available. Exiting.")
        return

    for game in selected_games:
        logging.log(logging.INFO, f"Launching Telegram and opening chat for {game['bot_name']}...")
        telegram_path = launch_telegram()
        if telegram_path:
            open_telegram_chat(game["bot_id"])

            # Динамічно завантажуємо клас гри
            game_module_name = f"{game['bot_id'].lower().replace(' ', '_')}_game"
            game_class_name = ''.join(word.capitalize() for word in game['bot_id'].split('_'))
            game_class = load_game_class(game_module_name, game_class_name)

            if game_class:
                # Створюємо екземпляр гри та викликаємо специфічну логіку гри
                game_instance = game_class()
                game_instance.play_game()  # Викликаємо метод, що містить всю логіку для цієї гри

                logging.log(logging.INFO, f"Finished playing {game['bot_name']}")
            else:
                logging.log(logging.ERROR, f"Failed to load game logic for {game['bot_name']}")
        else:
            logging.log(logging.ERROR, f"Failed to launch Telegram for {game['bot_name']}")

if __name__ == "__main__":
    main()
