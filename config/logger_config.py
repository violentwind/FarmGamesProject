import logging
import os
from colorlog import ColoredFormatter


def setup_logger(log_file='logs/project.log', level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Define the color formatter
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'bold_blue',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_purple',
            'SUCCESS': 'bold_green',
        }
    )

    # File handler logs to file without colors
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"))

    # Console handler logs to the console with colors
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Initialization of the main logger
main_logger = setup_logger()
