import os
import pyautogui
from PIL import Image
import cv2
import numpy as np
import time


def Screenshot(folder, active_window):
    
    def resize_image(image, target_width, target_height):
        return image.resize((target_width, target_height), Image.LANCZOS)

    def take_and_resize_screenshot(target_width, target_height):

            # Get the position and size of the Rocket League window
            left, top, width, height = active_window.left, active_window.top, active_window.width, active_window.height

            # Capture the screenshot of the Rocket League window
            screenshot = pyautogui.screenshot(region=(left, top, width, height))

            # Resize the screenshot to 1080p
            resized_screenshot = resize_image(screenshot, target_width, target_height)

            # Save the resized screenshot with an incremental filename
            file_path = f"{folder}/frame.jpg"
            resized_screenshot.save(file_path)


    
    target_width, target_height = 1920, 1080  # 1080p resolution
    take_and_resize_screenshot(target_width, target_height)

def Photo(cap, folder):

    ret, frame = cap.read()
    if ret:
        # Convert the frame to a PIL image
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Resize the image
        max_size = 250
        ratio = max_size / max(pil_img.size)
        new_size = tuple([int(x*ratio) for x in pil_img.size])
        resized_img = pil_img.resize(new_size, Image.LANCZOS)

        # Convert the PIL image back to an OpenCV image
        frame = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)

        # Save the frame as an image file
        path = f"{folder}/frame.jpg"
        cv2.imwrite(path, frame)
    else:
        print("Failed to capture image")

    
