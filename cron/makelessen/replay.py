import json
import time
from pynput import keyboard, mouse

# Load data from JSON file
with open('keylog.json', 'r') as f:
    actions = json.load(f)

# Setup mouse and keyboard controllers
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Replay actions
start_time = time.time()

for action in actions:
    time.sleep(action['time'] - (time.time() - start_time))  # Wait for the right duration
    if action['event'] == 'click':
        x = action['x']
        y = action['y']
        button = mouse.Button.left if 'left' in action['button'] else mouse.Button.right
        mouse_controller.position = (x, y)
        mouse_controller.click(button)
        print(f"Clicked at ({x}, {y}) with {action['button']}")
    elif action['event'] == 'keypress':
        key = action['key']
        if len(key) == 1:  # Regular character
            keyboard_controller.press(key)
            keyboard_controller.release(key)
            print(f"Pressed key: {key}")
        else:  # Special key
            print(f"Pressed special key: {key}")
            print(f"Pressed special key: {key}")

print("Replay finished.")