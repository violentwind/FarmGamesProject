import os
from typing import Optional, Type
from launcher.launcher import launch_telegram, open_telegram_chat
from start_menu.start_menu import StartMenu
from modules.config_manager import ConfigManager
from config.logger_config import main_logger


def load_game_class(game_module_name: str, game_class_name: str) -> Optional[Type]:
    try:
        module = __import__(f"games.{game_module_name}", fromlist=[game_class_name])
        main_logger.info(f"Successfully imported module: games.{game_module_name}")
        game_class = getattr(module, game_class_name)
        main_logger.info(f"Successfully loaded class: {game_class_name} from module: {game_module_name}")
        return game_class

    except ImportError as ie:
        main_logger.error(f"ImportError: Failed to import module games.{game_module_name}: {ie}")
    except AttributeError as ae:
        main_logger.error(f"AttributeError: Module {game_module_name} does not have class {game_class_name}: {ae}")
    except Exception as e:
        main_logger.error(f"Unexpected error when loading class {game_class_name} from {game_module_name}: {e}")

    return None


def load_all_game_configs() -> list[dict[str, any]]:
    configs: list[dict[str, any]] = []
    config_dir = os.path.join("config", "games")

    for filename in os.listdir(config_dir):
        if filename.endswith(".json"):
            bot_id = filename.replace(".json", "")
            config_manager = ConfigManager(bot_id)
            config = config_manager.get_config()
            configs.append(config)

    return configs


def main() -> None:
    main_logger.info("Starting the FarmGamesProject")

    game_configs = load_all_game_configs()

    if not game_configs:
        main_logger.error("No game configurations found. Exiting.")
        return

    menu = StartMenu(game_configs)
    selected_games = menu.run()

    if not selected_games:
        main_logger.error("No games selected. Exiting.")
        return

    for game in selected_games:
        main_logger.info(f"Launching Telegram and opening chat for {game['bot_name']}...")
        telegram_path = launch_telegram()
        if telegram_path:
            open_telegram_chat(game["bot_id"])

            game_module_name = f"{game['bot_id'].lower().replace(' ', '_')}_game"
            game_class_name = ''.join(word.capitalize() for word in game['bot_id'].split('_'))
            game_class = load_game_class(game_module_name, game_class_name)

            if game_class:
                game_instance = game_class()
                game_instance.play_game()

                main_logger.info(f"Finished playing {game['bot_name']}")
            else:
                main_logger.error(f"Failed to load game logic for {game['bot_name']}")
        else:
            main_logger.error(f"Failed to launch Telegram for {game['bot_name']}")


if __name__ == "__main__":
    main()
