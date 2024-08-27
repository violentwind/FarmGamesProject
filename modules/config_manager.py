import json
import os
from config.logger_config import main_logger


class ConfigManager:
    def __init__(self, bot_id: str) -> None:
        self.config_path: str = os.path.join("config", "games", f"{bot_id}.json")
        main_logger.debug(f"Initializing ConfigManager with bot_id: {bot_id}")
        self.config: dict[str, any] = self._load_config()

    def _load_config(self) -> dict[str, any]:
        if not os.path.exists(self.config_path):
            main_logger.error(f"Configuration file not found: {self.config_path}")
            raise FileNotFoundError(f"Configuration file not found for {self.config_path}")

        with open(self.config_path, 'r') as file:
            config = json.load(file)
            main_logger.info(f"Configuration loaded successfully for {self.config_path}")
            return config

    def get_config(self) -> dict[str, any]:
        return self.config
