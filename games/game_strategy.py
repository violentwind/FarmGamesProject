# game_strategy.py

from abc import ABC, abstractmethod


class GameStrategy(ABC):

    @abstractmethod
    def launch(self):
        """Запускає гру з відкритого чату."""
        pass

    @abstractmethod
    def collect_offline_bonus(self):
        """Збирає офлайн бонус, якщо він є."""
        pass

    @abstractmethod
    def perform_basic_actions(self):
        """Виконує базові активності в грі."""
        pass

    @abstractmethod
    def check_additional_activities(self):
        """Перевіряє наявність додаткових активностей."""
        pass

    @abstractmethod
    def record_last_access_time(self):
        """Записує час останнього входу в гру."""
        pass
