import json
import time
from pynput import keyboard, mouse

data = []
start_time = time.time()

def on_click(x, y, button, pressed):
    duration = time.time() - start_time
    if pressed:
        data.append({'event': 'click', 'x': x, 'y': y, 'button': str(button), 'time': duration})
        print(f"Click at ({x}, {y}) with {button} at {duration:.2f}s")

def on_press(key):
    duration = time.time() - start_time
    try:
        if key.char == '=':  # Change 'q' to whatever key you want to use for exit
            print("Exiting...")
            save_data()
            return False  # Stop listener
        data.append({'event': 'keypress', 'key': key.char, 'time': duration})
        print(f"Key pressed: {key.char} at {duration:.2f}s")
    except AttributeError:
        data.append({'event': 'keypress', 'key': str(key), 'time': duration})
        print(f"Special key pressed: {key} at {duration:.2f}s")

def save_data():
    with open('keylog.json', 'w') as f:
        json.dump(data, f)

mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

try:
    mouse_listener.join()
    keyboard_listener.join()
except KeyboardInterrupt:
    save_data()
    print("Keylogger stopped and data saved.")


