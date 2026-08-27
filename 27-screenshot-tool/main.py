import pyautogui
from datetime import datetime
import os


def take_screenshot():
    folder = "screenshots"

    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)

    print("\n===== Screenshot Tool =====")
    print("Screenshot captured successfully!")
    print("Saved to:", filepath)


take_screenshot()
