import pyautogui
import random
import time

def press_keys(keys):
    pyautogui.keyDown(keys[0])
    for key in keys[1:]:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    pyautogui.keyUp(keys[0])

while True:
    # Press alt+tab
    press_keys(['alt', 'tab'])
    
    # Generate a random wait time within one minute
    wait_time = random.uniform(0, 60)
    print(f"Waiting for {wait_time:.2f} seconds...")
    time.sleep(wait_time)
    
    # Press alt+tab+tab
    press_keys(['alt', 'tab', 'tab'])
    
    # Generate another random wait time
    wait_time = random.uniform(0, 60)
    print(f"Waiting for {wait_time:.2f} seconds...")
    time.sleep(wait_time)
    
    # Press alt+tab again
    press_keys(['alt', 'tab'])