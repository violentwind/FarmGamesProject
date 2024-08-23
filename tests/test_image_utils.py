import sys
import os

# Додаємо кореневий шлях проекту до sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.insert(0, project_root)

import cv2
from modules.image_processing.image_utils import ImageUtils, ScreenUtils

def test_get_screen_resolution():
    width, height = ScreenUtils.get_screen_resolution()
    print(f"Current screen resolution: {width}x{height}")

def test_scale_image():
    screen_width, screen_height = ScreenUtils.get_screen_resolution()
    scaled_image = ImageUtils.scale_image('assets/ava_ethernity_bot/play_button.png', screen_width, screen_height)

    # Збереження масштабованого зображення для перевірки
    cv2.imwrite('assets/ava_ethernity_bot/scaled_play_button.png', scaled_image)
    print("Scaled image saved successfully.")

# Запуск тесту
if __name__ == "__main__":
    test_get_screen_resolution()  # Тестуємо отримання роздільної здатності
    test_scale_image()  # Тестуємо масштабування зображення
