from modules.load_all_configs import load_all_configs
from modules.logger_config import main_logger
from modules.telegram_launcher import launch_telegram
from start_menu.start_menu import StartMenu


def main():
    # Log the start of the program
    main_logger.info("Starting the Farm Games Project...")

    # Load game configurations
    configs = load_all_configs()

    # If no configurations were found, exit the program
    if not configs:
        main_logger.error("No game configurations found. Exiting.")
        return

    # Initialize and run the start menu
    menu = StartMenu(configs)
    selected_games = menu.run()

    # Log the selected games
    if selected_games:
        main_logger.info(f"Selected games: {[game['bot_name'] for game in selected_games]}")

        # Launch Telegram
        telegram_path = launch_telegram()
        if not telegram_path:
            main_logger.error("Failed to launch Telegram. Exiting.")
            return

        # Тут можна додати код для запуску вибраних ігор через Telegram
    else:
        main_logger.warning("No games selected.")

if __name__ == "__main__":
    main()