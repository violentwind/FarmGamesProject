import logging

import pyautogui


def resize_image(image_path: str, output_path: str, size: tuple[int, int]) -> None:
    """
    Resizes an image to the specified dimensions.

    Parameters:
    image_path (str): The path to the input image.
    output_path (str): The path where the resized image will be saved.
    size (tuple[int, int]): The target size as a tuple (width, height).
    """
    image = Image.open(image_path)

    # Resize the image to the target size
    resized_image = image.resize(size)

    # Save the resized image to the output path
    resized_image.save(output_path)


def convert_image_to_grayscale(image_path: str, output_path: str) -> None:
    """
    Converts an image to grayscale.

    Parameters:
    image_path (str): The path to the input image.
    output_path (str): The path where the grayscale image will be saved.
    """
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert("L")

    # Save the grayscale image to the output path
    image.save(output_path)


def compress_image(image_path: str, output_path: str, quality: int = 85) -> None:
    """
    Compresses an image and saves it with the specified quality.

    Parameters:
    image_path (str): The path to the input image.
    output_path (str): The path where the compressed image will be saved.
    quality (int): The quality of the output image, on a scale from 1 (worst) to 95 (best). Default is 85.
    """
    # Open the image and compress it with the specified quality
    image = Image.open(image_path)
    image.save(output_path, "JPEG", quality=quality)


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


from PIL import Image


def resize_image(image_path: str, output_path: str, size: tuple[int, int]) -> None:
    image = Image.open(image_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)


def convert_image_to_grayscale(image_path: str, output_path: str) -> None:
    image = Image.open(image_path).convert("L")
    image.save(output_path)


def compress_image(image_path: str, output_path: str, quality: int = 85) -> None:
    image = Image.open(image_path)
    image.save(output_path, "JPEG", quality=quality)
