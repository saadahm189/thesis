import pyautogui
import time
import random

try:
    while True:
        # Generate a random interval between 10 and 60 seconds
        random_interval = random.uniform(10, 60)
        time.sleep(random_interval)  # Wait for the random interval
        # Press Alt+Tab
        pyautogui.hotkey('alt', 'tab')
        # Sleep to allow the Alt+Tab switch to complete before pressing again
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram terminated.")