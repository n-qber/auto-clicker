from pynput.mouse import Controller, Button
from pynput.keyboard import Listener
from threading import Thread
from time import sleep

TPC = .05
CLICK = False
mouse = Controller()

def start_clicking():
    #print("[*] Start clicking")
    global CLICK
    if CLICK:
        return
    CLICK = True
    while CLICK:
        mouse.click(Button.left, 1)
        sleep(TPC)

def stop_clicking():
    #print("[*] Stop clicking")
    global CLICK
    CLICK = False

def toggle_clicking():
    #print("[*] Toggle clicking")
    global CLICK
    if CLICK:
        CLICK = False
        return
    Thread(target=start_clicking).start()

press = {"c": lambda: Thread(target=start_clicking).start(),
         "t": lambda: Thread(target=toggle_clicking).start()}

release = {"c": lambda: Thread(target=stop_clicking).start()}

def on_press(key):
    if hasattr(key, "char"):
        press.get(key.char, lambda:None)()

def on_release(key):
    if hasattr(key, "char"):
        release.get(key.char, lambda: None)()

print("======= AUTO CLICKER 1.0 =======")
print("[*] Author: Nicolas Bertozzo\n\n")
print("[*] Press C: start clicking\n[*] Release C: stop clicking\n[*] Press T: toggle clicking")

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
