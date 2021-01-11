from ctypes import *
import keyboard
	
block_shortcut = 'alt+x' #Block Shortcut
unblock_shortcut = 'alt+c' #Unblock Shortcut
emergency_shortcut = 'alt+esc' #emergency shorcut use this if your desired shortcut doesnt work.
print("block:", block_shortcut) #you can comment this out if you want to.
print("unblock:", unblock_shortcut) 

def trigger():
    print("block shortcut triggered")
    windll.user32.BlockInput(True)

def trigger_unblock():
    print("unblock shortcut triggered")
    windll.user32.BlockInput(False)
    
keyboard.add_hotkey(block_shortcut, trigger)
keyboard.add_hotkey(unblock_shortcut, trigger_unblock)
 
keyboard.wait(emergency_shortcut)
#ok = windll.user32.BlockInput(True) #enable block

#or 

#ok = windll.user32.BlockInput(False) #disable block 

