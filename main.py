import pyautogui
import cv2
import numpy as np
import time
import os

def find_and_click_image(image_path):
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    
    threshold = 0.8 
    loc = np.where(result >= threshold)

    if loc[0].size > 0 and loc[1].size > 0:
        point = (loc[1][0], loc[0][0]) 
        print(f"Görsel bulundu! Tıklanacak koordinatlar: {point}")

        pyautogui.click(point)
        return True
    else:
        return False

def get_images_from_directory(directory):
    valid_extensions = ('.png', '.jpg', '.jpeg')
    images = [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]
    return images

def main():
    current_directory = os.getcwd()
    images_to_click = get_images_from_directory(current_directory)
    
    if not images_to_click:
        print("Bu dizinde tıklanacak görsel bulunamadı.")
        return

    print(f"Görseller bulundu: {images_to_click}")

    while True:
        for image_name in images_to_click:
            image_path = os.path.join(current_directory, image_name)
            if find_and_click_image(image_path):
                print(f"{image_name} görseline tıklama yapıldı!")
        time.sleep(0.001) 

if __name__ == "__main__":
    main()
