import json
import os
import time
from datetime import datetime
from pathlib import Path

from games.game_strategy import GameStrategy
from modules.image_processing import ImageUtils
from modules.logger_config import main_logger


class AvaEthernityBot(GameStrategy):

    def __init__(self):
        self.config_path = Path("games/configs/ava_ethernity_bot.json")
        self.assets_path = os.path.join('games', 'strategies', 'ava_ethernity_bot')  # Оновлено шлях до асетів

    def launch(self):
        main_logger.info("Launching Ava ETHERNITY game...")
        time.sleep(3)

        play_button_image = os.path.join(self.assets_path, 'play_button.png')
        if ImageUtils.find_and_click_image(play_button_image, confidence=0.8):
            main_logger.info("Play button found and clicked.")
        else:
            main_logger.error("Play button not found! Check the screen and the image.")

    def collect_offline_bonus(self):
        main_logger.info("Collecting offline bonus...")
        # Логіка для збору офлайн бонусу

    def perform_basic_actions(self):
        main_logger.info("Performing basic actions...")
        # Логіка для виконання базових активностей

    def check_additional_activities(self):
        main_logger.info("Checking for additional activities...")
        # Логіка для перевірки додаткових активностей

    def record_last_access_time(self):
        access_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        main_logger.info(f"Recording last access time: {access_time}")

        # Оновлюємо конфігураційний файл
        if self.config_path.exists():
            with open(self.config_path, "r") as file:
                config_data = json.load(file)

            config_data["last_access_time"] = access_time  # Додаємо новий параметр

            with open(self.config_path, "w") as file:
                json.dump(config_data, file, indent=4)
        else:
            main_logger.error(f"Configuration file not found at {self.config_path}")

    def play_game(self):
        """Метод, що містить всю логіку гри."""
        self.launch()
        self.collect_offline_bonus()
        self.perform_basic_actions()
        self.check_additional_activities()
        self.record_last_access_time()