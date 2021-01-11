from ctypes import *
import keyboard

shortcut = 'alt+x' #define your hot-key
shortcut2 = 'alt+c'
print('Hotkey set as:', shortcut)

def trigger():
    print("block shortcut triggered")
    windll.user32.BlockInput(True)

def trigger_unblock():
    print("unblock shortcut triggered")
    windll.user32.BlockInput(False)
    
keyboard.add_hotkey(shortcut, trigger)
keyboard.add_hotkey(shortcut2, trigger_unblock)

print("esc to stop")
keyboard.wait("esc")
#ok = windll.user32.BlockInput(True) #enable block

#or 

#ok = windll.user32.BlockInput(False) #disable block 

