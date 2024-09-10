from pynput import mouse, keyboard
from PIL import ImageGrab, ImageFilter
import time
import threading
import os

# Configuration
config = {
    "capture_screenshots": True,
    "blur_screenshots": False,
    "screenshot_interval": 60,  # in seconds
    "inactive_time_threshold": 5,  # in seconds
}

# Define the path to the screenshots folder
screenshots_folder = os.path.join(os.getcwd(), "screenshots")

# Ensure the folder exists
if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)

# Variables to store the last known mouse position and activity state
last_activity_time = time.time()
is_active = True

def capture_screenshot():
    screenshot = ImageGrab.grab()
    if config["blur_screenshots"]:
        screenshot = screenshot.filter(ImageFilter.GaussianBlur(5))
    
    screenshot_path = os.path.join(screenshots_folder, f"screenshot_{int(time.time())}.png")
    
    screenshot.save(screenshot_path)
    print("Screenshot captured and saved")

def on_move(x, y):
    global last_activity_time, is_active
    last_activity_time = time.time()
    if not is_active:
        print("User is active.")
        is_active = True

def on_click(x, y, button, pressed):
    global last_activity_time, is_active
    last_activity_time = time.time()
    if not is_active:
        print("User is active.")
        is_active = True

def on_scroll(x, y, dx, dy):
    global last_activity_time, is_active
    last_activity_time = time.time()
    if not is_active:
        print("User is active.")
        is_active = True

def on_press(key):
    global last_activity_time, is_active
    last_activity_time = time.time()
    if not is_active:
        print("User is active.")
        is_active = True

def on_release(key):
    pass

def screenshot_scheduler():
    while True:
        if config["capture_screenshots"]:
            capture_screenshot()
        time.sleep(config["screenshot_interval"])

def inactivity_checker():
    global last_activity_time, is_active
    while True:
        current_time = time.time()
        if current_time - last_activity_time > config["inactive_time_threshold"]:
            if is_active:
                print("User is inactive.")
                is_active = False
        time.sleep(1)

def start_activity_monitoring():
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

    mouse_listener.start()
    keyboard_listener.start()

    screenshot_thread = threading.Thread(target=screenshot_scheduler)
    screenshot_thread.daemon = True
    screenshot_thread.start()

    inactivity_thread = threading.Thread(target=inactivity_checker)
    inactivity_thread.daemon = True
    inactivity_thread.start()

    print("User is active.") 
    mouse_listener.join()
    keyboard_listener.join()
