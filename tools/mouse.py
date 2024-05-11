import pyautogui
import random
import time

# Get the screen size
screen_width, screen_height = pyautogui.size()

while True:
    # Randomly choose new coordinates within the screen boundaries
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the new coordinates
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

    # Randomly choose to scroll up or down (20% chance)
    if random.random() < 0.2:
        scroll_amount = random.randint(-50, 50)
        pyautogui.scroll(scroll_amount)

    # Randomly choose a small delay before the next movement
    time.sleep(random.uniform(0.1, 0.5))