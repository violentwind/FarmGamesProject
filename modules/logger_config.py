import logging
import os

from colorlog import ColoredFormatter


def setup_logger(log_file='logs/project.log', level=logging.INFO):
    """
    Sets up the logging configuration for the project.

    This function configures both a file handler and a console handler with color formatting
    to log messages of various severity levels.

    Parameters:
    log_file (str): The file path where logs will be stored. Defaults to 'logs/project.log'.
    level (int): The logging level threshold. Defaults to logging.INFO.

    Returns:
    logging.Logger: A configured logger instance.
    """
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Define the color formatter for console output
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
            'SUCCESS': 'bold_green',  # Custom log level (if used)
        }
    )

    # File handler logs to a file without colors
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"))

    # Console handler logs to the console with colors
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Create a logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(level)  # Set the logging threshold level
    logger.addHandler(file_handler)  # Add the file handler to the logger
    logger.addHandler(console_handler)  # Add the console handler to the logger

    return logger


# Initialization of the main logger instance for the project
main_logger = setup_logger()
