import os
import subprocess
import winreg as reg
from pathlib import Path
from typing import Optional

from modules.logger_config import main_logger


def find_telegram() -> Optional[Path]:
    """
    Searches for the Telegram executable in common installation paths and the Windows registry.

    Returns:
    Optional[Path]: The path to the Telegram executable if found, otherwise None.
    """
    main_logger.info("Searching for Telegram executable...")

    possible_paths = [
        Path("C:\\Program Files\\Telegram Desktop\\Telegram.exe"),
        Path("C:\\Program Files (x86)\\Telegram Desktop\\Telegram.exe"),
        Path(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    ]

    for path in possible_paths:
        if path.exists():
            main_logger.info(f"Found Telegram at {path}")
            return path

    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER,
                         r"Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Telegram Desktop") as key:
            path, _ = reg.QueryValueEx(key, "InstallLocation")
            telegram_exe = Path(path) / "Telegram.exe"
            if telegram_exe.exists():
                main_logger.info(f"Found Telegram via registry at {telegram_exe}")
                return telegram_exe
    except FileNotFoundError:
        main_logger.error("Telegram not found in registry.")
    except Exception as e:
        main_logger.error(f"Unexpected error while searching in registry: {e}")

    main_logger.error("Telegram not found.")
    return None


def launch_telegram() -> Optional[Path]:
    """
    Launches the Telegram application if it is found on the system.

    Returns:
    Optional[Path]: The path to the launched Telegram executable, or None if it could not be found or launched.
    """
    try:
        telegram_path = find_telegram()

        if telegram_path:
            main_logger.info(f"Launching Telegram from {telegram_path}")
            subprocess.Popen(str(telegram_path))
            return telegram_path
        else:
            main_logger.error("Telegram could not be found. Please ensure Telegram is installed.")
            return None
    except Exception as e:
        main_logger.error(f"Failed to launch Telegram: {e}")
        return None
