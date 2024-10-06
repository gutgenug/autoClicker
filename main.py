import time
from pynput.mouse import Button, Controller
from pynput import keyboard
import threading

mouse = Controller()
running = False

def on_press(key):
    global running
    try:
        if key.char == 'k': # Key to start the auto clicker
            running = True
        elif key.char == 'h': # Key to stop the auto clicker
            running= False
    except AttributeError:
        pass


def autoclicker():
    while True:
        if running:
            mouse.click(Button.left)
            time.sleep(0.01) # The click interval(in seconds)
        else:
            time.sleep(1)


loop_thread = threading.Thread(target=autoclicker, daemon=True)
loop_thread.start()

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    print("Press 'k' to start the clicker and 'h' to stop it.")
    listener.join()  # Keep the listener running