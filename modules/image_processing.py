import logging

import pyautogui


class ImageUtils:
    @staticmethod
    def find_and_click_image(image_path, confidence=0.8):
        """
        Шукає зображення на екрані. Якщо знайдено - натискає на нього.

        Параметри:
        ----------
        image_path (str): Шлях до зображення.
        confidence (float): Впевненість при пошуку зображення (від 0 до 1).

        Повертає:
        --------
        bool: True, якщо зображення знайдено і натиснуто, інакше False.
        """
        try:
            # Шукаємо зображення на екрані
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                pyautogui.click(location)
                logging.log(logging.INFO, f"Image found and clicked: {image_path}")
                return True
            else:
                logging.log(logging.ERROR, f"Image not found on screen: {image_path}")
                return False
        except Exception as e:
            logging.log(logging.ERROR, f"An error occurred while trying to find and click image: {str(e)}")
            return False
