import logging
import os
import platform
import subprocess
import winreg as reg
from pathlib import Path


def find_telegram():
    logging.log(logging.INFO,"Searching for Telegram executable...")

    possible_paths = [
        Path("C:\\Program Files\\Telegram Desktop\\Telegram.exe"),
        Path("C:\\Program Files (x86)\\Telegram Desktop\\Telegram.exe"),
        Path(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    ]

    for path in possible_paths:
        if path.exists():
            logging.log(logging.INFO,f"Found Telegram at {path}")
            return path

    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER,
                         r"Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Telegram Desktop") as key:
            path, _ = reg.QueryValueEx(key, "InstallLocation")
            telegram_exe = Path(path) / "Telegram.exe"
            if telegram_exe.exists():
                logging.log(logging.INFO,f"Found Telegram via registry at {telegram_exe}")
                return telegram_exe
    except FileNotFoundError:
        logging.log(logging.ERROR,"Telegram not found in registry.")
    except Exception as e:
        logging.log(logging.ERROR,f"Unexpected error while searching in registry: {e}")

    logging.log(logging.ERROR,"Telegram not found.")
    return None

def launch_telegram():
    try:
        telegram_path = find_telegram()

        if telegram_path:
            logging.log(logging.INFO, f"Launching Telegram from {telegram_path}")
            subprocess.Popen(str(telegram_path))
            return telegram_path
        else:
            logging.log(logging.ERROR,"Telegram could not be found. Please ensure Telegram is installed.")
            return None
    except Exception as e:
        logging.log(logging.ERROR,f"Failed to launch Telegram: {e}")
        return None

def open_telegram_chat(bot_id):
    telegram_url = f"tg://resolve?domain={bot_id}"
    logging.log(logging.INFO,f"Attempting to open Telegram chat with bot: {bot_id}")

    if platform.system() == "Windows":
        try:
            subprocess.Popen(["start", telegram_url], shell=True)
            logging.log(logging.INFO,f"Successfully opened chat with bot: {bot_id}")
        except Exception as e:
            logging.log(logging.ERROR,f"Failed to open chat with bot: {bot_id}. Error: {e}")
    else:
        logging.log(logging.ERROR,"This application is designed to work on Windows only.")

if __name__ == "__main__":
    launch_telegram()
