import pyautogui
import random
import time

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

try:
    while True:
        # Generate random coordinates within the screen boundaries
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)

        # Move the mouse to the random coordinates
        pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

        # Wait for a random interval before moving again
        time.sleep(random.uniform(0.5, 2))
except KeyboardInterrupt:
    print("\nProgram terminated.")
